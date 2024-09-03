from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .forms import UserCreationForm, ContactForm
from .models import Contact
from django.views.generic.detail import DetailView
from .models import Contact
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import logout




class HomeView(TemplateView):
    template_name = 'users/home.html'

class ContactListView(ListView):
    model = Contact
    template_name = 'users/contact_list.html'
    context_object_name = 'contacts'

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'users/contact_form.html'
    success_url = reverse_lazy('contact-list')

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'users/edit_contact.html'
    success_url = reverse_lazy('contact-list')

class DeleteContactView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact-list')
    template_name = 'users/delete_contact.html'

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class addContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'users/add_contact.html'
    success_url = reverse_lazy('contact-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class editContactView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'users/edit_contact.html'  # Ujistěte se, že toto odpovídá umístění vaší šablony
    success_url = reverse_lazy('contact-list')

class contactDetailView(DetailView):
    model = Contact
    template_name = 'users/contact_detail.html'


class AboutView(TemplateView):
            template_name = 'users/about.html'

class PrivacyPolicyView(TemplateView):
    template_name = 'privacy_policy.html'


def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')
