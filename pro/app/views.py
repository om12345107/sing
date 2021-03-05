from django.shortcuts import render, HttpResponseRedirect
from app.forms import sing
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def show(request):
    if request.method == "POST":
        blog = sing(request.POST)
        if blog.is_valid():
            blog.save()
    else:
        blog = sing()
    return render(request, 'folder/index.html', {'pto':blog})
#log
def log(request):
    if request.method =='POST':
        au = AuthenticationForm(request=request, data=request.POST)


    
        if au.is_valid():
            uname = au.cleaned_data['username']
            upass = au.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login (request, user)
        
            
                return HttpResponseRedirect('/main/profile/')
    else:
        au = AuthenticationForm()

    
    return render(request, 'folder/log.html', {'lg':au})
#om
def profile(request):
    return render(request, 'folder/profile.html')

