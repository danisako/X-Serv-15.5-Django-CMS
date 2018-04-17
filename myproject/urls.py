from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$','cms.views.index'),
	url(r'^(.+)$','cms.views.muestra'),
    url(r'^admin/', include(admin.site.urls)),
)
