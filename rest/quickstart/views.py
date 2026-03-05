from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# @api_view(['GET'])
# def student_list(request):
#     students = Student.objects.all()                      #Database se data fetch.
#     serializer = StudentSerializer(students, many=True)   #Data ko JSON me convert.
#     return Response(serializer.data)                      #JSON data ko response me bhej do.


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()                      #Database se data fetch.
        serializer = StudentSerializer(students, many=True)   #Data ko JSON me convert.
        return Response(serializer.data)                      #JSON data ko response me bhej do.

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)     #JSON data ko serializer ke through validate karo
        if serializer.is_valid():                             #Data valid hai ya nahi check karo.
            serializer.save()                                  #Data ko database me save karo.
            return Response(serializer.data, status=201)      #Saved data ko response me bhej do.
        return Response(serializer.errors, status=400)       #Agar data valid nahi hai to error message bhej do.  
    
@api_view(['GET','PUT','DELETE'])
def student_detail(request, pk):                             #Yaha pk URL se aata hai.

    student = Student.objects.get(id=pk)                     #Student table me id = pk wala record fetch karo

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    elif request.method == 'PUT':

        serializer = StudentSerializer(student, data=request.data)    #Existing student ko new data se update karo

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response({'message': 'Student deleted successfully'})


