# Student model ko JSON me convert karega

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:                                      #serializer configuration
        model = Student                              #Student model use karo
        fields = '__all__'                           #saare model fields include karo