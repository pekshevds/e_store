from django.shortcuts import render, HttpResponse
from django.views import View

from catalog_app.models import Good
from catalog_app.models import Category


class Index(View):

    def get(self, request, *args, **kwargs) -> HttpResponse:

        category_id = request.GET.get("category", 0)
        categories = Category.objects.all()
        current_category = None
        goods = Good.objects.all()
        if category_id:
            category = Category.objects.get(id=category_id)
            current_category = category
            goods = Good.objects.filter(category=category)

        context = {
            'current_category': current_category,
            'categories': categories,
            'goods': goods,
        }
        return render(request, template_name="catalog_app/index.html", context=context)
