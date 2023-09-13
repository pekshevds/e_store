from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from cart_app.service import add_good_to_cart_by_id
from cart_app.models import CartItem


class Index(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        items = CartItem.objects.filter(customer=request.user)
        context = {
            "items": items
        }
        return render(request=request, template_name="cart_app/index.html", context=context)

    @staticmethod
    def add(request, *args, **kwargs):
        if request.user.is_authenticated:
            good_id = kwargs.get("good_id", 0)
            add_good_to_cart_by_id(customer=request.user, good_id=good_id)
            return redirect("cart:index-page")
        return redirect("auth:sign-in-page")
