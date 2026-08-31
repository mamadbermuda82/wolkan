from django.urls import path
from .views import home, prompt_detail

urlpatterns = [
    path("", home, name="home"),
    path("prompt/<int:pk>/", prompt_detail, name="prompt_detail"),
]