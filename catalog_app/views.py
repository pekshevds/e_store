from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
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

        paginator = Paginator(goods, 27)
        page_number = request.GET.get("page", 0)

        route = ""
        if current_category:
            route += f"category={current_category.id}&"
        route += "page="
        if route:
            route = "?" + route

        context = {
            'current_category': current_category,
            'categories': categories,
            'goods': paginator.get_page(page_number),
            'route': route,
            'range': range(2, paginator.num_pages)
        }
        return render(request, template_name="catalog_app/index.html", context=context)
