from django.db import models

#-------------------------------------------------------------------------
#Contact table in database which stores message from viewers to admin

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    number = models.IntegerField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name

#---------------------------------------------------------------
#Addblog table in database which stores Blog added by admin

class Add_BlogModel(models.Model):

    title = models.CharField(max_length=50)   
    tags = models.CharField(max_length=80)   
    desc = models.TextField(max_length=8000)   
    image = models.ImageField( upload_to='my image/%y/%m/%d')   
    date = models.DateField(auto_now_add=True)
    
     
    def __str__(self):
        return self.title