from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from .models import Chapter, Section, Article, Question


class ArticleDetailsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    videoLink = serializers.CharField(source='video_link')
    section = serializers.CharField(source='section.name')
    chapter = serializers.CharField(source='section.chapter.name')

    def get_name(self, obj):
        return _('المادة رقم {}').format(obj.number)

    class Meta:
        model = Article
        fields = ('number', 'name', 'videoLink', 'content', 'date',
                  'chapter', 'section', 'description')


class ArticleSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return _('المادة رقم {}').format(obj.number)

    class Meta:
        model = Article
        fields = ('number', 'name', 'content', 'date')


class SectionSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)

    class Meta:
        model = Section
        fields = ('name', 'articles')


class ChapterSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)

    class Meta:
        model = Chapter
        fields = ('name', 'description', 'sections')


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('email', 'name', 'profession', 'question', 'answer')
        read_only_fields = ('answer', )
