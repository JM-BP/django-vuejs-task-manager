from rest_framework import serializers
from .models import Board, List, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'list', 'created_at']

class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)  # 🔹 Incluir tareas en las listas

    class Meta:
        model = List
        fields = ['id', 'name', 'board', 'tasks', 'created_at']

class BoardSerializer(serializers.ModelSerializer):
    lists = ListSerializer(many=True, read_only=True)  # 🔹 Incluir listas en el tablero

    class Meta:
        model = Board
        fields = ['id', 'name', 'owner', 'lists', 'created_at']
