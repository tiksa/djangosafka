from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'safka.views.home'),
    url(r'^fetchvotes$', 'safka.views.fetch_votes'),
    url(r'^add$', 'safka.views.add'),
    url(r'^clear$', 'safka.views.clear_votes'),
    # url(r'^djangosafka/', include('djangosafka.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
