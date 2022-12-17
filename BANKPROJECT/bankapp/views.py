from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bankapp.models import Form


# Create your views here.
def demo(request):
    return render(request, 'index.html')


def loginuser(request):
    if request.method == 'POST':
        username1 = request.POST.get('username', '')
        password1 = request.POST.get('password', '')
        user1 = authenticate(request, username=username1, password=password1)
        print(user1)
        if user1 is not None:

            auth.login(request, user1)
            return redirect('/form')
        else:
            messages.info(request, "invalid credentials")
            return redirect('/login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('/register')
            else:

                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('/login')
        else:
            messages.info(request, "Wrong password")
            return redirect('/register')
    return render(request, 'register.html')


def form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        dob = request.POST.get('dob', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        email = request.POST.get('email', '')
        number = request.POST.get('number', '')
        address = request.POST.get('address', '')
        district = request.POST.get('district', '')
        branch = request.POST.get('branch', '')
        accountType = request.POST.get('accountType', '')
        material = request.POST.get('material', '')
        user = Form(first_name=first_name, last_name=last_name, dob=dob, age=age, gender=gender, email=email,
                    number=number, address=address, district=district, branch=branch, account_type=accountType,
                    material=material)
        print(user)
        if user is not None:
            user.save()
            return redirect('/success')
        else:
            return redirect('/form')
    return render(request, 'person.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def success(request):
    # x=Form.objects.all()
    # x = Form.objects.get('first_name')
    x=request.POST.get('first_name','')
    y=request.POST.get('number','')
    z=request.POST.get('email','')
    return render(request, 'success.html', {'x': x, 'y':y, 'z':z})
