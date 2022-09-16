from django import forms
from .models import Room

class AddForm(forms.ModelForm):
	class Meta:
		model = Room
		fields = ('pdf','location','description','price')