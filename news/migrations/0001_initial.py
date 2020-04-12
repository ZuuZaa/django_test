# Generated by Django 3.0.5 on 2020-04-12 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=250)),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
