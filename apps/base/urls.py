from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.base.views import HomeTemplateView

app_name = 'base'
urlpatterns = [
    path('', login_required(HomeTemplateView.as_view()), name='home'),
]
