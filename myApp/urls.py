"""PracticeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from myApp.views import *
from django.conf.urls import url 


urlpatterns = [

    path("",index, name = 'home'),
    path("processor/", processor, name = 'processor'),
    path("graphics/", graphics, name = 'graphics'),
    path("storage/", storage, name = 'storage'),
    path("motherboard/", motherboard, name = 'motherboard'),
    path("ram/", ram, name = 'ram'),
    path("references/", references, name = 'references'),
    path("graphics_page_2/", graphics2, name = 'graphics_page_2'),
    path("processor_page_2/", processor2, name = 'processor_page_2'),
    path("storage_page_2/", storage2, name = 'storage_page_2'),
    url(r'^createuser/$', Create_User, name = 'createuser'),
    url(r'^createbuild/(\d+)/$', Create_Build, name = 'createbuild'),
    url(r'^buildlist/(\d+)/$', BuildList, name = 'buildlist'),
    url(r'^delete/(\d+)/$', Delete, name='delete'),
    url(r'^edit/(\d+)/$', Edit, name='edit'),
    url(r'^update/(\d+)/$', Update, name='update'),
]


# url(r'^addnewbuild/(\d+)/$', add_build_page_view),

    # url(r'^buildlist/(\d+)/$', UserBuildList_view),

    # url(r'^addlist/(\d+)/$', Add_New_Build_To_List),

    # url(r'^createlist/$', Create_List),