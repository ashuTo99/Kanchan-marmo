from django.test import TestCase
from .query import Twillio

class TwilliTestCase(TestCase):

    def test_invalid_phone(self):
        obj = Twillio
        response = obj.sendOtp(self,"9660222632",code="+91")
        self.assertNotEqual(response.status_code,400)

    def test_valid_phone(self):
        obj = Twillio
        response = obj.sendOtp(self,"9660222632",code="+91")
        self.assertEqual(response.status_code,200)

