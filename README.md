# prefect-slack

<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-slack/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-slack?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/PrefectHQ/prefect-slack/" alt="Stars">
        <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-slack?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-slack/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-slack?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/PrefectHQ/prefect-slack/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-slack?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>

## Welcome!

`prefect-slack` is a collection of prebuilt Prefect tasks that can be used to quickly construct Prefect flows.

## Getting Started

### Python setup

Requires an installation of Python 3.7+

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-slack`

```bash
pip install prefect-slack
```

Then, register to [view the block](https://orion-docs.prefect.io/ui/blocks/) on Prefect Cloud:

```bash
prefect block register -m prefect_slack
```

Note, to use the `load` method on Blocks, you must already have a block document [saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).

### Slack setup

In order to use tasks in the collection, you'll first need to create an Slack app and install it in your Slack workspace. You can create a Slack app by navigating to the [apps page](https://api.slack.com/apps) for your Slack account and selecting 'Create New App'.

For tasks that require a Bot user OAuth token, you can get a token for your app by navigating to your apps __OAuth & Permissions__ page.

For tasks that require and Webhook URL, you get generate new Webhook URLs by navigating to you apps __Incoming Webhooks__ page.

Slack's [Basic app setup](https://api.slack.com/authentication/basics) guide provides additional details on setting up a Slack app.

### Write and run a flow

```python
from prefect import flow
from prefect.context import get_run_context
from prefect_slack import SlackCredentials
from prefect_slack.messages import send_chat_message


@flow
def example_send_message_flow():
   context = get_run_context()

   # Run other tasks and subflows here

   token = "xoxb-your-bot-token-here"
   send_chat_message(
         slack_credentials=SlackCredentials(token),
         channel="#prefect",
         text=f"Flow run {context.flow_run.name} completed :tada:"
   )

example_send_message_flow()
```

### Use `with_options` to customize options on any existing task or flow:

```python
from prefect import flow
from prefect.context import get_run_context
from prefect_slack import SlackCredentials
from prefect_slack.messages import send_chat_message

custom_send_chat_message = send_chat_message.with_options(
    name="My custom task name",
    retries=2,
    retry_delay_seconds=10,
)
 
 @flow
 def example_wiht_options_flow():

   slack_credentials = SlackCredentials.load("my_slack_token")
   custom_send_chat_message(
         slack_credentials=slack_credentials,
         channel="#prefect",
         text=f"Flow run {context.flow_run.name} completed :tada:"
   )
 
 example_wiht_options_flow()
 ```
 
For more tips on how to use tasks and flows in a Collection, check out [Using Collections](https://orion-docs.prefect.io/collections/usage/)!

## Resources

If you encounter any bugs while using `prefect-slack`, feel free to open an issue in the [prefect-slack](https://github.com/PrefectHQ/prefect-slack) repository.

If you have any questions or issues while using `prefect-slack`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack)

Feel free to ⭐️ or watch [`prefect-slack`](https://github.com/PrefectHQ/prefect-slack) for updates too!

## Development

If you'd like to install a version of `prefect-slack` for development, first clone the repository and then perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-slack.git

cd prefect-slack/

pip install -e ".[dev]"
```
