from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    # Input validation
    def validate_grade(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Grade must be between 0 and 100")
        return value