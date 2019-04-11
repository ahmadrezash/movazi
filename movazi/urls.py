"""movazi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from django.contrib import admin
from django.urls import include, path
from website import views as website_views
from panel.views import ProfileView as profile
from . import Seed_view
from django.conf import settings
from django.conf.urls import  url,include  # For django versions before 2.0
from django.urls import path  # For django versions from 2.0 and up
from django.conf.urls.static import static
from django.conf import settings

# import debug_toolbar
urlpatterns = [

    # Panel URL's
    path('panel/',include('panel.urls'),name='user_panel'),
    # Website URL's
    path('',include('website.urls')),

    # For Test
    path('admin', admin.site.urls),
    path('seed', Seed_view.seeding, name = 'seeding'),
    path('panel/', include('django.contrib.auth.urls')), 
    # path('deb/', include(debug_toolbar.urls)),
    # path('',profile.dashboard,name = 'dashboard'),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)