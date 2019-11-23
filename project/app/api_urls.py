from django.conf.urls import url
from . import api_views

urlpatterns = [
    #url(r'^$', view=api_views.Index.as_view()),
    url(r'^v1/para/$', view=api_views.Para.as_view()),
    url(r'^v1/para/(?P<para_id>\d+)/$', view=api_views.Paramodi.as_view()),
]