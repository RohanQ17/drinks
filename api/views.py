from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def jobs_api(request, id=None):
    if request.method == 'GET':
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response({"jobs": serializer.data})

    elif request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'DELETE']:
        if id is None:
            return Response({"error": "ID is required for PUT and DELETE operations"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        try:
            job = Job.objects.get(id=id)
        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = JobSerializer(job, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            job.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)