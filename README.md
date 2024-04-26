> [!NOTE]
> Active development of this project has moved within PrefectHQ/prefect. The code can be found [here](https://github.com/PrefectHQ/prefect/tree/main/src/integrations/prefect-slack) and documentation [here](https://docs.prefect.io/latest/integrations/prefect-slack).
> Please open issues and PRs against PrefectHQ/prefect instead of this repository.

# `prefect-slack`

<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-slack/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-slack?color=26272B&labelColor=090422"></a>
    <a href="https://github.com/PrefectHQ/prefect-slack/" alt="Stars">
        <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-slack?color=26272B&labelColor=090422"2" /></a>
    <a href="https://pepy.tech/badge/prefect-slack/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-slack?color=26272B&labelColor=090422"" /></a>
    <a href="https://github.com/PrefectHQ/prefect-slack/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-slack?color=26272B&labelColor=090422"2" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=26272B&labelColor=090422"&logo=slack" /></a>
</p>

Visit the full docs [here](https://PrefectHQ.github.io/prefect-slack) to see additional examples and the API reference.

`prefect-slack` is a collection of prebuilt Prefect integrations that can be used to interact with Slack.

## Getting Started

### Saving credentials to block

In order to use tasks in the collection, you'll first need to create a Slack app and install it in your Slack workspace.

You can create a Slack app by navigating to the [apps page](https://api.slack.com/apps) for your Slack account and selecting **Create New App**.

Slack's [Basic app setup](https://api.slack.com/authentication/basics) guide provides additional details on setting up a Slack app.

=== "Webhook"

    For integrations that require a Webhook URL, you can generate new Webhook URLs by navigating to your app's __Incoming Webhooks__ page.

    Click __Add New Webhook to Workspace__ and copy the webhook URL, formatted like `https://hooks.slack.com/services/...`.

    Then, create and run a short script, replacing the placeholders.

    ```python
    from prefect_slack import SlackWebhook

    SlackWebhook(url="WEBHOOK_URL_PLACEHOLDER").save("BLOCK-NAME-PLACEHOLDER")
    ```

    Congrats! You can now easily load the saved block, which holds your credentials:

    ```python
    from prefect_slack import SlackWebhook

    SlackWebhook.load("BLOCK-NAME-PLACEHOLDER")
    ```

=== "OAuth"

    For integrations that require a Bot user OAuth token, you can get a token for your app by navigating to your app's __OAuth & Permissions__ page.

    Locate __Bot User OAuth Token__ and copy the token, formatted like `xoxb-...`.

    Then, create and run a short script, replacing placeholders.

    ```python
    from prefect_slack import SlackCredentials

    SlackCredentials(token="TOKEN-PLACEHOLDER").save("BLOCK-NAME-PLACEHOLDER")
    ```

    Next, update the scope to include `chat:write`, which will prompt you to reinstall the app.

    Congrats! You can now easily load the saved block, which holds your credentials:

    ```python
    from prefect_slack import SlackCredentials

    SlackCredentials.load("BLOCK-NAME-PLACEHOLDER")
    ```

!!! info "Unsure whether to authenticate with Webhook or OAuth?"

    Webhook requires slightly less configuration and is limited to a single channel, which makes it suitable for getting started.

### Integrate with Prefect flows

`prefect-slack` makes sending Slack messages effortless, giving you peace of mind that your messages are being sent as expected.

First, install [prefect-slack](#installation) and [save your Slack credentials to a block](#saving-credentials-to-block) to run the examples below!

=== "Webhook"

    ```python
    from prefect import flow
    from prefect_slack import SlackWebhook
    from prefect_slack.messages import send_incoming_webhook_message

    @flow
    def example_slack_send_message_flow():
        slack_webhook = SlackWebhook.load("BLOCK-NAME-PLACEHOLDER")
        result = send_incoming_webhook_message(
            slack_webhook=slack_webhook,
            text="This proves send_incoming_webhook_message works!",
        )
        return result

    example_slack_send_message_flow()
    ```

    Outputs:
    ```bash
    16:30:47.101 | INFO    | prefect.engine - Created flow run 'scrupulous-avocet' for flow 'example-slack-send-message-flow'
    16:30:48.389 | INFO    | Flow run 'scrupulous-avocet' - Created task run 'send_incoming_webhook_message-a90deb5e-0' for task 'send_incoming_webhook_message'
    16:30:48.391 | INFO    | Flow run 'scrupulous-avocet' - Executing 'send_incoming_webhook_message-a90deb5e-0' immediately...
    16:30:48.861 | INFO    | Task run 'send_incoming_webhook_message-a90deb5e-0' - Posting message to provided webhook
    16:30:49.390 | INFO    | Task run 'send_incoming_webhook_message-a90deb5e-0' - Finished in state Completed()
    16:30:49.571 | INFO    | Flow run 'scrupulous-avocet' - Finished in state Completed('All states completed.')
    ```

=== "OAuth"

    ```python
    from prefect import flow
    from prefect_slack import SlackCredentials
    from prefect_slack.messages import send_chat_message

    @flow
    def example_slack_send_message_flow():
        slack_credentials = SlackCredentials.load("BLOCK-NAME-PLACEHOLDER")
        result = send_chat_message(
            slack_credentials=slack_credentials,
            text="This proves send_chat_message works!",
            channel="CHANNEL-NAME-PLACEHOLDER",
        )
        return result

    example_slack_send_message_flow()
    ```

    Outputs:

    ```bash
    16:28:04.294 | INFO    | prefect.engine - Created flow run 'resourceful-koala' for flow 'example-slack-send-message-flow'
    16:28:05.675 | INFO    | Flow run 'resourceful-koala' - Created task run 'send_chat_message-0403e84a-0' for task 'send_chat_message'
    16:28:05.678 | INFO    | Flow run 'resourceful-koala' - Executing 'send_chat_message-0403e84a-0' immediately...
    16:28:06.160 | INFO    | Task run 'send_chat_message-0403e84a-0' - Posting chat message to testing-slack
    16:28:06.674 | INFO    | Task run 'send_chat_message-0403e84a-0' - Finished in state Completed()
    16:28:06.848 | INFO    | Flow run 'resourceful-koala' - Finished in state Completed()
    ```

### Capture exceptions and notify by Slack message

Perhaps you want a Slack notification with the details of the exception when your flow run fails.

`prefect-slack` can be wrapped in an `except` statement to do just that!

```python
from prefect import flow
from prefect.context import get_run_context
from prefect_slack import SlackWebhook

def notify_exc_by_slack(exc):
    context = get_run_context()
    flow_run_name = context.flow_run.name
    slack_webhook = SlackWebhook.load("BLOCK-NAME-PLACEHOLDER")
    slack_webhook.notify(body=f"Flow run {flow_run_name!r} failed due to {exc}.")

@flow
def example_flow():
    try:
        1 / 0
    except Exception as exc:
        notify_exc_by_slack(exc)
        raise

example_flow()
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
