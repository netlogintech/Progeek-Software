"""Progeek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from app import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('it-outsourcing/',views.it_outsourcing,name="outsourcing"),
    path('ims/',views.ims,name="ims"),
    path('testing',views.testing,name="testing"),
    path('managed/',views.managed,name="manage"),
    path('enterprise/',views.enterprise,name="enterprise"),
    path('captive/',views.captive,name="captive"),
    path('strategic/',views.strategic,name="strategic"),
    path('outsourced/',views.outsourced,name="outsourced"),
    path('system/',views.system,name="system"),
    path('enterprise-solution/',views.enterprise_solution),
    path('big-data/',views.big_data,name="big data"),
    path('data-sciences/',views.data_science,name="data science"),
    path('social/',views.social,name="social"),
    path('automation/',views.automations,name="automations"),
    path('cloud/',views.cloud,name="cloud"),
    path('mobility/',views.mobolity,name="mobolity"),
    path('robotics/',views.robotics,name="robotics"),
    path('IBM-solution/',views.ibm,name="ibm"),
    path('MS-solutions/',views.ms_app,name="Ms App"),
    path('MS-tech/',views.ms_tech,name="Ms Tech"),
    path('about/',views.about,name="about"),
    path('live/',views.live,name="live"),
    path('meeting/',views.meeting,name="meeting"),
    path('signup', views.register,name="reg"),
    path('career',views.career,name="career"),
    path('login', LoginView.as_view(template_name='app/login.html'),name='customerlogin'),
    path('logout', LogoutView.as_view(template_name='app/logout.html'),name='logout'),
    path('search/',views.search,name="search"),
    path('trainer/',views.trainer,name="trainer"),
    path('add-meet/',views.add_meeting,name="search"),
    path('afterlogin/',views.afterlogin_view),
    path('delete-gp/<int:pk>', views.delete_data,name='delete-gp'),
    path('join/',views.join,name="join"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
