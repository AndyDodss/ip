from django.urls import re_path ,path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('home',views.home,name='home'),

]