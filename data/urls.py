from django.urls import path
from . import views
app_name="data"

urlpatterns = [
    path('',views.DataList.as_view(),name='list'),
    path('<int:pk>/', views.DataDetail.as_view(), name='detail'),
]