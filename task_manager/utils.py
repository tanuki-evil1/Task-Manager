import json
from pathlib import Path

from django.test import override_settings, modify_settings

test_english = override_settings(
    LANGUAGE_CODE='en-US',
    LANGUAGES=(('en', 'English'),),
)

remove_rollbar = modify_settings(
    MIDDLEWARE={
        'remove':
            ['rollbar.contrib.django.middleware.RollbarNotifierMiddleware', ]
    }
)


def load_data(path):
    with open(Path(f'task_manager/fixtures/{path}')) as file:
        return json.loads(file.read())
