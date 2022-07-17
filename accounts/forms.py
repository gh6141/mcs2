from django import forms

from accounts.models import User

from django.contrib.auth.forms import(
  UserCreationForm as BaseUserCreationForm,
  UserChangeForm as BaseUserChangeFrom,
)

import datetime


class UserCreationForm(BaseUserCreationForm):
  class Meta(BaseUserCreationForm.Meta):
    model = User

class UserChangeForm(BaseUserChangeFrom):
  class Meta(BaseUserChangeFrom.Meta):
    model=User


class ProfileForm(forms.ModelForm):

    class Meta:
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        model = User
        fields = ('nickname','sex','date_of_birth','shussin','kyojuchi','shokugyo','shumi','self_introduction','doi_flg','profile_photo1','profile_photo2',
          'profile_photo3','profile_photo4','profile_photo5','tabako','osake','kekkonreki','kodomo',
          'is_admin','is_staff','date_joined','is_active')
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=[x for x in range(int(year)-80, int(year)-19)])
        }
"""
      
    username=
      nickname=
    email=
    sex=
    
    date_of_birth =
    shussin = 
    kyojuchi = 
    shokugyo = 
    shumi = 
    self_introduction=
    doi_flg=
    profile_photo1=
    profile_photo2=
    profile_photo3=
    profile_photo4=
    profile_photo5=
    tabako = 
    osake = 
    kekkonreki =
    kodomo = 

    is_admin=
    is_staff=
    date_joined=
    is_active = 
   
"""




