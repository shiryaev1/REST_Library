from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View

from main.forms import UserForm, BookCreateForm
from main.models import Book


class UserListView(View):

    template_name = 'main/home.html'
    model = User

    def get(self, request):
        args = {
            'users': self.model.objects.all().order_by('-id'),
            'user_form': UserForm(),
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
        args = {
            'users': self.model.objects.all().order_by('-id'),
            'user_form': form,
        }
        return render(request, self.template_name, args)


class UserBookLibView(View):

    template_name = 'main/library.html'

    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except ObjectDoesNotExist:
            raise Http404
        args = {
            'user': user,
            'books': Book.objects.filter(owner=user),
            'book_form': BookCreateForm(),
        }
        return render(request, self.template_name, args)

    def post(self, request, id):
        try:
            user = User.objects.get(id=id)
        except ObjectDoesNotExist:
            return Http404
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save(user)
            form = BookCreateForm()
        args = {
            'user': user,
            'books': Book.objects.filter(owner=user),
            'book_form': form,
        }
        return render(request, self.template_name, args)


class BookEditView(View):

    template_name = 'main/book_edit.html'

    def get(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except ObjectDoesNotExist:
            raise Http404
        form = BookCreateForm(instance=book)
        args = {
            'book_form': form,
        }
        return render(request, self.template_name, args)

    def post(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except ObjectDoesNotExist:
            return Http404
        form = BookCreateForm(request.POST, instance=book)
        if form.is_valid():
            form.save(book.owner)
            return redirect('main:user-lib', id=book.owner_id)
        args = {
            'book_form': form
        }
        return render(request, self.template_name, args)