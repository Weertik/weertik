from django.conf.urls import patterns, include, url
from auth_users import views


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'weertik.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^recovery', views.recovery, name='recovery'),
    url(r'^panel', views.panel, name='panel'),
    url(r'^change/(?P<token>.*)$', views.change, name='change'),
)
