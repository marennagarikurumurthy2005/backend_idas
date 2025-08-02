from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', views.signup),
    path('api/signin/', views.signin),
    path('api/dashboard/', views.dashboard),
]
