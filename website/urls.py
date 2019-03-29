from django.urls import include,  path 

from . import views
# from .views import ProfileView      as p_views


urlpatterns = [


    path(''                    , views.index                   , name = 'home'),
    path('home/'               , views.index                   , name = 'home'),

    path('blog'                , views.blog_main               , name = 'blog_main'),

    path('article/'            , views.article_pagination      , name = 'article_pagination'),
    path('article/main'        , views.article_pagination      , name = 'article_pagination'),
    path('article/<str:slug>'  , views.article_single          , name = 'article_single'),

    path('poster/'             , views.poster_pagination       , name = 'poster_pagination'),
    path('poster/main'         , views.poster_pagination       , name = 'poster_pagination'),
    path('poster/<str:slug>'   , views.poster_single           , name = 'poster_single'),

    path('news/'               , views.news_pagination         , name = 'news_pagination'),
    path('news/main'           , views.news_pagination         , name = 'news_pagination'),
    path('news/<str:slug>'     , views.news_single             , name = 'news_single'),


  
  
    # path('news/'             , n_views.create_news         , name = 'create_news'),
  
  
    # path('news/main'         , n_views.create_news         , name = 'create_news'),
  
    # path('multimedia/'       , m_views.create_multimedia   , name = 'create_multimedia'),

    # path('multimedia/main'   , m_views.create_multimedia   , name = 'create_multimedia'),
  
    # path('course/'           , c_views.create_course       , name = 'create_course'),
    # path('course/main'       , c_views.create_course       , name = 'create_course')

]

