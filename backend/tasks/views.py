from rest_framework import generics, permissions
from .models import Board, List, Task
from .serializers import BoardSerializer, ListSerializer, TaskSerializer

# ----- Vistas para Tableros -----
class BoardListCreateView(generics.ListCreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)  # Solo ver los tableros del usuario

    def perform_create(self, serializer):
        print("Usuario autenticado:", self.request.user)  # 👈 Verifica en la consola de Django
        serializer.save(owner=self.request.user)

class BoardDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)  # Solo acceder a los propios tableros


# ----- Vistas para Listas -----
class ListListCreateView(generics.ListCreateAPIView):
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        board_id = self.request.query_params.get('board', None)
        if board_id:
            return List.objects.filter(board__owner=self.request.user, board_id=board_id)
        return List.objects.filter(board__owner=self.request.user)

    def perform_create(self, serializer):
        board = serializer.validated_data['board']
        if board.owner != self.request.user:
            raise PermissionError("No tienes permiso para agregar listas a este tablero")
        serializer.save()


class ListDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return List.objects.filter(board__owner=self.request.user)


# ----- Vistas para Tareas -----
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        list_id = self.request.query_params.get('list', None)
        if list_id:
            return Task.objects.filter(list__board__owner=self.request.user, list_id=list_id)
        return Task.objects.filter(list__board__owner=self.request.user)

    def perform_create(self, serializer):
        task_list = serializer.validated_data['list']
        if task_list.board.owner != self.request.user:
            raise PermissionError("No tienes permiso para agregar tareas a esta lista")
        serializer.save()


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(list__board__owner=self.request.user)



'''
 curl -X POST http://127.0.0.1:8000/api/boards/ \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQzMTUyNTkwLCJpYXQiOjE3NDMxNTIyOTAsImp0aSI6ImE0NDkyMDEzYjI2ODQ2NDNiNTk3YzdhMWQzYTE5NTliIiwidXNlcl9pZCI6MX0.jv0AG_4uis0WAEHn7eY528vCsZlVujhcdWKGysx_oq0" \
     -H "Content-Type: application/json" \
     -d '{"name": "Nuevo Tablero"}'
{"owner":["This field is required."]}%  
'''
