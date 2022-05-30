from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('todo.urls') ),
    path('u/', include('django.contrib.auth.urls') ),
    path('admin/', admin.site.urls),
]
