from rest_framework.response import Response

from sms_app.models import Student, Teacher, Cls, Subject, Assesment, Assignment, Department
from sms_app.api.serializers import TeacherSerializer, SubjectSerializer, StudentSerializer, DepartmentSerializer, AssessmentSerializer, AssignmentSerializer, ClsSerializer
from rest_framework import status
#from rest_framework.views import APIView
#from rest_framework import mixins
from rest_framework import generics
#from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from sms_app.utils import ResponseData
from rest_framework.permissions import IsAuthenticated



class StudentListCreate(generics.ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  # Define the serializer class attribute

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        
        # Manually fetch cls_grade based on cls value
        for student_data in serializer.data:
            cls_id = student_data["cls"]
            try:
                cls_instance = Cls.objects.get(pk=cls_id)
                student_data["cls_grade"] = cls_instance.cls_grade
                student_data.pop("cls", None)
            except Cls.DoesNotExist:
                student_data["cls_grade"] = "Unknown"  # Set default value if cls instance not found
        
        response_data = ResponseData.success(status.HTTP_200_OK, "Success", serializer.data)
        return Response(response_data)
    
    def create(self, request, *args, **kwargs):
        # Extract data from the request
        name = request.data.get('name')
        age = request.data.get('age')
        cls_grade = request.data.get('cls_grade')
        # Map cls_grade to the corresponding Cls object
        try:
            cls_instance = Cls.objects.get(cls_grade=cls_grade)
            #print(cls_instance)
        except Cls.DoesNotExist:
            return Response(
                {
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": f"Cls with grade '{cls_grade}' does not exist",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        # Create the student object
        student_data = {
            'name': name,
            'age': age,
            'cls': cls_instance.pk  # Set the cls field to the primary key of the Cls instance
        }
        serializer = self.get_serializer(data=student_data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "code": status.HTTP_201_CREATED,
                    "message": "Student created successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Failed to create student",
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()  # Retrieve the student instance
        serializer = self.get_serializer(instance)  # Serialize the student instance

        # Fetch cls_grade based on cls field
        cls_id = instance.cls_id
        try:
            cls_instance = Cls.objects.get(pk=cls_id)
            cls_grade = cls_instance.cls_grade
        except Cls.DoesNotExist:
            cls_grade = "Unknown"  # Set default value if cls instance not found

        # Add cls_grade to the serialized data
        serialized_data = serializer.data
        serialized_data.pop("cls", None)
        serialized_data['cls_grade'] = cls_grade
        
        response_data = {
            "code": 200,
            "message": "Success",
            "data": serialized_data,
        }
        return Response(response_data)
    
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # Retrieve the student instance
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Serialize the student instance with provided data
        if serializer.is_valid():
                    # Extract cls_grade from request data and map it to corresponding Cls object
            cls_grade = request.data.get('cls_grade')
            if cls_grade:
                try:
                    cls_instance = Cls.objects.get(cls_grade=cls_grade)
                except Cls.DoesNotExist:
                    return Response(
                        {"message": f"Cls with grade '{cls_grade}' does not exist"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                serializer.validated_data['cls'] = cls_instance  # Set cls field in serializer

           # if serializer.is_valid():
                serializer.save()  # Save the serializer
                response_data = {
                            "code": 200,
                            "message": "Success",
                            "data": serializer.data,
        }
                return Response(response_data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, *args, **kwargs):
            instance = self.get_object()  # Retrieve the subj instance
            instance.delete()  # Delete the subj instance
            response_data = ResponseData.success(status.HTTP_204_NO_CONTENT, "Student deleted successfully")
            return Response(response_data)    

class clsListCreate(generics.ListCreateAPIView):
    queryset = Cls.objects.all()
    serializer_class = ClsSerializer  # Define the serializer class attribute
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        
        response_data = {
            "code": 200,
            "message": "Success",
            "data": serializer.data,
        }
        return Response(response_data)
    
class clsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cls.objects.all()
    serializer_class = ClsSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()  # Retrieve the student instance
        serializer = self.get_serializer(instance)  # Serialize the student instance
        
        response_data = {
                "code": 200,
                "message": "Success",
                "data": serializer.data,
            }
        return Response(response_data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # Retrieve the student instance
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Serialize the student instance with provided data
        if serializer.is_valid():
            serializer.save()
        
        
        response_data = {
                "code": status.HTTP_200_OK,
                "message": "Success",
                "data": serializer.data,
            }
        
        return Response(response_data)
    
    def delete(self, request, *args, **kwargs):
            instance = self.get_object()  # Retrieve the instance
            instance.delete()  # Delete the  instance
            response_data = {
                "code": status.HTTP_200_OK,
                "message": "Deleted successfully",
                #"data": serializer.data,
            }
            return Response(response_data)
    
        
class subjListCreate(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
                # Manually fetch cls_grade based on cls value
        for data in serializer.data:
            cls_id = data["cls"]
            teacher_id = data["teacher"]
            try:
                cls_instance = Cls.objects.get(pk=cls_id)
                teacher_instance = Teacher.objects.get(pk=teacher_id)
                
                data["cls_grade"] = cls_instance.cls_grade
                data["teacher_name"] = teacher_instance.name
                
                data.pop("cls", None)
                data.pop("teacher", None)
            except Cls.DoesNotExist:
                data["cls_grade"] = "Unknown"
                data["teacher_name"] = "Unknown" # Set default value if cls instance not found
        
        response_data = ResponseData.success(status.HTTP_200_OK, "Success", serializer.data)
        return Response(response_data)
        
    def create(self, request, *args, **kwargs):
        # Extract data from the request
        subj_name = request.data.get('subj_name')
        subj_duration = request.data.get('subj_duration')
        cls_grade = request.data.get('cls_grade')
        teacher_name = request.data.get('teacher_name')
        
        # Map cls_grade to the corresponding Cls object
        try:
            cls_instance = Cls.objects.get(cls_grade=cls_grade)
            teacher_instance = Teacher.objects.get(name=teacher_name)
            
            print(cls_instance)
            print(teacher_instance)
        except Cls.DoesNotExist:
            response_data = ResponseData.error(status.HTTP_400_BAD_REQUEST, f"Cls with grade '{cls_grade}' does not exist")
            return Response(response_data)
         
        except Teacher.DoesNotExist:
            response_data = ResponseData.error(status.HTTP_400_BAD_REQUEST, f"the teacher name '{teacher_name}' does not exist")
            return Response(response_data)

        
        # Create the subj object
        subj_data = {
            'subj_name': subj_name,
            'subj_duration': subj_duration,
            'cls': cls_instance.pk, # Set the cls field to the primary key of the Cls instance
            'teacher': teacher_instance.pk
        }
        serializer = self.get_serializer(data=subj_data)
        if serializer.is_valid():
            serializer.save()
            
            response_data = ResponseData.success(status.HTTP_201_CREATED, "Student created successfully", serializer.data)
            return Response(response_data)

        else:
            response_data = ResponseData.error(status.HTTP_400_BAD_REQUEST, "Failed to create student")
            return Response(response_data)

class subjDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()  # Retrieve the subj instance
        serializer = self.get_serializer(instance)  # Serialize the subj instance

        # Fetch cls_grade based on cls field
        cls_id = instance.cls_id
        teacher_id = instance.teacher_id
        try:
            cls_instance = Cls.objects.get(pk=cls_id)
            teacher_instance = Teacher.objects.get(pk=teacher_id)
            cls_grade = cls_instance.cls_grade
            teacher_name =teacher_instance.name
        except Cls.DoesNotExist:
            cls_grade = "Unknown"
            teacher_name = "Unknown"     # Set default value if cls instance not found

        # Add cls_grade to the serialized data
        serialized_data = serializer.data
        serialized_data.pop("cls", None)
        serialized_data.pop("teacher", None)
        serialized_data['cls_grade'] = cls_grade
        serialized_data['teacher_name'] =teacher_name
        
        response_data = ResponseData.success(status.HTTP_200_OK, "Success", serialized_data)
        return Response(response_data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # Retrieve the student instance
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Serialize the student instance with provided data
        if serializer.is_valid():
                    # Extract cls_grade from request data and map it to corresponding Cls object
            cls_grade = request.data.get('cls_grade')
            teacher_name = request.data.get('teacher_name')
            if cls_grade and teacher_name:
                try:
                    cls_instance = Cls.objects.get(cls_grade=cls_grade)
                    teacher_instance = Teacher.objects.get(name=teacher_name)
                    
                except Cls.DoesNotExist:
                    return Response(
                        {"message": f"Cls with grade '{cls_grade}' does not exist"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                except Teacher.DoesNotExist:
                    return Response(
                        {"message": f"the teacher '{teacher_instance}' does not exist"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                serializer.validated_data['cls'] = cls_instance  # Set cls field in serializer
                serializer.validated_data['teacher'] = teacher_instance
           # if serializer.is_valid():
                serializer.save()  # Save the serializer
                response_data = ResponseData.success(status.HTTP_200_OK, "Success", serializer.data)
                return Response(response_data)

        else:
            response_data = ResponseData.error(status.HTTP_400_BAD_REQUEST, "Failure")
            return Response(response_data)
        
    def delete(self, request, *args, **kwargs):
            instance = self.get_object()  # Retrieve the subj instance
            instance.delete()  # Delete the subj instance
            response_data = ResponseData.success(status.HTTP_204_NO_CONTENT, "Subject deleted successfully")
            return Response(response_data)            
    
class deptListCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class deptDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer   
        
class teacherListCreate(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
class teacherDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer  
        
class assessmentListCreate(generics.ListCreateAPIView):
    queryset = Assesment.objects.all()
    serializer_class = AssessmentSerializer
     
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        
        for assessment_data in serializer.data:
            subj_id = assessment_data["assessment_subj"]
            print(subj_id)
            try:
                assignment_instance = Subject.objects.get(pk=subj_id)
                assessment_data["subj_name"] = assignment_instance.subj_name
                assessment_data.pop("assessment_subj", None)
            except Assesment.DoesNotExist:
                assessment_data["assessment_subj"] = "Unknown"  # Set default value if cls instance not found
        
        response_data = ResponseData.success(status.HTTP_200_OK, "Success", serializer.data)
        return Response(response_data)  
    

class assessmentDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Assesment.objects.all()
    serializer_class = AssessmentSerializer 

    
    
class assignmentListCreate(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        
        for assignment_data in serializer.data:
            subj_id = assignment_data["assignment_subj"]
            print(subj_id)
            try:
                assignment_instance = Subject.objects.get(pk=subj_id)
                assignment_data["subj_name"] = assignment_instance.subj_name
                assignment_data.pop("assignment_subj", None)
            except Assesment.DoesNotExist:
                assignment_data["assignment_subj"] = "Unknown"  # Set default value if cls instance not found
        
        response_data = ResponseData.success(status.HTTP_200_OK, "Success", serializer.data)
        return Response(response_data)    
    

class assignmentDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

      
