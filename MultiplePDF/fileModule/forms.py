from django import forms

class FileForm(forms.Form):
    files1 = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
