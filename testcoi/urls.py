from django.contrib import admin
from django.urls import path
from coitask.views import DoctorApiList, SpecializationApiList, DoctorRetrieveView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctors/', DoctorApiList.as_view()),
    path('doctors/<int:pk>', DoctorRetrieveView.as_view()),
    path('specializations/', SpecializationApiList.as_view()),
]
