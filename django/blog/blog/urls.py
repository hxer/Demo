"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'core.views.home', name='home'),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name':'core/cover.html'} , name='login'),
    url(r'^logout', 'django.contrib.auth.views.logout', {'next_page':'/'} , name='logout'),
    url(r'^signup/$', 'myauth.views.signup', name='signup'),
    url(r'^setting/$', 'core.views.setting', name='setting'),
    url(r'^setting/picture/$', 'core.views.picture', name='picture'),
    url(r'^setting/picture/upload_picture$', 'core.views.upload_picture', name='upload_picture'),
    url(r'^setting/save_uploaded_picture$', 'core.views.save_uploaded_picture', name='save_uploaded_picture'),
    url(r'setting/password/$', 'core.views.password', name='password'),
    url(r'(?P<username>[^/]+)/$', 'core.views.profile', name='profile'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
