"""
URL configuration for povertyclassifier project.

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
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from knnclassifier import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', views.index, name='homepage'),
    re_path('predictImage', views.predictImage, name="predictImage"),
    re_path('viewDataBase', views.viewDataBase, name='viewDataBase'),
    re_path('save_prediction', views.save_prediction, name='save_prediction')
]


# currently only for the development purpose
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)