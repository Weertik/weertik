from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponse
import json
from .models import *


@login_required(login_url='/')
def friendships(request):
    param = {}
    user = request.user
    my_friends = None
    try:
        my_friends = Friendship.objects.all().filter(
            Q(from_user=user) | Q(to_user=user), status='A')
        param['friends'] = [x.from_user if x.to_user == user else x.to_user
                            for x in my_friends]
    except Friendship.DoesNotExist:
        print "Forever alone :'')"
    return render_to_response('friends.html', param,
                              context_instance=RequestContext(request))


@login_required(login_url='/')
def ajax_friendship(request):
    response = {}
    user = request.user
    if request.method == 'POST' and request.is_ajax():
        vals = {}
        uid = request.POST.get('uid', False)
        vals['status'] = request.POST.get('status', 'W')
        if uid != user.id:
            f_user = User.objects.get(id=uid)
            friendship = Friendship.objects.all().filter(
                Q(from_user=f_user, to_user=user) |
                Q(from_user=user, to_user=f_user))
            if friendship:
                if (friendship[0].to_user == user
                        or (vals['status'] == 'B'
                            and friendship[0].status != 'B')):
                    friend = friendship[0]
                    friend.status = vals['status']
                else:
                    response['error'] = True
            else:
                vals['to_user'] = f_user
                vals['from_user'] = user
                friend = Friendship(**vals)
            if 'error' not in response:
                friend.save()
                response['status'] = True
        else:
            response['error'] = True
    return HttpResponse(json.dumps(response), mimetype='application/json')
