from django.urls import path
from .views import ArticleDetailsView, ListChaptersView


urlpatterns = [
    path('chapters/', ListChaptersView.as_view(), name='list_chapters'),
    path('articles/<number>', ArticleDetailsView.as_view(), name='article_details'),
]
