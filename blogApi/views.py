from django.shortcuts import render
from .models import Blog
from .forms import *
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout


def blogList(request):
    blogs = Blog.objects.all().order_by('created_at')
    return render(request, 'bloglist.html', context={'data': blogs})


@login_required
def blogCreation(request):
    if request.method == 'POST':
        queryset = Blogform(request.POST, request.FILES)
        if queryset.is_valid():
            blog = queryset.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blogList')
    else:
        queryset = Blogform()
    return render(request, 'blogForm.html', context={'form': queryset})


@login_required
def blogUpdate(request, id):
    blog = get_object_or_404(Blog, id=id, user=request.user)
    if request.method == 'POST':
        form = Blogform(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogList')
    else:
        form = Blogform(instance=blog)
    return render(request, "blogForm.html", {'form': form})


@login_required
def blogDelete(request, id):
    queryset = get_object_or_404(Blog, id=id, user=request.user)
    if request.method == 'POST':
        queryset.delete()
        return redirect('blogList')
    return render(request, "blogDelete.html", {'data': queryset})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('blogList')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        queryset = UserRegistration(request.POST)
        if queryset.is_valid():
            user = queryset.save(commit=False)
            user.set_password(queryset.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('blogList')
    else:
        queryset = UserRegistration()

    return render(request, 'registration/register.html', {'form': queryset})


@login_required
def logout_confirmation(request):
    return render(request, 'registration/logout.html')


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required
def blogRead(request, id):
    queryset = get_object_or_404(Blog, id=id)
    print(id)
    return render(request, 'blogOpen.html', context={'form': queryset})


@login_required
def blogSearch(request):
    queryset = request.GET.get('q')
    if queryset:
        results = Blog.objects.filter(blog__icontains=queryset)
    else:
        results = Blog.objects.none()
    return render(request, 'blogSearch.html', context={'results': results, 'query': queryset})
