from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,logout,login
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from sign_up_app.forms import SignupForm, ProfileChangeForm

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


@login_required
def change_profile(request):
    curr_user = request.user
    change_form = ProfileChangeForm(instance=curr_user)
    if request.method == 'POST':
        change_form = ProfileChangeForm(request.POST, instance=curr_user)
        if change_form.is_valid():
            change_form.save()
            change_form = ProfileChangeForm(instance=curr_user)

    return render(request, 'account/change_profile.html', context={'change_form':change_form})


@login_required
def change_pass(request):
    curr_user = request.user
    changed = False
    change_pass_form = PasswordChangeForm(curr_user)
    if request.method == 'POST':
        change_pass_form = PasswordChangeForm(curr_user, data=request.POST)
        if change_pass_form.is_valid():
            change_pass_form.save()
            changed = True
            return HttpResponseRedirect(reverse('Albumapp:albumspage'))
    return render(request, 'account/change_pass.html', context={'change_pass_form':change_pass_form, 'changed':changed})

