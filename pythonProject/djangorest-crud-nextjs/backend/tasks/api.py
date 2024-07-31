from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer 

    # Rutas personalizadas
    '''
    @action(detail=True, methods=['post'])
    def undo(self, request, pk=None):
        task = self.get_object()
        task.done = False
        task.save()
        return Response({'status': 'task marked as undone'})
    '''
    @action(detail=True, methods=['post'])
    def done(self, request, pk=None):
        task = self.get_object()
        task.done = not task.done
        task.save()
        return Response({
            'status': 'task marked as done' if task.done else 'task marked as undone'
            }, status=status.HTTP_200_OK)