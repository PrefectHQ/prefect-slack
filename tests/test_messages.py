from itertools import product

import pytest
from prefect import flow

from prefect_slack.messages import send_chat_message

CHANNELS = ["#random", "#general"]
TEXT = ["hello", "goodbye"]
ATTACHMENTS = [None]
SLACK_BLOCKS = [None]

@pytest.mark.parametrize(["channel", "text", "attachments", "slack_blocks"], product(CHANNELS, TEXT, ATTACHMENTS, SLACK_BLOCKS))
async def test_send_chat_message(slack_credentials, channel, text, attachments, slack_blocks):
    @flow
    async def test_flow():
        await send_chat_message(
            slack_credentials=slack_credentials, text=text, channel=channel, attachments=attachments, slack_blocks=slack_blocks
        )

    await test_flow()
    slack_credentials.get_slack_web_client().chat_postMessage.assert_called_with(
        text=text, channel=channel, blocks=slack_blocks, attachments=attachments
    )
