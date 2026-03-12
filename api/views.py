from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Routine
from .serializers import RoutineSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({"message" : "Welcome to Routine Api"})

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def routine_view(request):
    if request.method == 'GET':
        routines = Routine.objects.filter(user=request.user)
        serializer = RoutineSerializer(routines, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoutineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user= request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def routine_detail(request, pk):
    try:
        routine = Routine.objects.get(pk=pk, user=request.user)
    except Routine.DoesNotExist:
        return Response({"error": "Routine not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoutineSerializer(routine)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = RoutineSerializer(routine, data=request.data, partial=(request.method=='PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        routine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def all_routines(request):
        routines = Routine.objects.all()
        serializer = RoutineSerializer(routines, many=True)
        return Response(serializer.data)