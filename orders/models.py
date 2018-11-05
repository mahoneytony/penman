# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Order(models.Model):
	number = models.AutoField(primary_key=True)
	subject = models.CharField(max_length=300, blank=True)
	topic = models.CharField(max_length=1000)
	create_date = models.DateTimeField(auto_now=True)