from django.conf.urls import patterns, include, url
from friends import views


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'weertik.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.friendships, name='friendships'),
)
