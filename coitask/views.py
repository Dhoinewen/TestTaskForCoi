from django.utils import timezone
from datetime import timedelta
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializer import DoctorSerializer, SpecializationSerializer


class DoctorApiListPagination(PageNumberPagination):
    page_size = 2


class DoctorRetrieveView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorApiList(generics.ListAPIView):
    serializer_class = DoctorSerializer
    pagination_class = DoctorApiListPagination

    def get_queryset(self):
        queryset = Doctor.objects.order_by('id')
        params = self.request.query_params

        category = params.get('category', None)
        work_experience = params.get('work_experience', None)
        sorted_by = params.get('sorted_by', None)

        if category:
            queryset = Doctor.objects.filter(cat__name=category)

        if work_experience:
            queryset = Doctor.objects.filter(work_experience__lte=timezone.now()-timedelta(days=int(work_experience)))

        if sorted_by:
            queryset = Doctor.objects.order_by(sorted_by)

        return queryset


class SpecializationApiList(generics.ListCreateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    pagination_class = None