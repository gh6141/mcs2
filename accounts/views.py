from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseForbidden

# Create your views here.
from django.contrib import messages
from django.contrib.auth import login
#from django.contrib.auth.forms import UserCreationForm
from accounts.forms import ProfileForm,UserCreationForm
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DetailView,ListView

from django.contrib.auth.decorators import login_required

from accounts.models import User
from django.db.models import Q

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


@login_required
def profile_edit(request, profile_id):
    user = get_object_or_404(User, pk=profile_id)
    if user.username != request.user.username:
        return HttpResponseForbidden("このメッセージの編集は許可されていません。")

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            post=form.save()
            post.profile_photo1=request.FILES.get('profile_photo1')
            post.save()
            return redirect('profile_detail', profile_id=profile_id)
    else:
        form = ProfileForm(instance=user)
    return render(request, 'accounts/profile_edit.html', {'form': form})


@login_required
def profile_detail(request, profile_id):
    user = get_object_or_404(User, pk=profile_id)
    
    return render(request, 'accounts/profile_detail.html',
                  {'user':user,})



class ProfileListView(LoginRequiredMixin,ListView): 
    def get_queryset(self):
        q_word = self.request.GET.get('query')
 
        if q_word:
            object_list = User.objects.filter(  Q(nickname__icontains=q_word) )
        else:
            object_list = User.objects.all()
        return object_list


"""
class ProfileEditView(LoginRequiredMixin,UpdateView):
    model=User
    fields = ('nickname','sex','date_of_birth','shussin','kyojuchi','shokugyo','shumi','self_introduction','doi_flg','profile_photo1','profile_photo2',
          'profile_photo3','profile_photo4','profile_photo5','tabako','osake','kekkonreki','kodomo',
          'is_admin','is_staff','date_joined','is_active')
    template_name="accounts/profile_edit.html"

    def get_object(self,queryset=None):
        obj=super().get_object(queryset)

        if obj.username != self.request.username:
            raise PermissionDenied
        return obj
    def get_success_url(self) -> str:
        return reverse('profile_detail',kwargs={'pk':self.object.id})

class ProfileDetailView(LoginRequiredMixin,DetailView):
    model=User
    template_name="accounts/profile_detail.html"

"""

