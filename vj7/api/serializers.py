from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # for multiple field we get readoly so to write:
        read_only_field = ['name', 'roll',]
        # or we can write property also form this way below:
        # extra_kwargs = {'name':{'read_only':True}}