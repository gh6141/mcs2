from django import forms

from accounts.models import User

from django.contrib.auth.forms import(
  UserCreationForm as BaseUserCreationForm,
  UserChangeForm as BaseUserChangeFrom,
)

import datetime
from django.core.exceptions import ValidationError


class UserCreationForm(BaseUserCreationForm):
  class Meta(BaseUserCreationForm.Meta):
    model = User

class UserChangeForm(BaseUserChangeFrom):
  class Meta(BaseUserChangeFrom.Meta):
    model=User

def age(birthday):
    today = datetime.date.today()
    return (int(today.strftime("%Y%m%d")) - int(birthday.strftime("%Y%m%d"))) // 10000

class ProfileForm(forms.ModelForm):
    class Meta:
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        model = User
        fields = ('nickname','sex','date_of_birth','shussin','kyojuchi','shokugyo','shumi','self_introduction','doi_flg','profile_photo1','profile_photo2',
          'profile_photo3','profile_photo4','profile_photo5','tabako','osake','kekkonreki','kodomo',
          'is_admin','is_staff','date_joined','is_active')
        MONTHS = {
         1: '1', 2: '2', 3: '3', 4: '4',
         5: '5', 6: '6', 7: '7', 8: '8',
         9: '9', 10: '10', 11: '11', 12: '12'
         }

        widgets = {
            'date_of_birth': forms.SelectDateWidget(months=MONTHS,years=[x for x in range(int(year)-80, int(year)-19)])
        }
        
    def clean_date_of_birth(self):
        dobirth = self.cleaned_data.get('date_of_birth')
        year=age(dobirth)    
        if year<20 or year>=80:
             self.add_error(None, '申し訳ありませんが、利用できるのは２０歳以上８０歳未満の方です。')
        return dobirth
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




