from django import forms
from .models import Post

class PostUpdateForm(forms.ModelForm):
    favorited_weight = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '10'}), required=True) 
    retweeted_weight = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '10'}), required=True)
    commented_weight = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '10'}), required=True)
    is_followed_weight = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '10'}), required=True)
    thumbnail = forms.ImageField(label='サムネ',widget=forms.ClearableFileInput(attrs={'onchange': 'previewImage(this);'},))
    class Meta:
        model = Post
        fields = ('title', 'description', 'tags', 'thumbnail', 'tweeturl', 'favorited_weight', 'retweeted_weight', 'commented_weight', 'is_followed_weight', 'content','is_public', 'ended_at')
