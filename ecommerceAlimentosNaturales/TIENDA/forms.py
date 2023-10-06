from django import forms
from .models import Producto, Categoria, Carrito

class FormProducto(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ("titulo",'imagen', "descripcion",  'precio', 'categoria')
        widgets = {
            
            'titulo': forms.TextInput(attrs={'class': 'pub_titulo'}),
            'descripcion': forms.Textarea(attrs={'class': 'pub_contenido'}),
            'imagen': forms.FileInput(attrs={'name':'imagen_adjunta', 'class': 'pub_imagen'}),
        }

