from typing import ParamSpec
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from Auth_app.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from Auth_app.models import CustomUser, User_More_info
from django.contrib.auth import login, logout, authenticate, user_logged_in
from django.contrib.auth.decorators import login_required
from Post_app.models import Post
from Auth_app.models import Follow

# Create your views here.

def Register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        
        if CustomUser.objects.filter(email=email).exists():
            return redirect('Auth_app:register')
        
        if CustomUser.objects.filter(username=username).exists():
            return redirect('Auth_app:register')
        
        user = CustomUser(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            dob = dob,
            gender = gender
            
        )
        user.set_password(password)
        user.save()
        return redirect('Auth_app:login')
        
        
    context = {
        
    }
    return render(request, 'Auth_app/register.html', context)

def Login_page(request):
    context={
        'title':'user | login | page'
    }
    return render(request, 'Auth_app/login.html')

def Do_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        
        user = EmailBackEnd.authenticate(request, username=email, password=password)
        
        if user !=None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email and password are not same!')
            return redirect('Auth_app:login')
        
    else:
        messages.error(request, 'Email and password are not same!')
        return redirect('Auth_app:login')
   
@login_required
def Do_logout(request):
    logout(request)
    return redirect('Auth_app:login') 


@login_required
def Profile(request, id):
    user = CustomUser.objects.get(id=id)
    user_morinfo = User_More_info.objects.filter(user=request.user.id)
    if request.method == 'POST':
        image = request.FILES.get('image')
        caption = request.POST.get('caption')
        post = Post(
            image = image,
            caption = caption
        )
        post.author = request.user
        post.save()
    context = {
        'user':user,
        'user_morinfo':user_morinfo
    }       
    return render(request, 'Auth_app/profile.html', context)
@login_required
def Update_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        user_id = request.POST.get('id')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')
        cover_pic = request.FILES.get('cover_pic')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        
        user = CustomUser.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.dob = dob
        
        if password !=None and password !='':
            user.set_password(password)
            
        if profile_pic !=None and profile_pic !='':
            user.prfole_pic = profile_pic
            
        if cover_pic !=None and cover_pic !='':
            user.cover_pic = cover_pic
            
        if gender !=None and gender !='':
            user.gender = gender
        
        user.save()
        messages.success(request,'Profile SUccessfully Updated')
        return HttpResponseRedirect(reverse('Auth_app:profile', kwargs={'id':user_id}))
        # return HttpResponseRedirect(reverse('Auth_app:profile', kwargs={'id':id}))
                    
        
    return render(request, 'Auth_app/profile.html')

@login_required
def Add_more(request):
    if request.method == 'POST':
        work = request.POST.get('work')
        study = request.POST.get('study')
        live_in = request.POST.get('live_in')
        bio = request.POST.get('bio')
        user_id = request.POST.get('id')
        # username = request.POST.get('username')
        # if work !=None and work !='':
        #     user = User_More_info.objects.filter(user=request.user.id)
        #     user.work = work
        #     user.study = study
        #     user.live_in = live_in
        #     user.bio = bio
        # else:
        user = User_More_info(
            work = work,
            study = study,
            live_in = live_in,
            bio = bio,
        )
        user.user = request.user
        user.save()
        return HttpResponseRedirect(reverse('Auth_app:profile', kwargs={'id':user_id}))
    return render(request, 'Auth_app/profile.html')
@login_required
def Update_more(request):
    if request.method == 'POST':
        work = request.POST.get('work')
        study = request.POST.get('study')
        live_in = request.POST.get('live_in')
        bio = request.POST.get('bio')
        user_id = request.POST.get('id')

        user = User_More_info.objects.get(id=user_id)
        user.work = work
        user.study = study
        user.live_in = live_in
        user.bio = bio
        user.user = request.user
        user.save()
        return HttpResponseRedirect(reverse('Auth_app:profile', kwargs={'id':request.user.id}))
        
    return render(request, 'Auth_app/profile.html')

@login_required
def Other_userprofile(request, username):
    User_data = CustomUser.objects.get(username=username)
    Already_followed = Follow.objects.filter(Follower=request.user, Following=User_data)
    if User_data == request.user:
        return HttpResponseRedirect(reverse('Auth_app:profile', kwargs={'id':request.user.id}))
    context = {
        'User_data':User_data,
        'Already_followed':Already_followed
    }
    return render(request, 'Auth_app/Other_user.html', context=context)

@login_required
def Follow_user(request, username):
    following_user = CustomUser.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(Follower=follower_user, Following=following_user)
    if not already_followed:
        follow = Follow(Follower=follower_user, Following=following_user)
        follow.save()
        return HttpResponseRedirect(reverse('Auth_app:other_user', kwargs={'username':username}))
def Unfollow_user(request, username):
    following_user = CustomUser.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(Follower=follower_user, Following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('Auth_app:other_user', kwargs={'username':username}))