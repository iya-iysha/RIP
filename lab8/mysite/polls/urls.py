from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
]  
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)