from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PersonalViewSet, ChambaViewSet, DocumentViewSet,
    CategoryViewSet, SkillViewSet, TaskViewSet, CalificationsViewSet
)

# Crear el router
router = DefaultRouter()

# Registrar los ViewSets
router.register(r'personal', PersonalViewSet, basename='personal')
router.register(r'chamba', ChambaViewSet, basename='chamba')
router.register(r'documents', DocumentViewSet, basename='documents')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'skills', SkillViewSet, basename='skills')
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'califications', CalificationsViewSet, basename='califications')

# Definir las rutas
urlpatterns = [
    path('api/v1/', include(router.urls)),  # Todas las rutas del router estarán bajo el prefijo "api/v1/"
]
