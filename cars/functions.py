import csv
import random
import string
from dotenv import load_dotenv
from pathlib import Path

from locations.models import Location

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path)


def load_data(file_name):
    with open(file_name, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        count = 0
        rows = []
        for row in file_reader:
            if count == 0:
                count += 1
                continue
            rows.append(row)

    return rows


def generate_uid_for_car():
    number = str(random.randint(1000, 9999))
    letter = random.choice(string.ascii_letters).upper()
    uid = number + letter
    return uid


def generate_load_capacity():
    load_capacity = random.randint(1, 1000)
    return load_capacity


def loc_list_create():
    locations = Location.objects.all()
    loc_list = []
    for location in locations:
        loc_list.append(location.zip_code)

    return loc_list
