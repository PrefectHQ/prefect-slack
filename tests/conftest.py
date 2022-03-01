import sys
from unittest.mock import MagicMock

import pytest

if sys.version_info < (3, 8):
    # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock
    from mock import AsyncMock
else:
    from unittest.mock import AsyncMock


@pytest.fixture
def slack_credentials():
    slack_credentials_mock = MagicMock()
    slack_credentials_mock.get_slack_web_client.return_value = AsyncMock(
        chat_postMessage=MagicMock(data=dict())
    )
    return slack_credentials_mock
