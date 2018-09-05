from django.db import models

class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_description = models.CharField(max_length=250)
    task_value = models.TextField()
    task_minAge = models.CharField(max_length=50)


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    person_first_name = models.CharField(max_length=100)
    person_last_name = models.CharField(max_length=100)
    person_parent = models.BooleanField(null=True)
    person_child = models.BooleanField(null=True)


class CompletedTasks(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.DO_NOTHING, related_name='completed_task_id')
    task_completed_by = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='completed_by_person_id')
    completed_date = models.DateField()
    completed_time = models.TimeField()
    task_approved_by = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='person_id_who_approved')




