from django import forms

class ArchivoForm(forms.Form):
    archivos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
