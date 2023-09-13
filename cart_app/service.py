from cart_app.models import CartItem
from catalog_app.models import Good
from auth_app.models import User


def add_good_to_cart_by_id(customer: User, good_id: int):
    if good_id and customer:
        good = Good.objects.get(id=good_id)
        cart_item = CartItem.objects.create(customer=customer, good=good, qnt=1)
        cart_item.save()
