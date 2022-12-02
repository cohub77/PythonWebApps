from django.contrib import admin
from django.urls import path, include


urlpatterns = [
# Photo
    path('photo/', include('photos.urls')),
    # Hero
    path('', include('hero.urls')),

    

    # Admin views for users
    # path('admin/', admin.site.urls),
    # path('admin/', include('admin.site.urls')),   Don't do this!

]
