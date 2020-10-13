from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import HealthCareUserCreationForm, HealthCareUserChangeForm


class HealthCareUserCreateView(CreateView):
    
    template_name = 'signup.html'
    form_class = HealthCareUserCreationForm
    success_url = reverse_lazy('home')
