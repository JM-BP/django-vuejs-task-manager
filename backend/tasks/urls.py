from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BoardListCreateView, BoardDetailView, ListListCreateView, ListDetailView, TaskListCreateView, TaskDetailView

urlpatterns = [
    # Endpoints de autenticación con JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener token de acceso y refresh
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refrescar el token de acceso
    
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
