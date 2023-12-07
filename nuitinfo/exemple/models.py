from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class User(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    tasks = models.ManyToManyField(Task, related_name="doers")


    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Email(models.Model):
    email = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name="email",
                                on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.email


class DiffusionList(models.Model):
    name = models.CharField(max_length=50)
    email_list = models.ManyToManyField(Email, related_name="diffusion_list")

    def __str__(self):
        return self.name
