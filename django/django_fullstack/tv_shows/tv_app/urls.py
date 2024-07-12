from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.pre_show),
    path('shows' , views.shows),
    path('shows/new' , views.new_show),
    path('shows/create_show' , views.create_show),
    path('shows/<int:id>' , views.show_info),
    path('shows/edit/<int:id>' , views.edit_show , name= 'edit_page'),
    path('shows/update_show/<int:id>' , views.update_show),
    path('shows/<int:id>/delete' , views.delete)
]