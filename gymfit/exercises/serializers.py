from rest_framework import serializers

from gymfit.exercises.models import Muscle, Equipment, Category, Exercise


class MuscleSerializer(serializers.ModelSerializer):
    """Muscle Serializer"""
    class Meta:
        model = Muscle


class EquipmentSerializer(serializers.ModelSerializer):
    """Equipment Serializer"""
    class Meta:
        model = Equipment


class CategorySerializer(serializers.ModelSerializer):
    """Category Serializer"""
    class Meta:
        model = Category


class ExerciseSerializer(serializers.ModelSerializer):
    """Exercise Serializer"""
    class Meta:
        model = Exercise
