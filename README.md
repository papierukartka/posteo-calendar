# wtf

This is an attempt to glue [holidata](https://github.com/GothenburgBitFactory/holidata) and [calendar-cli](https://github.com/tobixen/calendar-cli) in order to create something resembling Google's holiday calendar on Posteo.
Might work for other calendar providers too.

# Usage

- Get install requirements.txt, or just `pip install --user -U calendar-cli`
- Edit the variables in the main section of the script:

```python
calendar_url = ''
caldav_url = ''
user = 'me@posteo.net',
password = 'mypass'
```

- Uncomment `create_whole_day_event` line which connects to the calendar after you've made sure you're safe
- Run `python posteo_holidays.py`

