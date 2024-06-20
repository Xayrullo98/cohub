"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp.views import *
from app.settings import DEBUG, MEDIA_URL, MEDIAFILE_DIRS, STATICFILES_DIRS, STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('detail/<id>/', portfolio, name='detail'),

]
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIAFILE_DIRS)
    urlpatterns += static(STATIC_URL, document_root=STATICFILES_DIRS)
