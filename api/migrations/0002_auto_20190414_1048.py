# Generated by Django 2.2 on 2019-04-14 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128)),
                ('name', models.CharField(max_length=256)),
                ('profession', models.CharField(max_length=256)),
                ('question', models.CharField(max_length=1024)),
                ('answer', models.CharField(blank=True, max_length=1024)),
            ],
        ),
        migrations.RenameField(
            model_name='chapter',
            old_name='desciption',
            new_name='description',
        ),
    ]