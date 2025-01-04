from rest_framework import serializers
from .models import Personal, Chamba, Document, Category, Skill, Task, Califications
from django.core.exceptions import MultipleObjectsReturned



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
    categoria = CategorySerializer(read_only=True)

    class Meta:
        model = Skill
        fields = '__all__'


class PersonalSerializer(serializers.ModelSerializer):
    tipo_empleado = ChambaSerializer()

    class Meta:
        model = Personal
        fields = '__all__'

    def validate_correo(self, value):
        if self.instance:
            if Personal.objects.filter(correo=value).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("Este correo ya está registrado.")
        else:
            if Personal.objects.filter(correo=value).exists():
                raise serializers.ValidationError("Este correo ya está registrado.")
        return value

    def create(self, validated_data):
        tipo_empleado_data = validated_data.pop('tipo_empleado', None)
        print(tipo_empleado_data)
        if tipo_empleado_data:
            try:
                # Intenta buscar o crear el registro
                tipo_empleado, created = Chamba.objects.get_or_create(**tipo_empleado_data)
                print(tipo_empleado)
            except MultipleObjectsReturned:
                # Si hay múltiples registros, toma el primero disponible
                tipo_empleado = Chamba.objects.filter(**tipo_empleado_data).first()
                created = False
        else:
            tipo_empleado = None

        # Crea el objeto Personal
        personal = Personal.objects.create(tipo_empleado=tipo_empleado, **validated_data)
        print(personal)
        return personal

    def update(self, instance, validated_data):
        tipo_empleado_data = validated_data.pop('tipo_empleado', None)

        if tipo_empleado_data:
            try:
                tipo_empleado, created = Chamba.objects.get_or_create(**tipo_empleado_data)
            except MultipleObjectsReturned:
                tipo_empleado = Chamba.objects.filter(**tipo_empleado_data).first()
                created = False

            instance.tipo_empleado = tipo_empleado

        return super().update(instance, validated_data)


class TaskSerializer(serializers.ModelSerializer):
    created_by = PersonalSerializer(read_only=True)
    assigned_to = PersonalSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class CalificationsSerializer(serializers.ModelSerializer):
    calificador = PersonalSerializer(read_only=True)
    calificado = PersonalSerializer(read_only=True)

    class Meta:
        model = Califications
        fields = '__all__'
