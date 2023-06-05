from django.db import models

# Create your models here.


class Block(models.Model):
    block_number = models.CharField(max_length=200,unique=True)
    varient = models.CharField(max_length=300,blank=True,null=True)
    bench_number = models.BigIntegerField(blank=True,null=True)
    name_of_person = models.CharField(max_length=300,blank=True,null=True)
    block_picture = models.ImageField(upload_to="uploads/block", blank=True,null=True)
    block_length = models.FloatField()
    block_height = models.FloatField()
    block_width = models.FloatField()
    actual_weight = models.FloatField(default=0)
    cbm = models.FloatField(default=0)
    measurement_weight = models.FloatField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)



    class Meta:
        db_table = 'blocks'


    def __str__(self):
        return str(self.block_number)