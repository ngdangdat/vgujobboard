#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    settings = os.environ.get("DJANGO_SETTINGS_MODULE", None)
    if settings is None:
        # Not available, set a default settings
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.development")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
