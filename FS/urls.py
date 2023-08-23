from django.contrib import admin
from django.urls import path,include
from SharingApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
          path('admin/', admin.site.urls),
          path('',views.register,name='register'),
          path('login',views.login,name='login'),
          path('forgot-password',views.For,name='forgot-password'),
          path('home/<i>',views.home,name='home'),
        path('logout',views.logout,name='logout'),
        path('fileupload/<i>',views.fileupload,name='fileupload'),
        path('seefile/<i>',views.seefile,name='seefile'),
        path('delete/<i>',views.delete,name='delete'),
         path('accounts/', include('allauth.urls')),
         path('logout', LogoutView.as_view()),
        

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
