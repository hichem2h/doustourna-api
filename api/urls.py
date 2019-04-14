from django.urls import path
from .views import ArticleDetailsView, ListChaptersView, QuestionView


urlpatterns = [
    path('chapters/', ListChaptersView.as_view(), name='list_chapters'),
    path('articles/<number>', ArticleDetailsView.as_view(), name='article_details'),
    path('questions/', QuestionView.as_view(), name='questions'),
]
