"""whys_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path

from whys_app_data.views.importView import ImportView
from whys_app_data.views.deleteView import DeleteAll
from whys_app_data.views.modelListView import ModelListView
from whys_app_data.views.modelDetailView import ModelDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    path('import', ImportView.as_view()),
    path('detail/<str:nazev_modulu>/', ModelListView.as_view()),
    path('detail/<str:nazev_modulu>/<int:id>/', ModelDetailView.as_view()),

    path('del', DeleteAll.as_view()),
]
