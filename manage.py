#!/usr/bin/env python

import os
import sys
from medicament_supply import settings
from os.path import join

if __name__ == "__main__":
    sys.path.insert(0, join(settings.PROJECT_ROOT))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medicament_supply.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
