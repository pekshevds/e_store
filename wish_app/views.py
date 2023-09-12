from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class Index(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="wish_app/index.html")
