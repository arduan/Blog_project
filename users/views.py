from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreatForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreatForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
