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
# from django.contrib.staticfiles.templatetags.staticfiles import static

# from blog import views
from django.contrib import admin
from django.urls import include, path
from website import views as website_views
from panel.views import ProfileView as profile
from . import Seed_view
from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  # For django versions from 2.0 and up
# import debug_toolbar
urlpatterns = [

    # Panel URL's
    path('panel/',include('panel.urls'),name='user_panel'),
    path('panel/', include('django.contrib.auth.urls')), 
    # path('deb/', include(debug_toolbar.urls)),
    # Website URL's
    path('',include('website.urls')),

    path('seed', Seed_view.seeding, name = 'seeding'),
    # path('', website_views.index, name = 'index'),
    # path('post/', views.individual_post, name='individual_post'),
    # path('weblog',include('zinnia.urls'))
    path('admin', admin.site.urls),
    # path('blog', include('blog.urls')), # 
    # path('',profile.dashboard,name = 'dashboard'),
        # path('/post/new', views.post_new, name='post_new'),

    # path('', include('blog.urls'))
]

from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)