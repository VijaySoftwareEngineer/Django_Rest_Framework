from rest_framework import serializers
from .models import Student
    
class StudentSerializer(serializers.ModelSerializer):
        # validator
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should be start with R')
    name = serializers.CharField(validators = [start_with_r])   
    
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
      

# field level validation:
    def validate_roll(self, value):
        if value >= 100:
            raise serializers.ValidationError('Seat Full')
        return value
    
# object level validation:
    def validate(self, data):
        nm = data.gat('name')
        ct = data.get('city')
        if nm.lower() == 'veer' and ct.lower() != 'Haryana':
            raise serializers.ValidationError('City must be ranchi')
        return data
