import unittest
import os
from printapp.printstatus import *

class TestPrintQueue(unittest.TestCase):

    def setUp(self):
        self.username = os.getenv('UNIFLOW_USER')
        self.password = os.getenv('UNIFLOW_PASSWORD')
        self.assertNotEqual(None, self.username)
        self.assertNotEqual(None, self.password)

    def test_budget(self):
        uc = get_uniflow_client(self.username, self.password)
        budget = uc.get_budget()
        self.assertIsInstance(budget, float)
        budget = uc.get_budget()
        self.assertIsInstance(budget, float)

    def test_queue(self):
        uc = get_uniflow_client(self.username, self.password)
        uc.get_print_queue()
        uc.get_print_queue()

    def test_invalid_credentials(self):
        self.assertRaises(InvalidCredentialsError, get_uniflow_client,
                          'invalidUser', 'invalidPassword')

    def test_blank_credentials(self):
        self.assertRaises(InvalidCredentialsError, get_uniflow_client,
                          '', '')
        self.assertRaises(InvalidCredentialsError, get_uniflow_client,
                          'invalidUser', '')
        self.assertRaises(InvalidCredentialsError, get_uniflow_client,
                          '', 'invalidPassword')
    def test_is_username_and_password_valid(self):
        self.invalid_username = "lil0"
        self.invalid_password = "password"

        #good username, good password
        self.assertTrue(is_username_and_password_valid(self.username, self.password))
        #good username, bad password
        self.assertFalse(is_username_and_password_valid(self.username, self.invalid_password))
        #bad username, good password
        #self.assertFalse(is_username_and_password_valid(self.invalid_username, self.password))
        #bad username, bad password
        self.assertFalse(is_username_and_password_valid(self.invalid_username, self.invalid_password))
