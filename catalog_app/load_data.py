from pathlib import Path

from catalog_app.models import Category
from catalog_app.models import Good


def create_category(name, code_1c) -> Category:
    return Category.objects.get_or_create(name=name, code_1c=code_1c)


def create_good(name, art, code_1c, category) -> Good:
    return Good.objects.get_or_create(name=name, art=art, code_1c=code_1c, category=category)


def load_data():

    BASE_DIR = Path(__file__).resolve().parent.parent
    with open(BASE_DIR / "data.txt", mode="r") as file:
        for line in file.readlines():
            parts = line.rstrip("\n").split("\t")
            category, category_created = create_category(name=parts[3], code_1c=parts[4])
            good, good_created = create_good(name=parts[0], code_1c=parts[1], art=parts[2], category=category)
