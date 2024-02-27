from django_filters import FilterSet, ModelChoiceFilter, DateFilter, CharFilter
from .models import New, Category
from django import forms


class NewFilter(FilterSet):

    category = ModelChoiceFilter(
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Выберите категорию')

    pupdate_gt = DateFilter(
        field_name='time_now',
        lookup_expr='gt',
        label='Позже даты',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    name = CharFilter(
        label='Поиск по заголовку',
        lookup_expr='icontains'
    )

    class Meta:
        model = New
        fields = [
           'name',
            'category',
            'pupdate_gt',
        ]