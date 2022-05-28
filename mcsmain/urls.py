from django.urls import path

from mcsmain import views

urlpatterns = [
    path("new/", views.mcsmain_new, name="mcsmain_new"),
    path("<int:mcsmain_id>/", views.mcsmain_detail, name="mcsmain_detail"),
    path("<int:mcsmain_id>/edit/", views.mcsmain_edit, name="mcsmain_edit"),
]

