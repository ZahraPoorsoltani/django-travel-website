from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from accounts.utils import CustomBackend
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.forms import CustomAuthenticationForm,CustomUserCreationForm
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomAuthenticationForm(request=request,data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                print(username)
                user = CustomBackend.authenticate(request,username=username,password = password)
                if user is not None:
                    login(request,user)
                    messages.add_message(request,messages.SUCCESS,f'welcom, {username}')
                    return redirect('/')
                else:
                    messages.add_message(request,messages.ERROR,'this user is not exist!')

            
            else:
                print(form.errors)
                add_err(request,form.errors)              

        return render(request,'login.html')
    return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def add_err(request,form_err):
    err = form_err.items()
    for key,vals in err:
        for v in vals:
            messages.add_message(request,messages.ERROR,key+': '+v)

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = CustomUserCreationForm(request.POST)
            
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,f'registeration completed!')
                return redirect(reverse('accounts:login_view'))
            
            print(form.errors)
            add_err(request,form.errors)

            return render(request,'register.html',{'form':form})
        
        form = CustomUserCreationForm()
        # print(form)
        return render(request,'register.html',{'form':form})
    return redirect('/')


def pass_reset_view(request):
    form =PasswordResetForm()
    return render(request,'password-reset.html',{'form':form})