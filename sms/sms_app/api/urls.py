from django.urls import path,include
from .views import (StudentListCreate, StudentDetail, clsListCreate, 
clsDetail, subjListCreate, deptListCreate, deptDetail, subjDetail, teacherListCreate, teacherDetail,
assessmentListCreate, assessmentDetail, assignmentListCreate, assignmentDetail)

urlpatterns = [
    path('api/student', StudentListCreate.as_view(), name='student-list-create'),
    path('api/student/detail/<int:pk>', StudentDetail.as_view(), name='student-detail-update'),
   # path('api/grade/delete/<int:pk>', GradeDelete.as_view(), name='grade-delete'),
   
    path('api/class', clsListCreate.as_view(), name='cls-list-create'),
    path('api/class/detail/<int:pk>', clsDetail.as_view(), name='cls-list-create'),
   
    path('api/subject', subjListCreate.as_view(), name='subj-list-create'),
    path('api/subject/detail/<int:pk>', subjDetail.as_view(), name='subj-list-create'),
   
   
    path('api/department', deptListCreate.as_view(), name='dept-list-create'),
    path('api/department/detail/<int:pk>', deptDetail.as_view(), name='dept-list-create'),
   
    path('api/teacher', teacherListCreate.as_view(), name='teacher-list-create'),
    path('api/teacher/detail/<int:pk>', teacherDetail.as_view(), name='teacher-list-create'),
   
    path('api/assignment', assignmentListCreate.as_view(), name='assignment-list-create'),
    path('api/assignment/detail/<int:pk>', assignmentDetail.as_view(), name='assignment-list-create'),
   
    path('api/assessment', assessmentListCreate.as_view(), name='assessment-list-create'),
    path('api/assessment/detail/<int:pk>', assessmentDetail.as_view(), name='assessment-list-create'),
   
]

