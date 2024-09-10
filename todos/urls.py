from django.urls import path
from .views import TodoCreateView, TodoUpdateView, IndexView

app_name = 'todos'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # List todos
    path('todos/add/', TodoCreateView.as_view(), name='add_todo'),  # Add todo
    path('todos/<int:todo_id>/update/', TodoUpdateView.as_view(), name='update_todo'),  # Update todo
    path('todos/<int:todo_id>/delete/', TodoUpdateView.as_view(), name='delete_todo'),  # Delete todo
]
