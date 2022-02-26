from typing import Dict, Optional, Sequence, Union

from prefect import task
from slack_sdk.models.attachments import Attachment
from slack_sdk.models.blocks import Block as SlackBlock

from prefect_slack.credentials import SlackCredentials

from slack_sdk.web.async_slack_response import AsyncSlackResponse


@task
async def send_chat_message(
    channel: str,
    slack_credentials: SlackCredentials,
    text: Optional[str] = None,
    attachments: Optional[Sequence[Union[Dict, Attachment]]] = None,
    slack_blocks: Optional[Sequence[Union[Dict, SlackBlock]]] = None,
) -> AsyncSlackResponse:
    client = slack_credentials.get_slack_web_client()

    return await client.chat_postMessage(
        channel=channel, text=text, blocks=slack_blocks, attachments=attachments
    )


@task
async def send_incoming_webhook_message():
    raise NotImplementedError()
