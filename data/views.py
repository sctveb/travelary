from django.shortcuts import render
from django.views.generic import ListView
from .models import Data
# Create your views here.\

class DataList(ListView):
    model = Data
    
    def get_queryset(self):
        data = Data.objects.filter(name=self.request.GET['name'])
        return data
        
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post_user'] = self.post_user 
    #     return context