from rest_framework import serializers
from .models import Chapter, Section, Article


class ArticleDetailsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    videoLink = serializers.CharField(source='video_link')
    section = serializers.CharField(source='section.name')
    chapter = serializers.CharField(source='section.chapter.name')

    def get_name(self, obj):
        return f'المادة رقم {obj.number}'

    class Meta:
        model = Article
        fields = ('name', 'videoLink', 'content', 'date', 'chapter', 'section')


class ArticleSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return f'المادة {obj.number}'

    class Meta:
        model = Article
        fields = ('number', 'name', 'content')


class SectionSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)

    class Meta:
        model = Section
        fields = ('name', 'articles')


class ChapterSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)

    class Meta:
        model = Chapter
        fields = ('name', 'desciption', 'sections')
