from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name="data"

urlpatterns = [
    path('',views.DataList.as_view(),name='list'),
    path('<int:pk>/', views.DataDetail.as_view(), name='detail'),
    path('<int:data_id>/reviewcreate/<int:user_id>', views.ReviewCreate.as_view(), name='reviewcreate'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
