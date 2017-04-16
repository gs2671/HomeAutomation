from django import forms

class CommentForm(forms.Form):
    text=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Type your Comment'}), label='',required = False)

    
