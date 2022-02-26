from django.urls import path,include
from app_one import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     
     path('', views.index, name='home'),
     path('contact', views.contactus, name='contact'),
     path('login', views.login, name='login'),
     path('addblog', views.add_blog, name='addblog'),
     path('logout', views.logout , name='logout'),
     path('post_delete/<int:id>', views.delete, name='delete_post' ),
     path('edit_or_updatepost/<int:id>', views.update_or_edit , name='edit_post' ),
     path('contact_message/<int:id>', views.contact_message_delete , name='delete_message' )

] +  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)