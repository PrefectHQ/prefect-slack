# Reliably send Slack messages with prefect-slack

<p align="center">
    <!--- Insert a cover image here -->
    <!--- <br> -->
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

Visit the full docs [here](https://PrefectHQ.github.io/prefect-slack) to see additional examples and the API reference.

`prefect-slack` is a collection of prebuilt Prefect integrations that can be used to interact with email services.

## Getting Started

### Slack setup

In order to use tasks in the collection, you'll first need to create a Slack app and install it in your Slack workspace.

You can create a Slack app by navigating to the [apps page](https://api.slack.com/apps) for your Slack account and selecting **Create New App**.

For tasks that require a Bot user OAuth token, you can get a token for your app by navigating to your app's __OAuth & Permissions__ page.

For tasks that require a Webhook URL, you can generate new Webhook URLs by navigating to your app's __Incoming Webhooks__ page.

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
         slack_credentials=SlackCredentials(token=token),
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
def example_with_options_flow():

    slack_credentials = SlackCredentials.load("my_slack_token")
    custom_send_chat_message(
            slack_credentials=slack_credentials,
            channel="#prefect",
            text=f"Flow run {context.flow_run.name} completed :tada:"
    )

example_with_options_flow()
```
 
## Resources

For more tips on how to use tasks and flows in a Collection, check out [Using Collections](https://docs.prefect.io/collections/usage/)!

### Installation

Install `prefect-slack`:

```bash
pip install prefect-slack
```

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2. For more information about how to use Prefect, please refer to the [Prefect documentation](https://docs.prefect.io/).

### Feedback

If you encounter any bugs while using `prefect-slack`, feel free to open an issue in the [prefect-slack](https://github.com/PrefectHQ/prefect-slack) repository.

If you have any questions or issues while using `prefect-slack`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to star or watch [`prefect-slack`](https://github.com/PrefectHQ/prefect-slack) for updates too!

### Contributing

If you'd like to help contribute to fix an issue or add a feature to `prefect-slack`, please [propose changes through a pull request from a fork of the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).
 
Here are the steps:
 
1. [Fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository)
2. [Clone the forked repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository)
3. Install the repository and its dependencies:
```
pip install -e ".[dev]"
```
4. Make desired changes
5. Add tests
6. Insert an entry to [CHANGELOG.md](https://github.com/PrefectHQ/prefect-slack/blob/main/CHANGELOG.md)
7. Install `pre-commit` to perform quality checks prior to commit:
```
pre-commit install
```
8. `git commit`, `git push`, and create a pull request

## Development

If you'd like to install a version of `prefect-slack` for development, first clone the repository and then perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-slack.git

cd prefect-slack/

pip install -e ".[dev]"
```
