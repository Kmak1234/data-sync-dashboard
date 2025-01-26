from django.db import models

# Create your models here.
class schemaData(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table: "schema1".data_tale
        managed = True

class Schema2Data(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    transferrred_at = models.DateField(auto_now_add=True)
    original_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'schema2'.data_table
        managed = True