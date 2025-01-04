from rest_framework import viewsets
from .models import Personal, Chamba, Document, Category, Skill, Task, Califications
from .serializers import PersonalSerializer, ChambaSerializer, DocumentSerializer, CategorySerializer, SkillSerializer, TaskSerializer, CalificationsSerializer
# ViewSets para cada modelo

class PersonalViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalSerializer
    queryset = Personal.objects.all()

class ChambaViewSet(viewsets.ModelViewSet):
    serializer_class = ChambaSerializer
    queryset = Chamba.objects.all()

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class CalificationsViewSet(viewsets.ModelViewSet):
    serializer_class = CalificationsSerializer
    queryset = Califications.objects.all()
