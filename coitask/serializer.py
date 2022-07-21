from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from datetime import date

from .models import *


class CatListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class ExperienceCalculator(serializers.Serializer):
    def to_representation(self, value):
        experience = date.today() - value
        return experience.days


class DoctorSerializer(serializers.ModelSerializer):
    cat = StringRelatedField(many=True)
    work_experience = ExperienceCalculator()

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'description', 'birthday', 'work_experience', 'cat')


class SpecializationSerializer(serializers.ModelSerializer):
    doctors = CatListingField(many=True, read_only=True)

    class Meta:
        model = Specialization
        fields = ('id', 'name', 'doctors')


