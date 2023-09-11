from django.shortcuts import render, HttpResponse
from django.views import View


class Index(View):

    def get(self, request) -> HttpResponse:
        context = {
            'items': range(5000),
        }
        return render(request, template_name="catalog_app/index.html", context=context)
