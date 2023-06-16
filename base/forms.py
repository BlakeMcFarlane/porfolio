from django import forms

class Contact(forms.Form):
    name=forms.CharField(max_length=40,widget=forms.TextInput(
        attrs={
            'class': 'input-class',
            'placeholder':"Name",
        }
    ))
    email=forms.CharField(max_length=80,widget=forms.TextInput(
        attrs={
        'class':'input-class',
        'placeholder':"Email",
    }))
    subject=forms.CharField(max_length=500,widget=forms.TextInput(
        attrs={
        'class':'input-class',
        'placeholder':"Subject",
        'style':'height:200px'
    }))
