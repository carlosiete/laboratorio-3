from django import forms
from apps.redsocial.models import usuario

class usuario_form(forms.ModelForm):

	class Meta:
		model = usuario

		fields = [
			'id_usuario',
			'nombre',
			'apellido',
			'sexo',
			'carrera',
			'promocion',
			'fecha_nacimiento',
			'correo',
			'telefono',
			'clave',
			'estatus',
			]
		labels = {
			'id_usuario': 'Nombre',
			'nombre': 'Sexo',
			'apellido': 'Apellido',
			'sexo': 'Sexo',
			'carrera': 'Carrera',
			'fecha_nacimiento': 'Fecha de nacimiento',
			'correo': 'Correo',
			'telefono': 'Telefono',
			'clave': 'Clave',		
		}
		widgets = {
			'id_usuario': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Cedula'}),
			'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
			'apellido': forms.TextInput(attrs={'class':'form-control','placeholder': 'Apellido'}),
			'sexo': forms.Select(attrs={'class':'form-control', 'placeholder': 'Sexo'}),
			'carrera': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Carrera'}),
			'promocion': forms.TextInput(attrs={'class':'form-control','placeholder': 'Promocion, ejemplo: 55'}),
			'fecha_nacimiento': forms.Select(attrs={'class':'form-control', 'placeholder': 'Fecha de nacimiento'}),
			'correo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Correo'}),
			'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefono'}),
			'clave': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Contraseña', 'type': 'password'}),		
		}