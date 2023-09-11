from pathlib import Path

from catalog_app.models import Category
from catalog_app.models import Good


def load_data():

    BASE_DIR = Path(__file__).resolve().parent.parent
    with open(BASE_DIR / "data.txt", mode="r") as file:
        for line in file.readlines():
            parts = line.rstrip("\n").split("\t")
            print(parts)
