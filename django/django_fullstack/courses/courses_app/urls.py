from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index),
    path('create_course' , views.create_course),
    path('courses/destroy/<int:id>' , views.view_course),
    path('destroy/<int:id>' , views.destroy_course),
    path('courses/comments/<int:id>' , views.view_comments , name="comments"),
    path('newcomment/<int:id>', views.create_comment)
]