
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management import call_command
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):

    def test_wait_for_db_ready(self, mocked_check):

        mocked_check.return_value = True

        call_command("wait_for_db")

        mocked_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError."""
        patched_check.side_effect = [OperationalError] + \
                                    [Psycopg2OpError] + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 3)
        patched_check.assert_called_with(databases=['default'])
