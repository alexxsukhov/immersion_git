from django.core.management import BaseCommand
from blogapp.models import Article


class Command(BaseCommand):
    help = 'Get ALL posts in articles'

    def handle(self, *args, **options):
        posts = Article.objects.all()
        self.stdout.write(f'{posts}')
