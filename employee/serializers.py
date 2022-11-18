from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    position = serializers.CharField(max_length = 200)
    contact = serializers.CharField(max_length = 10)
    location = serializers.CharField(max_length = 200)
    salary = serializers.IntegerField()
    
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.position = validated_data.get('position', instance.position)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.location = validated_data.get('location', instance.location)
        instance.salary = validated_data.get('salary', instance.salary)
        