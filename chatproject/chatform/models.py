from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Experience(models.Model):
    jobid = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name ="exp")
    exp = models.CharField(max_length=200)
    def __str__(self):
        return self.exp

class Gender(models.Model):
    jobid = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name ="gender")
    gen = models.CharField(max_length=200)
    def __str__(self):
        return self.gen

class Skills(models.Model):
    jobid = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name ="skills")
    skill = models.CharField(max_length=200)
    def __str__(self):
        return self.skill