from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=23234232)
    first_name = models.CharField(max_length=23234232)
    last_name = models.CharField(max_length=23234232)
    email = models.CharField(max_length=23234232)


    def __str__(self):
        return self.name

class Header(models.Model):
    logo=models.ImageField(upload_to="logo",blank=False)
    main_body_img=models.ImageField(upload_to="images",blank=False)
    title_body=models.CharField(max_length=256,blank=False)
    title_icon=models.ImageField(upload_to="icons",blank=False)
    trending_title=models.CharField(max_length=20,blank=True)
    trending_image=models.ImageField(upload_to="trending",blank=True)
    trending_discription=models.CharField(max_length=100,blank=True)

    def __str(self):
        return self.title_body

class Acheivement(models.Model):
    Total_no_of_client=models.IntegerField(blank=False)
    Trusted=models.IntegerField(blank=False)
    Locations=models.IntegerField(blank=False)
    Consulting_services=models.IntegerField(blank=False)

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject=models.CharField(max_length=200)
    message = models.TextField()
class Train(models.Model):
    topic=models.CharField(max_length=400)
    date=models.DateField()
    time =models.TimeField()
    meeting_number=models.IntegerField(blank=False)
    password=models.CharField(max_length=500,blank=False)
    user_name=models.ForeignKey('auth.User',on_delete=models.CASCADE)
class Join(models.Model):
    first_name = models.CharField(max_length=200)
    last_name =models.CharField(max_length=200)
    Email=models.EmailField()
    current_job_title =models.CharField(max_length=200)
    contact_number = models.IntegerField()
    Intrested =models.TextField()
