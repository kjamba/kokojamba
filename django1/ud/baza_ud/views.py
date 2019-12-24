from django.shortcuts import render, redirect

from .models import Concert, Artist, Place, Staff
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ConcertForm, AuthUserForm, RegisterUserForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class HomeListView(ListView):
    model = Concert
    template_name = 'index.html'
    context_object_name = 'concert_list'

class HomeDetailView(DetailView):
    model = Concert
    template_name = 'detail.html'
    context_object_name = 'get_concert'

class CustomSuccessViewMixin:
    @property
    def success_msg(self):
        return False
    
    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)

class ConcertCreateView(LoginRequiredMixin, CustomSuccessViewMixin, CreateView):
    login_url = reverse_lazy('login_page')
    model = Concert
    template_name = 'edit_page.html'
    form_class = ConcertForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись создана'
    def get_context_data(self, **kwargs):
        kwargs['concert_list'] = Concert.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class ConcertUpdateView(LoginRequiredMixin, CustomSuccessViewMixin, UpdateView):
    model = Concert
    template_name = 'edit_page.html'
    form_class = ConcertForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись успешно обновлена'
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user !=  kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs

class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('edit_page')
    
    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Пользователь успешно создан' 

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid
        


class MyprojectLogout(LogoutView):
    next_page = reverse_lazy('edit_page')


class ConcertDeleteView(LoginRequiredMixin, DeleteView):
    model = Concert
    template_name = 'edit_page.html'
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись удалена'
    
    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


def query_page(request):
    template = 'query_page.html'
    context = {
    }
    return render(request, template, context)

def get_artist(request):
    template = 'artist.html'

    id1 = Artist.objects.order_by('last_name')
    id2 = Artist.objects.order_by('first_name')
    id3 = Artist.objects.order_by('middle_name')
    id4 = Artist.objects.order_by('nickname')
    id5 = Artist.objects.order_by('cost')

    context = {
        'id1': id1,
        'id2': id2,
        'id3': id3,
        'id4': id4,
        'id5': id5,
    }
    return render(request, template, context)

def get_place(request):
    id1 = Place.objects.order_by('name')
    id2 = Place.objects.order_by('address')
    id3 = Place.objects.order_by('capacity')
    id4 = Place.objects.order_by('cost')
    template = 'place.html'
    context = {
        'id1': id1,
        'id2': id2,
        'id3': id3,
        'id4': id4,
    }
    return render(request, template, context)

def get_staff(request):
    id1 = Staff.objects.order_by('last_name')
    id2 = Staff.objects.order_by('first_name')
    id3 = Staff.objects.order_by('middle_name')
    id4 = Staff.objects.order_by('address')
    # id5 = Staff.objects.filter().order_by('position')

    template = 'staff.html'

    context = {
        'id1': id1,
        'id2': id2,
        'id3': id3,
        'id4': id4,
        # 'id5': id5,
    }
    return render(request, template, context)


