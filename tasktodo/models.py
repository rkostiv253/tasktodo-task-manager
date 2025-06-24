from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="workers"
    )

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return self.username


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    STATUS_CHOICES = (
        (True, "Completed"),
        (False, "In progress")
    )
    deadline = models.DateTimeField()
    status = models.BooleanField(choices=STATUS_CHOICES, default=False)
    URGENT = "UR"
    HIGH = "HI"
    MEDIUM = "ME"
    LOW = "LO"
    PRIORITY_CHOICES = [
        (URGENT, "Urgent"),
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "LOW"),
    ]
    priority = models.CharField(
        max_length=2,
        choices=PRIORITY_CHOICES,
        default=MEDIUM,
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="tasks"
    )
    workers = models.ManyToManyField(Worker, related_name="tasks")

    class Meta:
        ordering = ("-priority", "-status", "name",)

    def clean(self):
        if self.deadline < timezone.now():
            raise ValidationError("Deadline cannot be in the past.")

    def __str__(self):
        return f"{self.name}, {self.description}"
