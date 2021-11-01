from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentView.as_view(template_name='profile.html'), name='form'),
    path('delete/<int:id>/', views.delete_data.as_view(), name='delete'),
    path('<int:id>/', views.update_data.as_view(), name='update'),



]
