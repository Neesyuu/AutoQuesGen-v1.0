from django.contrib import admin
from django.urls import path
from T_register import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', views.tRegisterView, name='TRegisterView'),
    path('login', views.handleLogin, name='login'),
    path('logout', views.handleLogout, name='logout'),
    path('', views.handleHome, name='handleHome'),
    path('profile', views.profileTeacher, name='profileTeacher'),
    path('m_changepass', views.changePassword, name='changePasswordTeacher'),
    path('edit', views.editProfileTeacher, name='editProfileTeacher'),
    path('cs', views.cs, name='cs'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
