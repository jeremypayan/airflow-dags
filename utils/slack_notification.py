from airflow.hooks.base_hook import BaseHook
import requests
from log_config import LOGGER
import json


SLACK_CONN_ID = "slack_airflow"


def task_fail_slack_alert(context):
    slack_msg = """
            :red_circle: Task Failed.
            *Task*: {task}
            *Dag*: {dag}
            *Execution Time*: {exec_date}
            *Log Url*: {log_url}
            """.format(
        task=context.get("task_instance").task_id,
        dag=context.get("task_instance").dag_id,
        # ti=context.get("task_instance"),
        exec_date=context.get("execution_date"),
        log_url=context.get("task_instance").log_url,
    )
    send_slack_message(slack_msg, "#airflow_monitoring")


def daily_extract_success_alert(context):
    slack_msg = """
            :tada: The daily extract to GCS Suceeded.
            *Dag*: {dag},
            *Task*: {task},
            *Execution Time*: {exec_date}
            """.format(
        task=context.get("task_instance").task_id,
        dag=context.get("task_instance").dag_id,
        # ti=context.get("task_instance"),
        exec_date=context.get("execution_date"),
    )
    send_slack_message(slack_msg, "#airflow_monitoring")


def send_slack_message(msg, channel):
    slack_conn = BaseHook.get_connection(SLACK_CONN_ID)
    message = {"text": msg, "channel": channel}
    auth = {"Authorization": f"Bearer {slack_conn.get_password()}"}
    requests.post(slack_conn.host, params=message, headers=auth)


def send_message(message: str, url: str):
    """
    Send the message to the url
    """

    message = {"text": message}
    r = requests.post(
        url=url,
        data=json.dumps(message),
        headers={'Content-Type': 'application/json'}
    )
    if r.status_code != 200:
        LOGGER.error(f"Request to slack return an error : {r.status_code} - {r.text}, url: {url}")
        return
    else:
        LOGGER.info("The message has been sent to the slackbot !")
        return "200"
