# decorators.py
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages

def login_required(function):
    def wrap(request, *args, **kwargs):
        if 'user_id' in request.session:
            return function(request, *args, **kwargs)
        else:
            messages.add_message(request, messages.WARNING, 'The session has expired. Please login again to continue.')
            return redirect('custom_login')
    return wrap

def is_entrepreneur(function):
    def wrap(request, *args, **kwargs):
        if 'user_id' in request.session and request.session['user_type'] == "entrepreneur":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

def is_expert(function):
    def wrap(request, *args, **kwargs):
        if 'user_id' in request.session and request.session['user_type'] == "expert":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

def is_investor(function):
    def wrap(request, *args, **kwargs):
        if 'user_id' in request.session and request.session['user_type'] == "investor":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap