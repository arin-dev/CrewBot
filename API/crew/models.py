from django.db import models

# Create your models here.
class CrewMember(models.Model):
    name = models.CharField(max_length=100)
    userid = models.EmailField(unique=True)
    crewType = models.CharField(max_length=50)
    roleJobTitle = models.CharField(max_length=50)
    services = models.JSONField()
    tags = models.JSONField()
    expertise = models.JSONField()
    yoe = models.IntegerField()
    minRatePerDay = models.DecimalField(max_digits=6, decimal_places=2)
    maxRatePerDay = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    project_id = models.CharField(max_length=100, unique=True)
    project_detail_from_customer = models.TextField()
    detailed_desc = models.TextField()
    roleJobTitles = models.JSONField()
    crew_requirements = models.JSONField()
    queries = models.JSONField()
    selected_crews = models.JSONField()

    def __str__(self):
        return self.project_detail_from_customer