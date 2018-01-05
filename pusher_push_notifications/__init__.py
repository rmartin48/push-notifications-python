"""Pusher Push Notifications Python server SDK"""

import requests
import six

SDK_VERSION = '0.9.0'


class PushNotifications(object):
    """Pusher Push Notifications API client
    This client class can be used to publish notifications to the Pusher
    Push Notifications service"""

    def __init__(self, instance_id, secret_key, endpoint=None):
        if not isinstance(instance_id, six.string_types):
            raise TypeError('instance_id must be a string')
        if not isinstance(secret_key, six.string_types):
            raise TypeError('secret_key must be a string')
        if (endpoint is not None
                and not isinstance(endpoint, six.string_types)):
            raise TypeError('endpoint must be a string')

        self.instance_id = instance_id
        self.secret_key = secret_key
        self._endpoint = endpoint

    @property
    def endpoint(self):
        """Property method to calculate the correct Pusher API host"""
        default_endpoint = '{}.pushnotifications.pusher.com'.format(
            self.instance_id,
        )
        return self._endpoint or default_endpoint

    def publish(self, publish_body):
        requests.post(
            'https://{}/publish_api/v1/instances/{}/publishes'.format(
                self.endpoint,
                self.instance_id,
            ),
            json=publish_body,
            headers={
                'authorization': 'Bearer {}'.format(self.secret_key),
                'x-pusher-library': 'pusher-push-notifications-python {}'.format(
                    SDK_VERSION,
                )
            },
        )