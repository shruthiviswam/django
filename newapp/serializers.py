from rest_framework import serializers
from . import models

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        fields=('id','name','address')
        model=models.StudentAPI