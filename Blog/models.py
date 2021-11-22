from django.db import models


# Create your models here.

class Blogs(models.Model):
    Id =models.AutoField(primary_key=True)
    Blog_title =models.CharField( max_length=30)
    catogery =(
        ("python",'Python'),
        ("C++","C++"),
        ("Java","Java"),
        ("JavaScript","JavaScript"),
        ("Php","Php"),
        ("C","C")
    )
    Blog_catogery=models.CharField(max_length=30,choices=catogery)
    Blog_desc=models.TextField(max_length=100)
    Blog_detail_desc=models.TextField(max_length=2000)

    def __str__(self):
        return str(self.Id)
    
class USER_Data(models.Model):
    Id =models.AutoField(primary_key=True)
    Username =models.CharField(max_length=20)
    Email =models.EmailField()
    Password =models.CharField(max_length=20)


    def __str__(self):
        return str(self.Id)    


    
class Message(models.Model):
    firstname =models.CharField(max_length=20)
    lastname =models.CharField(max_length=20)
    Country =models.CharField(max_length=20)
    message =models.TextField(max_length=500)


    def __str__(self):
        return self.firstname          
