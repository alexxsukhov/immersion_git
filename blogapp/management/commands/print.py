from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Print test'

    def handle(self, *args, **options):
        self.stdout.write(f'All right')
