from unittest.mock import MagicMock

import pytest
from prefect.utilities.testing import AsyncMock


@pytest.fixture
def slack_credentials():
    slack_credentials_mock = MagicMock()
    slack_credentials_mock.get_slack_web_client.return_value = AsyncMock(
        chat_postMessage=MagicMock(data=dict())
    )
    return slack_credentials_mock
