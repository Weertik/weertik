from django.conf.urls import patterns, include, url
from django.contrib import admin
from auth_users import urls as auth_users_urls
from auth_users import views as auth_users_views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'weertik.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', auth_users_views.login),  # Only for login
    url(r'^auth/', include(auth_users_urls)),  # Other urls
)
