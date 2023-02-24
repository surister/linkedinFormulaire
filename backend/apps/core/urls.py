from django.urls import path

from .views import FormView

urlpatterns = [
    path('contactform/', FormView.as_view()),
]
