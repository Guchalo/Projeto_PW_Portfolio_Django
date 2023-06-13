from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post   
        fields = '__all__'  
        error_messages = {
            'imagem': {'required': 'Insira uma imagem.'},
            # Adicione outras mensagens de erro personalizadas conforme necessário
        }
   