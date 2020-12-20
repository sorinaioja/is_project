from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from asgiref.sync import sync_to_async

from django.conf import settings


def index(request):
    context = {}
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
    'room_name': room_name
    })

