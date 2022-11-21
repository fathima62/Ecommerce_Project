from django.shortcuts import render,redirect

def auth_customer (func) :
    def wrap (request):
        if 'userid' in request.session :
            return func(request)
        else :
            return redirect('common:common_home')

    return wrap