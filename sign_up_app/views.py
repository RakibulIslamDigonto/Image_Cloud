from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,logout,login
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from sign_up_app.forms import SignupForm

def signup(request):
    form = SignupForm()
    register = False
    
    
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            register = True

    context ={
        'title':'Create Account From',
        'signup_form':form,
        'register':register
    }
    return render(request, 'account/signup.html', context)


def login_user(request):
    login_form = AuthenticationForm()
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Albumapp:albumspage'))
    return render(request, 'account/login.html', context={'login_form':login_form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Albumapp:albumspage'))
            
@login_required
def profile(request):
    return render(request, 'account/profile.html', context={})


