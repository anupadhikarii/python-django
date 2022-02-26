from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from app_one.models import *
from django import forms

#---------------------------------------------------------------
#Using django Builtin Form for creating Loginform Template

class Adminlogin(AuthenticationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type':"username",
            'class':"input100",
            'name':'username',
            "placeholder":"username"
        })
        self.fields['password'].widget.attrs.update({
            'type':"password",
            'class':"input100",
            "placeholder":"password"
        })
  
    class Meta:
        model = User
        fields =  ['username', 'password']


#---------------------------------------------------------------

class AddBlog(forms.ModelForm):
    
    class Meta:
         model = Add_BlogModel
         fields ='__all__'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            "placeholder":"title"
        })

        self.fields['tags'].widget.attrs.update({
            "placeholder":"tags"
        })
        self.fields['image'].widget.attrs.update({
            "class":"form-control",        
            "placeholder":"file upload"

        })        
        self.fields['desc'].widget.attrs.update({
            "placeholder":"Desc", 
            "id":"" ,
            "cols":"300",
            "rows":"10"
        })
                
#---------------------------------------------------------------

class Contactus_form(forms.ModelForm):
    
    class Meta: 
         model = Contact
         fields ='__all__'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "placeholder":"name"
        })

        self.fields['email'].widget.attrs.update({
            "placeholder":"email"
        })
        self.fields['subject'].widget.attrs.update({
            "placeholder":"subject"
        })
        self.fields['number'].widget.attrs.update({
            "placeholder":"number"
        })       
        self.fields['message'].widget.attrs.update({
            "placeholder":"message", 
            "id":"" ,
            "cols":"300",
            "rows":"10"
        })
                   
                  