from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
from .models import Job
from .serializers import JobSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def jobs_api(request, id=None):
    if request.method == 'GET':
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'DELETE']:
        if id is None:
            return JsonResponse({"error": "ID is required for PUT and DELETE operations"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        try:
            job = Job.objects.get(id=id)
        except Job.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = JobSerializer(job, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            job.delete()
            return JsonResponse(status=status.HTTP_204_NO_CONTENT)