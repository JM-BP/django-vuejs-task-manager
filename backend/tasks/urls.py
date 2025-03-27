from django.urls import path
from .views import BoardListCreateView, BoardDetailView, ListListCreateView, ListDetailView, TaskListCreateView, TaskDetailView

urlpatterns = [
    # Endpoints para Tableros
    path('boards/', BoardListCreateView.as_view(), name='board-list-create'),
    path('boards/<int:pk>/', BoardDetailView.as_view(), name='board-detail'),
    
    # Endpoints para Listas
    path('lists/', ListListCreateView.as_view(), name='list-list-create'),
    path('lists/<int:pk>/', ListDetailView.as_view(), name='list-detail'),
    
    # Endpoints para Tareas
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
