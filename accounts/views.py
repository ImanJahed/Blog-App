
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import CustomUser
from .forms import CustomUserCreationForm

# Create your views here.
class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
