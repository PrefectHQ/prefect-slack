from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.webhook.async_client import AsyncWebhookClient

from prefect_slack import SlackCredentials, SlackWebhook


def test_slack_credentials():
    assert isinstance(SlackCredentials(token="xoxb-xxxx").get_client(), AsyncWebClient)


def test_slack_webhook():
    assert isinstance(
        SlackWebhook(url="https://hooks.slack.com/xxxx").get_client(),
        AsyncWebhookClient,
    )
