from datetime import timedelta
from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from NewsPaper import settings
from .models import New, Category


@shared_task
def new_send(arg_id):
    instance = New.objects.get(id=arg_id)
    emails = User.objects.filter(
        subscriptions__category__in=instance.categories.all()
    ).values_list('email', flat=True)
    emails = set(emails)
    categories_post = ', '.join([cat.category for cat in instance.categories.all()])
    subject = f'В категориях {categories_post} свежая новость/статья!'

    text_content = (
        f'{instance.title}\n'
        f"{(instance.text[:150] + '...') if len(instance.text) > 150 else instance.text}\n"
        f'Чиатать полностью: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'{instance.title}<br.'
        f"{(instance.text[:150] + '...') if len(instance.text) > 150 else instance.text}<br>"
        f'Чиатать полностью на <a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@shared_task
def send_weekly():
    today = timezone.now()
    last_week = today - timedelta(days=7)
    posts = New.objects.filter(date_of_creation__gte=last_week).order_by('-date_of_creation')
    categories = set(posts.values_list('categories__id', flat=True))
    subscribers_emails = set(
    Category.objects.filter(category__id__in=categories).values_list('user__email', flat=True)
    )

    for subscriber_email in subscribers_emails:
        subscriptions_to_categories = Category.objects.filter(user__email=subscriber_email)
        list_subscriptions_to_categories = set(subscriptions_to_categories.values_list('category', flat=True))
        subscribed_posts = posts.filter(postcategory__category__in=list_subscriptions_to_categories).distinct()


        subject = 'Новости и статьи за прошедшую неделю по вашим подпискам'
        from_email = None
        to_email = subscriber_email

        text_content = render_to_string(
            'subscriptions/weekly_newsletter_email.txt',
            {'subscribed_posts': subscribed_posts, 'link': settings.SITE_URL}
        )
        html_content = render_to_string(
            'subscriptions/weekly_newsletter_email.html',
            {'subscribed_posts': subscribed_posts, 'link': settings.SITE_URL}
        )

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()