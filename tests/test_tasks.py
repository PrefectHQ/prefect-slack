from prefect import flow

from prefect_slack.tasks import (
    goodbye_prefect_slack,
    hello_prefect_slack,
)


def test_hello_prefect_slack():
    @flow
    def test_flow():
        return hello_prefect_slack()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Hello, prefect-slack!"


def goodbye_hello_prefect_slack():
    @flow
    def test_flow():
        return goodbye_prefect_slack()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Goodbye, prefect-slack!"
