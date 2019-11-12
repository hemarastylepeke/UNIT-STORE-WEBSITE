from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('upload/', views.upload_book, name='upload_book'),
]
# To serve the files locally on the machine:
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
