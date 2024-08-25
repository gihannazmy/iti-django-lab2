from django.urls import path
from .views import *


urlpatterns = [

    path('', tracks_list, name='tracks_list'),
    path('Add/', track_create, name='tracks_create'),
    path('Update/<int:id>', track_update, name='track_update' ),
    path('Delete/<int:id>', track_delete, name='track_delete' ),
    path("Details/<int:id>", track_detail, name="track_details")
]