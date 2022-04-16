from django.db import models
from django.db.models import (CharField, DecimalField,
                              BigIntegerField, DateTimeField,
                              PositiveSmallIntegerField, BooleanField, FileField)

class BaseModel(models.Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        default_permissions = ()
        
# Create your models here.
class TimestampRequest(BaseModel):
    system_code  = PositiveSmallIntegerField()
    file_id = BigIntegerField()
    pdf_file=FileField( blank=True)
    status_cd = PositiveSmallIntegerField()


# class TimestampVerificationRequest(models.Model):

