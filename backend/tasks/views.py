from rest_framework import generics
from .models import Board, List, Task
from .serializers import BoardSerializer, ListSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated

# Vistas de Tableros
'''
BoardListCreateView
    Vista para manejar las peticiones GET y POST para listar y crear tableros.
    Usa ListCreateAPIView que proporciona funcionalidades para listar y crear objetos.
'''
class BoardListCreateView(generics.ListCreateAPIView):             
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]


'''
BoardDetailView
    Vista para  manejar las peticiones GET, PUT/PATCH y DELETE para obtener, actualizar y eliminar un tablero en específico.
    Usa RetrieveUpdateDestroyAPIView para estas operaciones.
'''
class BoardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

#Vistas de Listas

'''
ListListCreateView
    Vista para manejar las peticiones GET y POST para listar y crear listas.
    Usa ListCreateAPIView que proporciona funcionalidades para listar y crear objetos.
'''
class ListListCreateView(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

'''
ListDetailView
    Vista para  manejar las peticiones GET, PUT/PATCH y DELETE para obtener, actualizar y eliminar una lista en específico.
    Usa RetrieveUpdateDestroyAPIView para estas operaciones.
'''
class ListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

# Vistas de Tareas
'''
TaskListCreateView
    Vista para manejar las peticiones GET y POST para listar y crear tareas.
    Usa ListCreateAPIView que proporciona funcionalidades para listar y crear objetos.
'''
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

'''
TaskDetailView
    Vista para  manejar las peticiones GET, PUT/PATCH y DELETE para obtener, actualizar y eliminar una tarea en específico.
    Usa RetrieveUpdateDestroyAPIView para estas operaciones.
'''
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

