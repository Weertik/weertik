from django.shortcuts import render
from .models import *
from django.shortcuts import render_to_response


@login_required(login_url='/')
class friendships(request):
    user = request.user
    my_friends = Friendship.objects.get(from_user=user, status='A')
    my_friends += Friendship.objects.get(to_user=user, status='A')
    render_to_response('friends.html',
                       {'friends': my_friends},
                       context_instance=RequestContext(request))
