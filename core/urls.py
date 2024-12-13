from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path("books/", views.books, name="books"),
    path("notes/", views.notes, name="notes"),
    path("notes-details/<int:pk>/", views.note_details, name="notedetails"),
    path("notes-delete/<int:pk>/", views.delete_note, name="notedelete"),
    path("homework/", views.homework, name="homework"),
    path("notes_update/<int:pk>/", views.update_note, name="noteupdate"),
    path("delete_homework/<int:pk>/", views.delete_homework, name="delete_homework"),
    path('todo/', views.todo, name='todo'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('update_todo/<int:pk>/',views.update_todo, name='update_todo'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('conversion/', views.conversion, name='conversion'),
    path('Wikipedia/', views.Wikipedia, name='Wikipedia'),
    path('youtube/', views.youtube, name='youtube'),
]