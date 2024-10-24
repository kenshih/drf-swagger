from django.urls import path, include
from api import views
from api.viewsets import WorklistViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'worklists', WorklistViewSet, basename='worklist')

urlpatterns = [
    path('films/', views.FilmList.as_view()),
    path('worklists/', include(router.urls)),
]

