import json
import subprocess
import urllib3
from time import sleep


def holidata_events_jsonl(url='https://holidata.net/pl-PL/2021.json'):
    with urllib3.PoolManager().request(
        'GET',
        url,
        preload_content=False
    ) as response:
        return response.data.decode('utf-8')


def jsonl_to_json(jsonl_content):
    """
    params:
    jsonl_content: dicts separated with newlines

    returns:
    list of dicts (json)
    """
    return [json.loads(jline) for jline in jsonl_content.splitlines()]


def prep_events(event_list):
    """
    Strip unused fields out of holidata events json.

    params:
    event_list (json):

    returns:
    array of dicts with date and description fields (json)
    """
    for event in event_list:
        [event.pop(key) for key in ['locale', 'region', 'type', 'notes']]
    return event_list


def create_whole_day_event(calendar_url, caldav_url, caldav_user, caldav_pass, date='2021-01-16', event_name="testevent"):
    # https://github.com/tobixen/calendar-cli
    subprocess.run(shell=True, check=True, args=[
        "calendar-cli",
        f"--caldav-url={caldav_url}",
        f"--caldav-user={caldav_user}",
        f"--caldav-pass={caldav_pass}",
        f"--calendar-url={calendar_url}",
        f"calendar add --whole-day '{date}+1d' '{event_name}'",
        ],
    )
    sleep(2)  # avoid being blocked


if __name__ == "__main__":
    calendar_url = '' # calendar url found on Posteo under Settings > Calendar
    caldav_url = 'https://posteo.de:8443/'
    user = 'me@posteo.net',
    password = 'mypass'

    holidays = prep_events(
        jsonl_to_json(
            holidata_events_jsonl()
        )
    )

    for event in holidays:
        print(f"{event['date']}: {event['description']}")
        #create_whole_day_event(calendar_url, caldav_url, user, password, event['date'], event['description'])
