"""Credential classes used to perform authenticated interacting with Slack"""

from typing import Optional

from prefect.blocks.core import Block
from prefect.utilities.asyncutils import sync_compatible
from pydantic import Field, SecretStr
from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.webhook.async_client import AsyncWebhookClient


class SlackCredentials(Block):
    """
    Block holding Slack credentials for use in tasks and flows.

    Args:
        token: Bot user OAuth token for the Slack app used to perform actions.

    Example:
        Load stored Slack credentials:
        ```python
        from prefect_slack import SlackCredentials
        slack_credentials_block = SlackCredentials.load("BLOCK_NAME")
        ```
    """  # noqa E501

    _block_type_name = "Slack Credentials"
    _logo_url = "https://images.ctfassets.net/gm98wzqotmnx/7dkzINU9r6j44giEFuHuUC/85d4cd321ad60c1b1e898bc3fbd28580/5cb480cd5f1b6d3fbadece79.png?h=250"  # noqa

    token: SecretStr

    def get_client(self) -> AsyncWebClient:
        """
        Returns an authenticated `AsyncWebClient` to interact with the Slack API.
        """
        return AsyncWebClient(token=self.token.get_secret_value())


class SlackWebhook(Block):
    """
    Block holding a Slack webhook for use in tasks and flows.

    Args:
        url: Slack webhook URL which can be used to send messages
            (e.g. `https://hooks.slack.com/XXX`).

    Example:
        Load stored Slack webhook:
        ```python
        from prefect_slack import SlackWebhook
        slack_webhook_block = SlackWebhook.load("MY_BLOCK_NAME")
        ```
    """

    _block_type_name = "Slack Webhook"
    _logo_url = "https://images.ctfassets.net/gm98wzqotmnx/7dkzINU9r6j44giEFuHuUC/85d4cd321ad60c1b1e898bc3fbd28580/5cb480cd5f1b6d3fbadece79.png?h=250"  # noqa

    url: SecretStr = Field(..., title="Webhook URL")

    def get_client(self) -> AsyncWebhookClient:
        """
        Returns and authenticated `AsyncWebhookClient` to interact with the configured
        Slack webhook.
        """
        return AsyncWebhookClient(url=self.url.get_secret_value())

    @sync_compatible
    async def notify(self, body: str, subject: Optional[str] = None):
        """
        Sends a message to the Slack channel.
        """
        client = self.get_client()
        await client.send(text=body)
