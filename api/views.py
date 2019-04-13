from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from .serializers import ChapterSerializer, ArticleDetailsSerializer
from .models import Chapter, Article


class ListChaptersView(ListAPIView):
    methods = ('GET')
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class ArticleDetailsView(RetrieveAPIView):
    methods = ('GET')
    serializer_class = ArticleDetailsSerializer

    def get_object(self):
        number = self.kwargs.get('number')
        article = get_object_or_404(Article, number=number)
        return article
