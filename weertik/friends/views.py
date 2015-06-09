from django.shortcuts import render
from django.template import RequestContext, loader
from .models import *
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required(login_url='/')
def friendships(request):
    user = request.user
    my_friends = None
    try:
        my_friends = Friendship.objects.all().filter(
        	Q(from_user=user) | Q(to_user=user),
        	status='A')
    except Friendship.DoesNotExist:
        print "Forever alone :'')"

    return render_to_response('friends.html',
                              {'friends': my_friends},
                              context_instance=RequestContext(request))
