from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.pre_show),
    path('shows' , views.shows),
    path('shows/new' , views.new_show),
    path('shows/create_show' , views.create_show),
    path('shows/<int:id>' , views.show_info),
    path('shows/<int:id>/edit' , views.edit_show),
    path('shows/<int:id>/update_show' , views.update_show),
    path('shows/<int:id>/delete' , views.delete)
]