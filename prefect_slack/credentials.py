from dataclasses import dataclass

from slack_sdk.web.async_client import AsyncWebClient


@dataclass
class SlackCredentials:
    token: str

    def get_slack_web_client(self) -> AsyncWebClient:
        return AsyncWebClient(token=self.token)
