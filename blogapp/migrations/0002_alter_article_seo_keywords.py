# Generated by Django 4.2.5 on 2023-09-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Seo Keywords',
            field=models.CharField(max_length=100),
        ),
    ]
