from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from PIL import Image
# Create your models here.

class UserManager(BaseUserManager):
    #overriding the create user method
    def create_user(self, username, email,password=None,**extra_field ):
        if username is None:
            raise TypeError("There should be valid username")
        
        if email is None:
            raise TypeError("There should be valid email address")

        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,email, username ,password=None):
        if username is None:
            raise TypeError('User should have a valid username')
        if password is None:
            raise TypeError('User should not be none')
        if email is None:
            raise TypeError('User should have a valid Email')
        
    
        user=self.create_user( username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.role = MyUser.Role.ADMIN
        user.save(using=self._db)
        return user
    

#creating custom user
class MyUser(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        DOCTOR = "DOCTOR", "Doctor"
        PATIENT = "PATIENT", "Patient"

    profilepicture= models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    role=models.CharField(max_length=40, choices=Role.choices, default=Role.PATIENT)
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
    

        # if self.profile_picture:
        #     img = Image.open(self.profile_picture.path)

        #     # Resize image if it's larger than the desired dimensions
        #     max_width, max_height = 300, 300
        #     if img.height > max_height or img.width > max_width:
        #         output_size = (max_width, max_height)
        #         img.thumbnail(output_size)
        #         img.save(self.profile_picture.path)
    #telling how to manage the user to django
    objects= UserManager()
    
