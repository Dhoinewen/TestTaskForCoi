from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_doctors(self):
        return ",".join([str(p) for p in self.doctors.all()])

    class Meta():
        verbose_name = 'Doctor specialization'
        verbose_name_plural = 'Doctor specialization'


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    birthday = models.DateField()
    work_experience = models.DateField()
    cat = models.ManyToManyField(Specialization, blank=True, related_name='doctors')

    def get_cat(self):
        return ",".join([str(p) for p in self.cat.all()])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['birthday']
