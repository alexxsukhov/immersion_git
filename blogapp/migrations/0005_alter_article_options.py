# Generated by Django 4.2.5 on 2023-09-21 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_remove_article_seo_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]