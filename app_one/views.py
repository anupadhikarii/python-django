from django.contrib import auth
from django.shortcuts import render,HttpResponseRedirect, redirect
from app_one.models import *
from app_one.forms import AddBlog,Contactus_form,Adminlogin
from django.contrib import messages
from app_one.messaging import *



#---------------------------------------------------------------
#homepage 
#Here most of data from Database is Retrive

def index(request):

    form_addblog = AddBlog()
    form_contact = Contactus_form()
    blogs = Add_BlogModel.objects.all()
    message_send_by_viewers = Contact.objects.all()
   
    dic = {'form_addblog':form_addblog, 'form_contactus':form_contact, 'blogs':blogs, 'messages_to_admin':message_send_by_viewers}
   
    return render(request, 'home.html', dic)

#---------------------------------------------------------------
#Contant Form to message Admin/Blogger of website, and it is only visible to admin
#It is displayed on leftside as card after you login  with admin credentials 

def contactus(request):
    if request.method == 'POST':

        #email = request.POST['email']
        #name = request.POST['name']
        #thanks_for_contacting_message(email,name)    #-----> 'Thanks for contacting message' used by importing SendGrid module on messaging.py file 
        #commentout to use it and add your email and Api key on messaging.py file
       
        fm = Contactus_form(data = request.POST)

        if fm.is_valid():
           
           fm.save()
           messages.success(request, 'message  Sent Sucessfuly')
        
        else :
        
            messages.error(request,' Message failed to send')  
    
    return HttpResponseRedirect('/')



#---------------------------------------------------------------
#login functionality , Message popups in screen 'login as admin?' or login through 127.0.0.1:8000/login  to authenticate as admin
#username--> admin , password----> !@#$%^&*

def login(request):
  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
  
        if user is not None:
            
            auth.login(request, user)
            return redirect('/')
  
        else :
  
                messages.error(request,'Username and Password did not match')  
                return redirect('login')
  
    else:

         form = Adminlogin()
  
    dic = {'form':form}
    return render(request, 'login.html', dic)

#---------------------------------------------------------------
#logout as Admin

def logout(request):
    
    auth.logout(request)
    return HttpResponseRedirect('/')    


#---------------------------------------------------------------
#adding Blogs

def add_blog(request):

    if request.user.is_authenticated:


        if request.method == 'POST':
        
            fm = AddBlog(data = request.POST, files = request.FILES)

            if fm.is_valid():

                fm.save()
                messages.success(request, 'Blog added Sucessfuly')

            else :

                messages.error(request, 'ERROR ..fill EveryFields and do not use SVG image')
        
        return HttpResponseRedirect('/')

    else:

        return HttpResponseRedirect('/')



#---------------------------------------------------------------
#editing blogs 

def update_or_edit(request, id):
    
    if request.user.is_authenticated:

        if request.method == 'POST':
        
            post_to_edit = Add_BlogModel.objects.get(pk=id)
            edit_complete = AddBlog(request.POST , request.FILES ,instance= post_to_edit)
        
            if edit_complete.is_valid():
            
                edit_complete.save()
                messages.success(request, 'edited sucessfully')
            
                return HttpResponseRedirect('/')     
        
        else:

            post_to_edit = Add_BlogModel.objects.get(pk=id)            
            form_addblog = AddBlog(instance=post_to_edit)

        return render(request, 'editpage.html', {'form_addblog':form_addblog})
   
    else:
   
        return HttpResponseRedirect('/')

#---------------------------------------------------------------
#deleting Blog 

def delete(request, id):

    if request.user.is_authenticated:
  
        blog_to_delete = Add_BlogModel.objects.get(pk=id)
        blog_to_delete.delete()
        messages.success(request, 'Deleted Sucessfully')
        
        return HttpResponseRedirect('/')
    
    else:
       
        return HttpResponseRedirect('/')

#---------------------------------------------------------------
#deleting message after reading it

def contact_message_delete(request,id):

    if request.user.is_authenticated:
    
        contact_message_to_delete = Contact.objects.get(pk=id)
        contact_message_to_delete.delete()
        messages.success(request, 'Message delete sucessfully')

        return HttpResponseRedirect('/')

    else:

        return HttpResponseRedirect('/')
