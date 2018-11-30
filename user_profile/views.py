from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from data.models import Data
from .models import User_Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

class ProfileList(LoginRequiredMixin,TemplateView):
    template_name='user_profile/user_profile_list.html'
    

    def get_context_data(self, **kwargs):
        context = super(ProfileList, self).get_context_data(**kwargs)
        try:
            context['user_profile'] = self.request.user.user_profile
        except User_Profile.DoesNotExist:
            pass
        return context
    
class ProfileCreate(LoginRequiredMixin,CreateView):
    model = User_Profile
    fields = ['image_profile','age','gender']
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        
        return super().form_valid(form)
    
class ProfileUpdate(LoginRequiredMixin,UpdateView):
    model = User_Profile
    fields = ['image_profile','age','gender']
    
class ProfileDelete(LoginRequiredMixin,DeleteView):
    model = User_Profile
    success_url = reverse_lazy('user_profile:base')