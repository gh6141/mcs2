from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views
from django.urls import path,include
from django.views.generic import CreateView
from accounts.views import SignUpView,ProfileCreateView,profile_detail,profile_edit,ProfileListView



urlpatterns = [

   # path('signup/', CreateView.as_view(
   #     template_name='accounts/signup.html',
   #     form_class=UserCreationForm,
   #     success_url='/',
   # ), name='signup'),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('profile_create/',ProfileCreateView.as_view(),name='profile_create'),
    #path('<int:pk>/profile_edit/',ProfileEditView.as_view(),name='profile_edit'),
    #path('<int:pk>/profile_detail/',ProfileDetailView.as_view(),name='profile_detail'),
    path("<int:profile_id>/", profile_detail, name="profile_detail"),
    path("<int:profile_id>/profile_edit/", profile_edit, name="profile_edit"),

    path('profile_list/',ProfileListView.as_view(),name='profile_list'),
    
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='accounts/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

