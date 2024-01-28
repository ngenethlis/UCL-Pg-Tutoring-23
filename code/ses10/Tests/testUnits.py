# testing transaction.py
from transaction import Transaction
from client import Client
import unittest


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction("Nic", "Ben", 100)

    def tearDown(self):
        self.transaction = None

    def test_getSender(self):
        self.assertEqual(self.transaction.getSender(), "Nic")

    def test_getReceiver(self):
        self.assertEqual(self.transaction.getReceiver(), "Ben")

    def test_getAmount(self):
        self.assertEqual(self.transaction.getAmount(), 100)


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client("Nic", "WC1H", "9696420")

    def tearDown(self):
        self.client = None

    def test_getName(self):
        self.assertEqual(self.client.getName(), "Nic")

    def test_getAddress(self):
        self.assertEqual(self.client.getAddress(), "WC1H")

    def test_getPhone(self):
        self.assertEqual(self.client.getPhone(), "9696420")

    def test_getBalance(self):
        self.assertEqual(self.client.getBalance(), 0)

    def test_getTransactions(self):
        self.assertEqual(self.client.getTransactions(), [])

    def test_addTransaction_checkBalance(self):
        t = Transaction("Nic", "Ben", 100)
        self.client.addTransaction(t)
        self.assertEqual(self.client.getBalance(), 100)
        self.assertEqual(self.client.getTransactions(), [t])

