from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # this import the assets file for css

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('account/', include('account.urls')),
]

urlpatterns += staticfiles_urlpatterns() # Appending our static files to the url patterns