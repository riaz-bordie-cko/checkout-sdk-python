import checkout_sdk as sdk
from checkout_sdk import HTTPClient
from checkout_sdk.payments import PaymentsClient
from tests.base import CheckoutSdkTestCase


class CheckoutApiTests(CheckoutSdkTestCase):

    def test_init_checkout_api(self):
        api = sdk.get_api()

        self.assertTrue(isinstance(api.payments, PaymentsClient))
        self.assertTrue(isinstance(api.payments._http_client, HTTPClient))
