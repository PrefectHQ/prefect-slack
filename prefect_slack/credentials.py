from dataclasses import dataclass

from slack_sdk.web.async_client import AsyncWebClient


@dataclass
class SlackCredentials:
    """
    Class for holding Slack credentials for use in tasks and flows.

    Args:
        token: Bot user OAuth token for the Slack app used to perform actions.
    """

    token: str

    def get_slack_web_client(self) -> AsyncWebClient:
        """
        Returns an authenticated `AsyncWebClient` to interact with the Slack API.
        """
        return AsyncWebClient(token=self.token)
