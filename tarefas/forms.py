from django import forms
from .models import Tarefa



class TarefaForms(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('nome', 'is_active',)