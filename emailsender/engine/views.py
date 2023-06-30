from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView
from .models import *


class CreateMessage(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = 'engine.add_sender'
    model = Sender
    template_name = 'email_create.html'
    fields = ['title', 'content', 'emails']
    success_url = reverse_lazy('list')


class ListMessage(ListView):
    model = Sender
    ordering = 'datetime'
    template_name = 'email_list.html'
    context_object_name = 'email_list'
