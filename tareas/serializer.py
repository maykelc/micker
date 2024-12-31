from rest_framework import serializers
from .models import Personal, Chamba, Document, Category, Skill, Task, Califications

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'

class ChambaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamba
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class CalificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Califications
        fields = '__all__'
