from rest_framework import serializers
from sms_app.models import Student, Teacher, Subject, Cls, Department, Assesment, Assignment

class TeacherSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Teacher
        fields = "__all__"
        
        
class SubjectSerializer(serializers.ModelSerializer):
    #module = TeacherSerializer(many=False, read_only=True)
    class Meta:
        model = Subject
        fields = "__all__"
        

class StudentSerializer(serializers.ModelSerializer):
   # module = ModuleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Student
        fields = "__all__"
        
        
class DepartmentSerializer(serializers.ModelSerializer):
   # module = ModuleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Department
        fields = "__all__"
        
class AssessmentSerializer(serializers.ModelSerializer):
   # module = ModuleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Assesment
        fields = "__all__"
        
class ClsSerializer(serializers.ModelSerializer):
   # module = ModuleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cls
        fields = "__all__"
        
class AssignmentSerializer(serializers.ModelSerializer):
   # module = ModuleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Assignment
        fields = "__all__"
        
