from django.shortcuts import render
from django.contrib.auth.models import User
from notes.serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import NotesDb,TaskDb
from .serializers import NotesSerializer,TaskSerializer
from rest_framework.authtoken.models import Token

# Create your views here.
class RegisterationView(APIView):
    def post(self, request):
        serializer_instance = RegisterSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data={"message": "User created successfully"})
        else:
            return Response(data=serializer_instance.errors)


class NotesListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notes = NotesDb.objects.filter(user=request.user)
        serializer_instance = NotesSerializer(notes, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        serializer_instance = NotesSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(
                data={"message": "Note created successfully"},
                status=201
            )
        else:
            return Response(
                data=serializer_instance.errors,
                status=400
            )


class NotesRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return NotesDb.objects.get(pk=pk, user=self.request.user)
        except NotesDb.DoesNotExist:
            return None

    def get(self, request, pk):
        note = self.get_object(pk)

        if note is not None:
            serializer_instance = NotesSerializer(note)
            return Response(serializer_instance.data)

        return Response(
            data={"error": "Note not found"},
            status=404
        )

    def put(self, request, pk):
        note = self.get_object(pk)

        if note is not None:
            serializer_instance = NotesSerializer(note, data=request.data)

            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(
                    data={"message": "Note updated successfully"}
                )

            return Response(
                data=serializer_instance.errors,
                status=400
            )

        return Response(
            data={"error": "Note not found"},
            status=404
        )

    def delete(self, request, pk):
        note = self.get_object(pk)

        if note is not None:
            note.delete()
            return Response(
                data={"message": "Note deleted successfully"}
            )

        return Response(
            data={"error": "Note not found"},
            status=404
        )


class NotesRetrieveUpdateDeleteView(APIView):
    permission_class = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return NotesDb.objects.get(pk=pk, user=self.request.user)
        except NotesDb.DoesNotExist:
            return None

    def get(self, request, pk):
        note = self.get_object(pk)
        if note is not None:
            serializer_instance = NotesSerializer(note)
            return Response(serializer_instance.data)
        else:
            return Response(data={"error": "Note not found"}, status=404)

    def put(self, request, pk):
        note = self.get_object(pk)
        if note is not None:
            serializer_instance = NotesSerializer(note, data=request.data)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(data={"message": "Note updated successfully"})
            else:
                return Response(data=serializer_instance.errors)
        else:
            return Response(data={"error": "Note not found"}, status=404)

    def delete(self, request, pk):
        note = self.get_object(pk)
        if note is not None:
            note.delete()
            return Response(data={"message": "Note deleted successfully"})
        else:
            return Response(data={"error": "Note not found"}, status=404)

class LogoutView(APIView):
    permission_class = [IsAuthenticated]


class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        task = TaskDb.objects.filter(user=request.user)
        serializer_instance = TaskSerializer(task, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        serializer_instance = TaskSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(data={"message": "Note created successfully"})
        else:
            return Response(data=serializer_instance.errors)


class TaskRetrieveUpdateDeleteView(APIView):
    permission_class = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return TaskDb.objects.get(pk=pk, user=self.request.user)
        except TaskDb.DoesNotExist:
            return None

    def get(self, request, pk):
        task = self.get_object(pk)
        if task is not None:
            serializer_instance = TaskSerializer(task)
            return Response(serializer_instance.data)
        else:
            return Response(data={"error": "task not found"}, status=404)

    def put(self, request, pk):
        task = self.get_object(pk)
        if task is not None:
            serializer_instance = TaskSerializer(task, data=request.data)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(data={"message": "Task updated successfully"})
            else:
                return Response(data=serializer_instance.errors)
        else:
            return Response(data={"error": "Task not found"}, status=404)

    def delete(self, request, pk):
        task = self.get_object(pk)
        if task is not None:
            task.delete()
            return Response(data={"message": "Task deleted successfully"})
        else:
            return Response(data={"error": "Task not found"}, status=404)
