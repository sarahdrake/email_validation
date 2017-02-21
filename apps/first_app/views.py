from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'first_app/index.html')

def process(request):
    if request.method == 'POST':
        email_check = User.objects.login(request.POST['email'])
        if email_check == False:
            messages.add_message(request, messages.INFO, "Email not valid")
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, "Your email is valid!")
            return redirect('/success')
    else:
        return redirect('/')
def success(request):
    context ={
        'users': User.objects.all()
    }
    return render(request, 'first_app/success.html', context)
