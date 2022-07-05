from rest_framework import serializers
from .models import *


class CatListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class DoctorSerializer(serializers.ModelSerializer):
    cat = CatListingField(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'description', 'birthday', 'work_experience', 'cat')


class SpecializationSerializer(serializers.ModelSerializer):
    doctors = CatListingField(many=True, read_only=True)

    class Meta:
        model = Specialization
        fields = ('id', 'name', 'doctors')


