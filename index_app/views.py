from django.shortcuts import render, HttpResponse
from django.views import View


class Index(View):

    def get(self, request) -> HttpResponse:
        return render(request, "index_app/index.html")
