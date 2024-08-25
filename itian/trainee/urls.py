from django.urls import path
from .views import *



urlpatterns = [

    path('', trainees_list, name='trainees_list'),
    path('Add/', trainee_create, name='trainee_create'),
    path('Update/<int:id>', account_update, name='trainee_update' ),
    path('Delete/<int:id>', account_delete, name='trainee_delete' ),
    path('Details/<int:id>', trainee_info, name='trainee_info')
]