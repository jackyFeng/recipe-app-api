from unittest.mock import patch

from django.core.management import call_command
# django throws when the db is unavaiable
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):
    def test_wait_for_db_ready(self):
        """ Test waiting for db when db is available """
        # use patch to mock the behaviour of the function
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            # matched with core/management/commands/wait_for_db.py
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """ Test waiting for db """
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # raise error for first 5 times of calling getitem and not on 6th
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
