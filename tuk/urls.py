from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.welcome, name = 'welcome'),
    url('^profile/', views.profile, name= 'profile'),
    url(r'^new/article$', views.new_article, name='new-article')
]
