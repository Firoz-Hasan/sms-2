from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=150)
    description  = models.CharField(max_length=150)
    contact_email  = models.CharField(max_length=150)
    phone_number  = models.CharField(max_length=150)
    #module_taught  = models.OneToManyField(Module)
    
    def __str__(self):
        return self.dept_name    
    
class Teacher(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    edu_level  = models.CharField(max_length=150)
    #module_taught  = models.OneToManyField(Module)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teacher_list')
    
    def __str__(self):
        return self.name
    

class Cls(models.Model):
    cls_grade = models.CharField(max_length=150)
    cls_section  = models.CharField(max_length=150)
    #subjects  = models.ManyToManyField(Subject)
    #modules = models.ForeignKey(Module, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cls_grade
    
class Subject(models.Model):
    subj_name = models.CharField(max_length=30)
    subj_duration = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='modules_taught')
    cls = models.ForeignKey(Cls, on_delete=models.CASCADE, related_name='cls_subj')
    
    def __str__(self):
        return self.subj_name

    
        
class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    cls = models.ForeignKey(Cls, on_delete=models.CASCADE, related_name='cls_enrol')
    
    def __str__(self):
        return self.name
    
class Assesment(models.Model):
    ass_name = models.CharField(max_length=150)
    ass_percentage  = models.CharField(max_length=150)
    assessment_subj = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='ass_subj_name')
    
    #subjects  = models.ManyToManyField(Subject)
    #modules = models.ForeignKey(Module, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ass_name    
    
class Assignment(models.Model):
    assign_name = models.CharField(max_length=150)
    assign_percentage  = models.CharField(max_length=150)
    assignment_subj = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='assignment_subj_name')
    
        #subjects  = models.ManyToManyField(Subject)
        #modules = models.ForeignKey(Module, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.assign_name  
