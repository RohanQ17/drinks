from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    contactEmail = models.EmailField()
    contactPhone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Job(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')

    def __str__(self):
        return self.title