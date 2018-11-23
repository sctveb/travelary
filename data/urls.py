from django.urls import path
from . import views
app_name="data"

urlpatterns = [
    path('',views.DataList.as_view(),name='list')    
]