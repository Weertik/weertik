# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext, loader
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import uuid
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


def _send_email(template, context, emails, subject, origin='info@weertik.com'):
    plaintext = get_template(template + '.txt')
    html = get_template(template + '.html')

    text_content = plaintext.render(context)
    html_content = html.render(context)
    msg = EmailMultiAlternatives(subject,
                                 text_content, origin, emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('panel'))
    if request.method != 'POST':
        return render(request, 'login.html')

    user = auth.authenticate(username=request.POST.get('username', ''),
                             password=request.POST.get('password', ''))
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('panel'))
    else:
        error = 'username and password not is correct'
        return render_to_response('login.html',
                                  {'error': error},
                                  context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))


def recovery(request):
    if request.method != 'POST':
        return render(request, 'recovery.html')
    email = request.POST.get('email', '')
    user = None
    try:
        user = User.objects.get(email=email)
        token_user = Token_auth.objects.get(user=user)
    except User.DoesNotExist:
        return render_to_response('recovery.html',
                                  {'error': True, 'email': email},
                                  context_instance=RequestContext(request))
    except Token_auth.DoesNotExist:
        token_user = Token_auth()
        token_user.user = user
        token_user.token = uuid.uuid4().hex
        token_user.save()

    context = Context({'username': user.username,
                       'token': token_user.token})

    _send_email('recovery_email',
                context, [email],
                'Weertik - Recuperar contraseña')

    return render_to_response('recovery.html',
                              {'send': True},
                              context_instance=RequestContext(request))


def change(request, token):
    try:
        token_user = Token_auth.objects.get(token=token)
        user = token_user.user
    except Token_auth.DoesNotExist:
        return render_to_response('change.html',
                                  {'e_token': True},
                                  context_instance=RequestContext(request))

    if request.method == 'POST':
        password = request.POST.get('password', '1')
        password_repeat = request.POST.get('password_repeat', '2')
        if password == password_repeat:
            user.set_password(password)
            user.save()
            token_user.delete()
            context = Context({'username': user.username})

            _send_email('change_email', context,
                        [user.email], 'Weertik - Contraseña modificada')
            return render_to_response('change.html',
                                      {'send': True},
                                      context_instance=RequestContext(request))
        return render_to_response('change.html',
                                  {'e_pass': True, 'user': user},
                                  context_instance=RequestContext(request))
    return render_to_response('change.html',
                              {'user': user},
                              context_instance=RequestContext(request))


def signup(request):
    if request.method != 'POST':
        return render_to_response('signup.html',
                                  {'form': SignupForm()},
                                  context_instance=RequestContext(request))

    form = SignupForm(request.POST)
    if form.is_valid():
        exist = False
        send = False
        try:
            user = User.objects.create_user(
                first_name=form.data['first_name'],
                last_name=form.data['last_name'],
                password=form.data['password'],
                username=form.data['email'],
                email=form.data['email'])
        except Exception, e:
            user = User.objects.get(email=form.data['email'])
            exist = True

        if not exist:
            user.is_active = False
            user.save()
            group = Group.objects.get(name='Free')
            group.user_set.add(user)

        try:
            token_user = Token_auth.objects.get(user=user)
        except Token_auth.DoesNotExist:
            token_user = Token_auth()
            token_user.user = user
            token_user.token = uuid.uuid4().hex
            token_user.save()

        if not user.is_active:
            context = Context({'username': user.username,
                               'token': token_user.token})
            _send_email('signup_email',
                        context, [user.email],
                        'Weertik - Activa tu cuenta')
            send = True

        return render_to_response('signup.html',
                                  {'send': send,
                                   'exist': exist,
                                   'email': user.email,
                                   'form': form},
                                  context_instance=RequestContext(request))

    return render_to_response('signup.html',
                              {'form': form},
                              context_instance=RequestContext(request))


def active(request, token):
    try:
        token_user = Token_auth.objects.get(token=token)
        user = token_user.user
    except Token_auth.DoesNotExist:
        return render_to_response('active.html',
                                  {'e_token': True},
                                  context_instance=RequestContext(request))

    user.is_active = True
    user.save()
    token_user.delete()
    context = Context({'username': user.username})
    _send_email('active_email', context,
                [user.email], 'Weertik - Cuenta activada')
    return render_to_response('active.html',
                              {'send': True},
                              context_instance=RequestContext(request))

# DELETE THIS
def panel(request):
    auth.logout(request)
    return render(request, 'panel.html')
