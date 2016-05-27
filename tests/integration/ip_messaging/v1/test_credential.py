# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests.integration import IntegrationTestCase
from tests.integration.holodeck import Request
from twilio import serialize
from twilio.exceptions import TwilioException
from twilio.http.response import Response


class CredentialTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.credentials.list()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://ip-messaging.twilio.com/v1/Credentials',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "credentials": [
                    {
                        "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "Test slow create",
                        "type": "apn",
                        "sandbox": "False",
                        "date_created": "2015-10-07T17:50:01Z",
                        "date_updated": "2015-10-07T17:50:01Z",
                        "url": "https://ip-messaging.twilio.com/v1/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 1,
                    "first_page_url": "https://ip-messaging.twilio.com/v1/Credentials?PageSize=1&Page=0",
                    "previous_page_url": null,
                    "url": "https://ip-messaging.twilio.com/v1/Credentials?PageSize=1&Page=0",
                    "next_page_url": null,
                    "key": "credentials"
                }
            }
            '''
        ))
        
        actual = self.client.ip_messaging.v1.credentials.list()
        
        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "credentials": [],
                "meta": {
                    "page": 0,
                    "page_size": 1,
                    "first_page_url": "https://ip-messaging.twilio.com/v1/Credentials?PageSize=1&Page=0",
                    "previous_page_url": null,
                    "url": "https://ip-messaging.twilio.com/v1/Credentials?PageSize=1&Page=0",
                    "next_page_url": null,
                    "key": "credentials"
                }
            }
            '''
        ))
        
        actual = self.client.ip_messaging.v1.credentials.list()
        
        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.credentials.create(friendly_name="friendly_name", type="gcm")
        
        values = {
            'FriendlyName': "friendly_name",
            'Type': "gcm",
        }
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://ip-messaging.twilio.com/v1/Credentials',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "Test slow create",
                "type": "apn",
                "sandbox": "False",
                "date_created": "2015-10-07T17:50:01Z",
                "date_updated": "2015-10-07T17:50:01Z",
                "url": "https://ip-messaging.twilio.com/v1/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        actual = self.client.ip_messaging.v1.credentials.create(friendly_name="friendly_name", type="gcm")
        
        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.credentials(sid="CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://ip-messaging.twilio.com/v1/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "Test slow create",
                "type": "apn",
                "sandbox": "False",
                "date_created": "2015-10-07T17:50:01Z",
                "date_updated": "2015-10-07T17:50:01Z",
                "url": "https://ip-messaging.twilio.com/v1/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        actual = self.client.ip_messaging.v1.credentials(sid="CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.credentials(sid="CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update(friendly_name="friendly_name", type="gcm")
        
        values = {
            'FriendlyName': "friendly_name",
            'Type': "gcm",
        }
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://ip-messaging.twilio.com/v1/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "Test slow create",
                "type": "apn",
                "sandbox": "False",
                "date_created": "2015-10-07T17:50:01Z",
                "date_updated": "2015-10-07T17:50:01Z",
                "url": "https://ip-messaging.twilio.com/v1/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        actual = self.client.ip_messaging.v1.credentials(sid="CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update(friendly_name="friendly_name", type="gcm")
        
        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.credentials(sid="CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://ip-messaging.twilio.com/v1/Credentials/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))
        
        actual = self.client.ip_messaging.v1.credentials(sid="CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.assertTrue(actual)
