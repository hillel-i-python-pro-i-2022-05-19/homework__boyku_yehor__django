from django.urls import path
from . import views

urlpatterns = [
    path('', views.name_and_email_generated),
    path('<int:number>', views.name_and_email_generated)
]
