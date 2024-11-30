from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserManager(BaseUserManager):
    #overriding the create user method
    def create_user(self, username, email,password=None,**extra_field ):
        if username is None:
            raise TypeError("User should have valid username")
        if email is None:
            raise TypeError("There should be valid email address")

        user = self.model(username=username, email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username,email,password=None):
        if username is None:
            raise TypeError('User should have a valid username')
        if password is None:
            raise TypeError('User should not be none')
        if email is None:
            raise TypeError('User should have a valid Email')
        
    
        user=self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.role = MyUser.Role.ADMIN
        user.save(using=self._db)
        return user
    

#creating custom user
class MyUser(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"

    base_role= Role.STUDENT
    role=models.CharField(max_length=40, choices=Role.choices)
    username= models.CharField(max_length=40, unique=True)
    email= models.EmailField(max_length=225, unique=True,db_index=True )
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False) 
    created_at = models.TimeField(auto_now_add=True) #auto_now_add gives starting time
    updated_at = models.TimeField(auto_now=True)  #auto now gives updated time

    #taking email as username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    #telling how to manage the user to django
    objects= UserManager()
    
# Proxy models for specific roles
# Extend myuser to impose the role specific behaviour
class StudentManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role=MyUser.Role.STUDENT)

class Student(MyUser):
    base_role = MyUser.Role.STUDENT
    objects = StudentManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Welcome, Student!"

class TeacherManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role=MyUser.Role.TEACHER)

class Teacher(MyUser):
    base_role = MyUser.Role.TEACHER
    objects = TeacherManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Welcome, Teacher!"

# Signals to create profiles
# This is to store the addition information
# Signals automatically create profiles when a user with a specific role is created.

class StudentProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    student_id = models.IntegerField(null=True, blank=True)
    #we can add specific details 

@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.role == MyUser.Role.STUDENT:
        StudentProfile.objects.create(user=instance)

#similarly for teachers

class TeacherProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    teacher_id = models.IntegerField(null=True, blank=True)

@receiver(post_save, sender=Teacher)
def create_teacher_profile(sender, instance, created, **kwargs):
    if created and instance.role == MyUser.Role.TEACHER:
        TeacherProfile.objects.create(user=instance)