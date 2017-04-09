from django import forms

class CommentForm(forms.Form):
    text=forms.CharField(label="Insert Comment", max_length=100 )
