"""backend URL Configuration

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
from django.urls import path, include
from departments import views
from . import views as homeViews
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.i18n import i18n_patterns

admin.sites.AdminSite.site_header = 'RECB Admin'
admin.sites.AdminSite.site_title = 'Rajkiya Engineering College, Bijnor'
admin.sites.AdminSite.index_title = 'REC,Bijnor'

urlpatterns = [
    path("i18n", include("django.conf.urls.i18n")),
    path('create', views.create_department, name='form'),
    path('', homeViews.home, name='department')

]
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
