from django import forms
from app.models import Comment , Subscribers


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['created_at','post']


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        exclude = ['created_at']        
  