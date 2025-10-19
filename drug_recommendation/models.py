from django.db import models

class PatientDetails(models.Model):
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    disease = models.CharField(max_length=255)

    def __str__(self):
        return self.gender + ", " + str(self.age) + ", " + self.disease
