from prefect import flow

from prefect_slack.tasks import (
    goodbye_prefect_slack,
    hello_prefect_slack,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    print(hello_prefect_slack)
    print(goodbye_prefect_slack)
