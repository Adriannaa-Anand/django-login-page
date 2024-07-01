from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login', permanent=False)),  # Redirect root to login
    path('register/', include('login_app.urls')),  # Include myapp URLs
    path('login/', include('login_app.urls')),
    path('logout/', include('login_app.urls')),
    path('home/', include('login_app.urls')),
]
