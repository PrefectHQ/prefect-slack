# prefect-slack

## Welcome!

`prefect-slack` is a collections of prebuilt Prefect tasks that can be used to quickly construct Prefect flows.

## Getting Started

### Python setup

Requires an installation of Python 3.7+

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect` and `prefect-slack`

```bash
pip install "prefect>=2.0a9" prefect-slack
```

### Write and run a flow

```python
import asyncio

from prefect import flow
from prefect.context import get_run_context
from prefect_slack import SlackCredentials
from prefect_slack.messages import send_chat_message

@flow
async def example_flow():
    context = get_run_context()

    # Run other tasks and subflows here

    await send_chat_message(
        slack_credentials=SlackCredentials("xoxb-your-bot-token-here"),
        channel="#prefect",
        text=f"Flow run {context.flow_run.name} completed :tada:"
    )

asyncio.run(example_flow())
```

## Development

If you'd like to install a version of `prefect-slack` for development, first clone the repository and then perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-slack.git

cd prefect-slack/

pip install -e ".[dev]"
```
