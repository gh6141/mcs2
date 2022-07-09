from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import User

from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError



class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username')

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'username','kyojuchi','kekkonreki')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'username', 'is_staff','kyojuchi','kekkonreki')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'username')
    ordering = ('email',)
# -----------
class UserCreationForm(forms.ModelForm):#ユーザー登録フォームを作成

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'nickname', 'date_of_birth')

    def clean_password2(self):#確認用パスワードが合致するかチェック
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):#パスワードを生成
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):#ユーザー更新フォームを作成

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'nickname', 'date_of_birth', 'is_active','kyojuchi','kekkonreki')


class UserAdmin(BaseUserAdmin):#Django管理サイトの画面を編集

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id','username','email', 'nickname', 'date_of_birth','kyojuchi','kekkonreki')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal name', {'fields': ('username','nickname','sex')}),
        ('Personal info', {'fields': ('date_of_birth', 'shussin','kyojuchi','shokugyo','shumi','self_introduction','doi_flg','profile_photo1',
        'profile_photo2','profile_photo3','profile_photo4','profile_photo5','tabako','osake','kekkonreki','kodomo','date_joined')}), )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nickname', 'date_of_birth', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User,UserAdmin)
admin.site.unregister(Group)#Django管理サイトからGroupモデルの削除
# Register your models here.

