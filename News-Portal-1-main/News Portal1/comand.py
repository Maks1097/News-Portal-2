from news.models import *


u1 = User.objects.create_user(username='Пётр')
u2 = User.objects.create_user(username='Василий')


Author.objects.create(authorUser=u1)
Author.objects.create(authorUser=u2)


Category.objects.create(name='IT')
Category.objects.create(name='Спорт')
Category.objects.create(name='Политика')
Category.objects.create(name='Культура')


author = Author.objects.get(id=1)
Post.objects.create(author=author, categoryType='NW', title='sometitle', text='sometext')
Post.objects.create(author=author, categoryType='AR', title='Someitle', text='Sometext')
Post.objects.create(author=author, categoryType='AR', title='SomeTitle', text='SomeText')


Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=4))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=2))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=3))


Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='anytextbyauthor')
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).authorUser, text='anytextbyauthor')
Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=1).authorUser, text='anytextbyauthor')
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=2).authorUser, text='anytextbyauthor')
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='anytextbyauthor')


Comment.objects.get(id=1).dislike()
Post.objects.get(id=1).dislike()

Comment.objects.get(id=2).like()
Post.objects.get(id=2).like()

Comment.objects.get(id=3).like()
Post.objects.get(id=3).like()


Author.objects.get(id=1)
a = Author.objects.get(id=1)
a.update_rating()
a.ratingAuthor

Author.objects.get(id=2)
b = Author.objects.get(id=2)
b.update_rating()
b.ratingAuthor


a = Author.objects.order_by('-ratingAuthor')[:1]
for i in a:
    i.ratingAuthor
    i.authorUser.username


post = Post.objects.order_by('-rating')[:1].values('author__authorUser__username', 'rating', 'title', 'dateCreate')
Post.objects.order_by('-rating')[0].preview()


Comment.objects.all().values('commentCreate', 'commentUser', 'rating', 'text')