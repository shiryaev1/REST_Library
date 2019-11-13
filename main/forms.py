from django import forms
from django.contrib.auth.models import User

from main.models import Book


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
        }


class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'content', 'author')

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write about it...'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write title...'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write author...'}),
        }

    def save(self, user):
        book = super(BookCreateForm, self).save(commit=False)
        book.owner = user
        book.save()

        return book