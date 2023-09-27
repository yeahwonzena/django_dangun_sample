from django import forms
from .models import Post


class CustomLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '아이디를 입력해주세요', 'class': 'login-input'}),
        label='아이디',
        label_suffix='', 
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력해주세요', 'class': 'login-input'}),
        label='비밀번호',
        label_suffix='', 
    )

class CustomRegistrationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '아이디를 입력해주세요', 'class': 'login-input'}),
        label='아이디',
        label_suffix='', 
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력해주세요', 'class': 'login-input'}),
        label='비밀번호',
        label_suffix='', 
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 다시 입력해주세요', 'class': 'login-input'}),
        label='비밀번호 확인',
        label_suffix='', 
    )
    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'price', 'description', 'location', 'images']