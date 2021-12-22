from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your view here.
def index(request):
    if request.method == "POST":
        return render(request, "index.html")
        Username = request.post['Username']
        Email = request.post['Email']
        Password = request.post['Password']
        ConfirmPassword = request.post['Confirm Password']
        Address = request.post['Address']

        myuser = User.objects.create_user(Username, Email, Password, ConfirmPassword, Address)

        myuser.save()

        messages.success(request, "Your Loginform has been successfull.")

        return redirect('signin')


def signup(request):
    return render(request, "signup.html")

def Email(request):
    return render(request, "Email.html")

def Password(request):
    return render(request, "Password.html")

def Address (request):
    return render(request, "Address .html")