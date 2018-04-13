from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers

from .forms import *
from .models import *

# Create your views here.
def vista_about(request):
	return render(request, 'about.html')

def vista_motos(request):
	motos = ['ktm', 'kawasaki', 'yamaha', 'suzuki']
	diccionario = {'moto':motos}
	return render(request, 'about1.html', diccionario)

def vista_empresas(request):
	empresas = ["exito", 'coca cola', 'google','php']
	diccionario ={'nombre':empresas}
	return render(request, 'empresas.html', diccionario)

def vista_empleado(request):
	persona = ['luis', 'carlos', 'juan', 'luisa']
	diccionario = {'Nombre':persona}
	return render(request, 'empleados.html', diccionario)

def vista_contacto(request):
	info_enviado = False
	email = " "
	subject = " "
	text = " "
	if request.method == "POST":
		formulario= contacto_form(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['correo']
			subject = formulario.cleaned_data['tema']
			text = formulario.cleaned_data['texto']
			return render(request, 'contacto.html', locals())
	else:

		formulario = contacto_form()
	return render(request, 'contacto.html', locals())
		
def vista_formulario(request):
	datos_recibidos = False
	name = ""
	age = ""
	fn = ""
	phone = ""
	Forever = ""
	sex = ""
	user = ""
	password = ""
	email = ""
	if request.method == "POST":
		taller= formulario_form(request.POST)
		if taller.is_valid():
			datos_recibidos = True
			name = taller.cleaned_data['nombre']
			age = taller.cleaned_data['edad']
			fn = taller.cleaned_data['fecha_nacimiento']
			phone = taller.cleaned_data['celular']
			Forever = taller.cleaned_data['Forever_Alone']
			sex = taller.cleaned_data['sexo']
			user = taller.cleaned_data['usuario']
			password = taller.cleaned_data['contraseña']
			email = taller.cleaned_data['correo']
			return render(request, 'formulario.html', locals())
	else:
		taller = formulario_form()
	return render(request, 'formulario.html', locals())



def vista_lista_producto(request):
	lista= Producto.objects.filter()
	return render(request, 'lista_producto.html', locals())

def vista_lista_categoria(request):
	lista2= Categoria.objects.filter()
	return render(request, 'lista_categoria.html', locals())

def vista_lista_marca(request):
	lista3= Marca.objects.filter()
	return render(request, 'lista_marca.html', locals())
#--------AGREGAR--------#
def vista_agregar_producto(request):
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect('/lista_producto/')
	else:
		formulario = agregar_producto_form()
	return render(request, 'vista_agregar_producto.html', locals())
#------------EDITAR-------3
def vista_editar_producto(request, id_prod):
	prod = Producto.objects.get(id=id_prod)
	if request.method == "POST":
		formulario = agregar_producto_form(request.POST, request.FILES, instance=prod)
		if formulario.is_valid():
			prod = formulario.save()
			return redirect('/lista_producto/')
	else:
		formulario = agregar_producto_form(instance= prod)
	return render(request, 'vista_agregar_producto.html', locals())
#--------------ELIMINAR-------#
def vista_eliminar_producto(request, id_prod):
		prod = Producto.objects.get(id=id_prod)
		prod.delete()
		return redirect ('/lista_producto/')


#-------------------07/03/2018----------------#


def vista_ver_producto(request, id_prod):
	p = Producto.objects.get(id=id_prod)
	return render(request, 'ver_producto.html', locals())

def vista_administracion(request):
	return render(request, 'administracion.html')

def vista_agregar_categoria(request):
	if request.method == 'POST':
		formulario = agregar_categoria_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect('/lista_categoria/')
	else:
		formulario = agregar_producto_form()
	return render(request, 'vista_agregar_producto.html', locals())

#____________21/03/2018______________________#

def vista_login(request):
	usu = ""
	cla = ""
	if request.method == "POST":
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/administracion/')
			else:
				msj = "usuario o clave incorrectos"
	formulario = login_form()
	return render(request, 'login.html', locals())
def vista_logout(request):
	logout(request)
	return redirect('/login/')
#______________________04/04/2018___________#

def vista_registrar(request):
	form = registrar_form()
	if request.method == "POST":
		form = registrar_form(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			correo = form.cleaned_data['email']
			password_1 = form.cleaned_data['password_1']
			password_2 = form.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario, email=correo, password= password_1)
			u.save()
			return render(request, 'registro_exitoso.html', locals())
	else:
		return render(request, 'registrar.html', locals())
	return render(request, 'registrar.html', locals())
#------------------11/04/2018-------#

def ws_productos_vista(request):
	data = serializers.serialize('json',Producto.objects.filter(status = True))
	return HttpResponse(data, content_type= 'application/json')
	
def vista_base(request):
	User.objects.filter()
	return render(request, 'base.html', locals())