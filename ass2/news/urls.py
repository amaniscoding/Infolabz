"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from redchillinews import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('sports',views.sports,name='sports'),
    path('entertainment',views.entertainment,name="entertainment"),
    path('business',views.business,name="business"),
    path('national',views.national,name="national"),
    path('world',views.world,name="world"),
    path('politics',views.politics,name="politics"),
    path('technology',views.technology,name="technology"),
    path('startup',views.startup,name="startup"),
    path('miscellaneous',views.miscellaneous,name="miscellaneous"),
    path('unconventional',views.unconventional,name="unconventional"),
    path('science',views.science,name="science"),
    path('automobile',views.automobile,name="automobile"),
]
