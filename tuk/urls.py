from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.news_today, name = 'newsToday'),

    url('^profile/', views.profile, name= 'profile'),
    url(r'^new/article$', views.new_article, name='new-article')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
