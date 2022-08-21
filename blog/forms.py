from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    
    class Meta:
        model = Comment
        fields = ['name','email','body']


