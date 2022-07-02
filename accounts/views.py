from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import ProfileForm
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    form_class=UserCreationForm
    template_name="accounts/signup.html"
    success_url=reverse_lazy('top')

    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        messages.add_message(self.request,messages.SUCCESS,"会員登録されました。")
        self.object=user
        return HttpResponsePermanentRedirect(self.get_success_url())
    def form_invalid(self,form):
        messages.add_message(self.request,messages.ERROR,"会員登録できませんでした。Error")
        return super().form_invalid(form)

class ProfileCreateView(CreateView):
    form_class=ProfileForm
    template_name="accounts/profile_create.html"
    success_url=reverse_lazy('top')

    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        messages.add_message(self.request,messages.SUCCESS,"プロフィールが登録されました。")
        self.object=user
        return HttpResponsePermanentRedirect(self.get_success_url())
    def form_invalid(self,form):
        messages.add_message(self.request,messages.ERROR,"プロフィールの登録ができませんでした。Error")
        return super().form_invalid(form)
