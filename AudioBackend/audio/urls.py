from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('song',views.song_api)

urlpatterns = [
    path('',include(router.urls))

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)