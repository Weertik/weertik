from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def panel(request):
    return render(request, 'panel.html')