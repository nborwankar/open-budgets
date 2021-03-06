from django.conf.urls import patterns, url
from openbudget.apps.entities.views.ui import EntityDetail, EntityList


urlpatterns = patterns('',

    url(r'^$', EntityList.as_view(), name='entity_list'),

    url(r'^jsi18n/$',
        'django.views.i18n.javascript_catalog',
        {'packages': ('openbudget.apps.entities',)},
        name='entities_js_i18n'),

    url(r'^(?P<slug>[-\w]+)/$', EntityDetail.as_view(), name='entity_detail'),
    url(r'^(?P<slug>[-\w]+)/(?P<period>\d+)/$', EntityDetail.as_view(), name='entity_detail'),
    url(r'^(?P<slug>[-\w]+)/(?P<period>\d+)/(?P<item_uuid>\w+)/$', EntityDetail.as_view(), name='entity_detail'),
)
