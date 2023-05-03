from django.core.management import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "create moderator permission"

    def handle(self, *args, **options):
        moderator_group, created = Group.objects.get_or_create(name="Moderator")
        if created:
            print("Successfully created Moderators")
