# Generated by Django 4.2.5 on 2023-09-25 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(default='', unique=True, verbose_name='Символьный код')),
                ('image', models.ImageField(blank=True, default='', upload_to='static/images/products/')),
                ('h1', models.CharField(blank=True, default='', max_length=150, verbose_name='Заголовок H1')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('announce', models.TextField(blank=True, default='', max_length=500, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, default='', verbose_name='Описание')),
                ('seo_title', models.CharField(blank=True, default='', max_length=150, verbose_name='Seo Title')),
                ('seo_description', models.TextField(blank=True, default='', max_length=500, verbose_name='Seo Description')),
                ('seo_keywords', models.CharField(blank=True, default='', max_length=100, verbose_name='Seo Keywords')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='shopapp.category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
