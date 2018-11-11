from django.db import models
# from django_mysql.models import JSONField


class Workout(models.Model):
    # lifts = JSONField()
    date = models.DateTimeField('date of workout')


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
