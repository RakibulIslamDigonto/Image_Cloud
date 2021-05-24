from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm()
    register = False
    
    
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            register = True

    context ={
        'title':'Create Account From',
        'signup_form':form,
        'register':register
    }
    return render(request, 'signup/signup.html', context)

