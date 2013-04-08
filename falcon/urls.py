from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'falcon.views.home', name='home'),
    # url(r'^falcon/', include('falcon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include('demo.apps.home.url')),
    #url(r'^$', 'principal.views.formulario_view'),
    url(r'^$', 'principal.views.ubicacion_view'),
    #url(r'^contact/$', 'principal.views.contact'),
    #url(r'^ejemplo/$', 'principal.views.ejemplo_view'),

)
