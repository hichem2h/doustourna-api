from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     ListCreateAPIView, get_object_or_404)
from .serializers import (ChapterSerializer, ArticleDetailsSerializer,
                          QuestionSerializer)
from .models import Chapter, Article, Question


class ListChaptersView(ListAPIView):
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class ArticleDetailsView(RetrieveAPIView):
    serializer_class = ArticleDetailsSerializer

    def get_object(self):
        number = self.kwargs.get('number')
        article = get_object_or_404(Article, number=number)
        return article


class QuestionView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.exclude(answer='')
