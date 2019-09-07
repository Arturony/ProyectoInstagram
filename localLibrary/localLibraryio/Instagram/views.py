from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Instagram.models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login
from django.conf import settings

# Create your views here.
def index(request):

    if request.user.is_authenticated:
       return redirect('home')
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        name = request.POST['nombre']
        username = request.POST['usuario']
        email = request.POST['correo']
        password = request.POST['password']
        usuarioDjango = User.objects.create_user(username = username, password = password, email = email, first_name = name)
        miUsuario = MiUsuario(usuario_django = usuarioDjango)
        usuarioDjango.save()
        miUsuario.save()
        miUsuario = authenticate(request, username=username, password=password)
        if miUsuario is not None:
            login(request, miUsuario)
            return redirect ('usimg')


@login_required
def home(request):
    usuario_actual = MiUsuario.objects.get(pk = request.user.pk)
    curr_user = request.user
    post_user = Post.objects.filter(user_id = curr_user.id)
    context = { 'mis_fotos' : post_user, 'usuario' : curr_user, 'usuario_actual' : usuario_actual}
    return render(request, 'home.html', context)

@login_required
def profile(request):
    curr_user = request.user
    mi_usuario = MiUsuario.objects.get( pk = request.user.pk )
    post_user = Post.objects.filter(user_id = curr_user.id)
    context = { 'usuario_actual' : mi_usuario, 'post_user':post_user }
    return render(request, 'profile.html', context)

@login_required
def galeria(request):
    usuario_actual = MiUsuario.objects.get(pk = request.user.pk)
    curr_user = request.user
    context = {'usuario' : curr_user, 'usuario_actual' : usuario_actual}
    if request.method == 'GET':
        return render(request, 'galeria.html', context)
    else:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        curr_user = request.user;
        cantidad_post = Post.objects.filter(user_id = curr_user.id).count()
        name = curr_user.username + '-' + str(cantidad_post)
        filename = fs.save(name, photo)
        path = fs.url(filename)
        descripcion = request.POST['descripcion']
        mi_curr_user = MiUsuario(pk = curr_user.pk)
        newPost = Post ( photo= path, descripcion= descripcion, user_id = mi_curr_user)
        newPost.save()
        return redirect('profile')


def usimg(request):
    usuario_actual = MiUsuario.objects.get(pk = request.user.pk)
    curr_user = request.user
    context = {'usuario' : curr_user, 'usuario_actual' : usuario_actual}
    if request.method == 'GET':
        return render(request, 'usimg.html', context)
    else:
        usuario_actual = MiUsuario.objects.get(pk = request.user.pk)
        curr_user = request.user
        user_photo = request.FILES['user_photo']
        fs = FileSystemStorage()
        curr_user = request.user;
        name ='profile/'+ curr_user.username + '-' + str("porfile_photo")
        filename = fs.save(name, user_photo)
        path = fs.url(filename)
        mi_usuario = MiUsuario.objects.get( pk = request.user.pk )
        usuario_actual.foto = path
        usuario_actual.save()
        print(usuario_actual.foto)
        return redirect('home')

def opciones(request):
    usuario_actual = MiUsuario.objects.get(pk = request.user.pk)
    curr_user = request.user
    context = {'usuario' : curr_user, 'usuario_actual' : usuario_actual}
    if request.method == 'GET':
        return render(request, 'opciones.html', context)
    else:
        usuario_actual = MiUsuario.objects.get(pk = request.user.pk)
        curr_user = request.user
        context = {'usuario' : curr_user, 'usuario_actual' : usuario_actual}
        user_photo = request.FILES['user_photo']
        fs = FileSystemStorage()
        curr_user = request.user;
        name ='profile/'+ curr_user.username + '-' + str("porfile_photo")
        filename = fs.save(name, user_photo)
        path = fs.url(filename)
        usuario_actual.foto = path
        mi_usuario = MiUsuario.objects.get( pk = request.user.pk )
        if fs.exists(path) == True:
            fs.delete(path)
            usuario_actual.save()
            print (usuario_actual.foto)
            return redirect('opciones')
        else:
            usuario_actual.save()
            print (usuario_actual)
            return redirect('opciones')
