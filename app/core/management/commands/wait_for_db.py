"""
management/commands/NameOfNewCommand.py
this is how we add new command to the manage.py
now we can execute the command " python manage.py wait_for_db"

"""
import time
from django.core.management.base import BaseCommand
# this is the error which django throws if the database not ready
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):

    def handle(self, *args, **options):

        self.stdout.write("Waiting for database...")
        db_up = False

        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except(OperationalError, Psycopg2OpError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))
