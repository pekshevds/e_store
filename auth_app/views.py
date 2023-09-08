from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login

from django.contrib.auth import get_user_model


class AuthSingInView(LoginView):
    template_name = "auth_app/signin.html"
    authentication_form = AuthenticationForm

    def get(self, request, *args, **kwargs):

        context = {"form": self.authentication_form()}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        form = self.authentication_form(request=request, data=request.POST)
        if not form.is_valid():
            context = {
                "form": form,
                "errors": form.errors,
            }
            return render(request, template_name=self.template_name, context=context)
        user = authenticate(request,
                            username=form.cleaned_data.get("username", ""),
                            password=form.cleaned_data.get("password", ""))
        if user:
            login(request, user)
            return redirect("index:index-page")
        else:
            return redirect("index:sign-in-page")


class AuthSingUpCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class AuthSingUpView(LoginView):
    template_name = "auth_app/signup.html"
    authentication_form = AuthSingUpCreationForm

    def get(self, request, *args, **kwargs):

        context = {
            "form": self.authentication_form(),
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        form = self.authentication_form(data=request.POST)
        if not form.is_valid():
            context = {
                "form": form,
                "errors": form.errors,
            }
            return render(request, template_name=self.template_name, context=context)
        form.save()
        return redirect("auth:sign-in-page")


class AuthSingOutView(LogoutView):
    pass
