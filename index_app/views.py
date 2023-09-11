from django.shortcuts import render, HttpResponse
from django.views import View


class Index(View):

    def get(self, request) -> HttpResponse:
        return render(request, template_name="index_app/index.html")
