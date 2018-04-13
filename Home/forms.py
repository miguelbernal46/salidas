from django import forms
from .models import *
from django.contrib.auth.models import User

class contacto_form(forms.Form):
	correo = forms.EmailField(widget=forms.TextInput())
	tema = forms.CharField(widget=forms.TextInput())
	texto = forms.CharField(widget=forms.Textarea())

class formulario_form(forms.Form):
	nombres = forms.CharField(widget=forms.TextInput())
	edad = forms.IntegerField(min_value=0,max_value = 100, widget=forms.NumberInput())
	Fecha_Nacimiento = forms.SplitDateTimeField(widget=forms.SelectDateWidget())
	celular = forms.IntegerField(max_value =99999999999999, widget=forms.TextInput())
	#sexo = forms.extend([('a',1),('b',2),('c',3)])
	Forever_Alone = forms.BooleanField()
	usuario = forms.CharField(widget=forms.TextInput())
	clave = forms.CharField(widget=forms.PasswordInput())
	correo = forms.EmailField(widget=forms.TextInput())

class agregar_producto_form(forms.ModelForm):
	class Meta:
		model = Producto
		fields= '__all__'
class agregar_categoria_form(forms.ModelForm):
	class Meta:
		model = Categoria
		fields= '__all__'
class login_form(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput())
	clave = forms.CharField(widget=forms.PasswordInput(render_value=False))





class registrar_form(forms.Form):
	username = forms.CharField(label= "Nombre de usuario", widget=forms.TextInput())
	email = forms.EmailField(label= "Correo electronico", widget= forms.TextInput())
	password_1 = forms.CharField(label= "Password", widget=forms.PasswordInput(render_value=False))
	password_2 =  forms.CharField(label= "Confirmar", widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
			raise forms.ValidationError('nombre de usuario ya existe')

	def clean_email(self):
		email=self.cleaned_data['email']
		try:
			u=User.objects.get(email=email)
		except User.DoesNotExist:
			return email
			raise forms.ValidationError('email')

	def clean_password_2(self):
		password_1 = self.cleaned_data['password_1']
		password_2 = self.cleaned_data['password_2']

		if password_1 == password_2:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')
