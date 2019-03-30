from django.urls import path 

from .views import ProfileView      as p_views

from .views import ArticleView      as a_views
from .views import NewsView         as n_views
from .views import MultiMediaView   as m_views
from .views import CourseView     as c_views

urlpatterns = [

    path(''                              , p_views.panel       , name = 'panel'),

    # path('profile/'                      , p_views.get_profile       , name = 'get_profile'),
    # path('profile/update'                , p_views.update_profile    , name = 'update_profile'), 
    path('article/all/'                  , a_views.all_article       , name = 'all_article'),
    path('article/create/'               , a_views.create_article    , name = 'create_article'),
    path('article/update/<str:slug>'     , a_views.update_article    , name = 'update_article'),
    path('article/delete/<str:slug>'     , a_views.delete_article    , name = 'delete_article'),

    path('news/all'                      , n_views.all_news          , name = 'all_news'),
    path('news/create/'                  , n_views.create_news       , name = 'create_news'),
    path('news/update/<str:slug>'        , n_views.update_news       , name = 'update_news'),
    path('news/delete/<str:slug>'        , n_views.delete_news       , name = 'delete_news'),

    path('aa'                  , p_views.aa       , name = 'aa'),
    # path('news/update/<slug:title>'      , n_views.update_news       , name = 'update_news'),
    # path('news/delete/<slug:title>'      , n_views.delete_news       , name = 'delete_news'),

    path('multimedia/poster/all/'               , m_views.all_poster    , name = 'all_poster'),
    path('multimedia/poster/create/'            , m_views.create_poster , name = 'create_poster'),
    path('multimedia/poster/update/<str:slug>'  , m_views.update_poster , name = 'update_poster'),
    path('multimedia/poster/delete/<str:slug>'  , m_views.delete_poster , name = 'delete_poster'),
    
    path('multimedia/video/all/'                 , m_views.all_video     ,  name = 'all_video'),
    path('multimedia/video/create/'              , m_views.create_video  , name = 'create_video'),
    path('multimedia/video/update/<str:slug>'    , m_views.update_video  , name = 'update_video'),
    path('multimedia/video/delete/<str:slug>'    , m_views.delete_video  , name = 'delete_video'),

    # path('multimedia/update/<slug:title>', m_views.update_multimedia , name = 'update_multimedia'),
    # path('multimedia/delete/<slug:title>', m_views.delete_multimedia , name = 'delete_multimedia'),

    path('course/create/all/'            , c_views.all_course        , name = 'all_course'),
    path('course/create/'                , c_views.create_course     , name = 'create_course'),
    path('course/update/<slug:title>'    , c_views.update_course     , name = 'update_course'),
    path('course/delete/<slug:title>'    , c_views.delete_course     , name = 'delete_course'),
   
   

]

