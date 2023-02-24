from functools import partial

from django.db import models

# Create your models here.

CharField256 = partial(models.CharField, max_length=256, null=True)


class FormModel(models.Model):
    linkedin_profile = CharField256()
    company_name = CharField256()
    employment_location = CharField256()
    employment_situation = CharField256()
    salary_range = CharField256()
    offer_text = models.TextField()
    display_salary = models.BooleanField(null=True)
    g_token = models.TextField()
