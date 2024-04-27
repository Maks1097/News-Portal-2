from django.urls import path
from .views import NewsList, NewDetail, NewSearch, NewCreate, NewUpdate, NewDelete, ArticleCreate, subscriptions
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('news/', cache_page(60)(NewsList.as_view()), name='new_list'),
   path('news/<int:pk>', cache_page(300)(NewDetail.as_view()), name='new_detail'),
   path('news/search/', cache_page(300)(NewSearch.as_view())),
   path('news/create/', NewCreate.as_view(), name='new_create'),
   path('news/<int:pk>/edit/', NewUpdate.as_view(), name='new_update'),
   path('news/<int:pk>/delete/', NewDelete.as_view(), name='new_delete'),
   path('articles/create/', ArticleCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/edit/', NewUpdate.as_view(), name='article_update'),
   path('articles/<int:pk>/delete/', NewDelete.as_view(), name='article_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]