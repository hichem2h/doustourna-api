from django.db import models


class Article(models.Model):
    number = models.PositiveIntegerField(unique=True)
    content = models.CharField(max_length=1024)
    video_link = models.URLField(max_length=128)
    date = models.DateField()
    section = models.ForeignKey('Section', related_name='articles',
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number}'


class Section(models.Model):
    name = models.CharField(max_length=128, unique=True)
    chapter = models.ForeignKey('Chapter', related_name='sections',
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Chapter(models.Model):
    name = models.CharField(max_length=128, unique=True)
    desciption = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'
