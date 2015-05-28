from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from account.forms import UserForm

# Create your views here.

def signup(request):
    context = RequestContext(request)

    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
            return HttpResponse("Form is not properly filled in.")
    else:
        user_form = UserForm()

    return render_to_response('account/signup.html', {'user_form': user_form, 'registered': registered}, context)

def user_login(request):
    context = RequestContext(request)

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            #TPB
            return render_to_response('account/login.html', {'error_msg': "Incorrect account info, please try again."}, context)
    else:
        return render_to_response('account/login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))
