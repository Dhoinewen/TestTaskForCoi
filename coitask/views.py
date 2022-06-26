from django.utils import timezone
from datetime import timedelta
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializer import DoctorSerializer, CategorySerializer


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


class CategoryApiList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None