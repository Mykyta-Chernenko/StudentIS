# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify


class Student(models.Model):
    student_card_id = models.CharField(max_length=15)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='student_images')
    date_of_birth = models.DateField()
    student_group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Студент: {self.name} {self.surname} {self.patronymic}'

class Group(models.Model):
    name = models.CharField(max_length=15)
    head = models.OneToOneField('Student', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def slug(self):
        return slugify(f'{self.name}')

    def __str__(self):
        return f'Группа {self.name}'
