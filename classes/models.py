from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30)
    

class Lecture(models.Model):
    name = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE ,related_name="lectures")
    

    def __str__(self):
        return self.name


class Slide(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    Lecture = models.OneToOneField(Lecture , on_delete=models.CASCADE , related_name="slide", primary_key=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    Lecture = models.OneToOneField(Lecture , on_delete=models.CASCADE , related_name="slide", primary_key=True)
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course, on_delete=models.CASCADE ,related_name='tags')

    def __str__(self):
        return self.name
