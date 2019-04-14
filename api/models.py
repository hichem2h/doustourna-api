from django.db import models
from translated_fields import TranslatedField


class Article(models.Model):
    number = models.PositiveIntegerField(unique=True)
    content = TranslatedField(
        models.CharField(max_length=1024)
    )
    video_link = models.URLField(max_length=128)
    description = TranslatedField(
        models.CharField(max_length=256)
    )
    date = models.DateField()
    section = models.ForeignKey('Section', related_name='articles',
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number}'

    class Meta:
        ordering = ['number']


class Section(models.Model):
    number = models.PositiveIntegerField()
    name = TranslatedField(
        models.CharField(max_length=128)
    )
    chapter = models.ForeignKey('Chapter', related_name='sections',
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['number']


class Chapter(models.Model):
    number = models.PositiveIntegerField()
    name = TranslatedField(
        models.CharField(max_length=128)
    )
    description = TranslatedField(
        models.CharField(max_length=256)
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['number']


class Question(models.Model):
    email = models.EmailField(max_length=128)
    name = models.CharField(max_length=256)
    profession = models.CharField(max_length=256)
    question = models.CharField(max_length=1024)
    answer = models.CharField(max_length=1024, blank=True)

    def __str__(self):
        return f'{self.name}'
