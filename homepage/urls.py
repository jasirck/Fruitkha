from django.urls import path
from homepage import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('homepage',views.homepage,name='homepage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)