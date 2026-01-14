from django.urls import path
from . import views

urlpatterns = [
    path("set-lang/<str:lang>/", views.set_lang, name="set_lang"),
    path("", views.home, name="home"),
    path("work/", views.work, name="work"),
    path("work/<slug:slug>/", views.series_detail, name="series_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
