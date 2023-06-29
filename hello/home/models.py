from django.db import models


# Create your models here.
class reel_entry(models.Model):
    
    reel_no = models.IntegerField(null=True)
    reel_gsm = models.IntegerField(null=True)
    reel_weight = models.IntegerField(null=True)
    reel_size = models.IntegerField(null=True)
    reel_rate = models.IntegerField( null=True)
    reel_mill = models.CharField(max_length=200,blank=True, null=True)
    reel_date= models.DateField(auto_now=True, null=True)
    reel_balance = models.IntegerField( null=True, default=0)
    reel_utilization = models.IntegerField( null=True, default=0)
    reel_waste = models.IntegerField( null=True, default=0)
    reel_amount = models.IntegerField( null=True, default=0)
    


    
class reel_transactions(models.Model):
    
    reel_no = models.IntegerField(null=True)
   
    reel_time_date= models.DateTimeField(auto_now=True,null=True)
    reel_old_balance = models.IntegerField( null=True, default=0)
    reel_new_balance = models.IntegerField( null=True, default=0)
    reel_old_utilization = models.IntegerField( null=True, default=0)
    reel_new_utilization = models.IntegerField( null=True, default=0)
    reel_old_waste = models.IntegerField( null=True, default=0)
    reel_new_waste = models.IntegerField( null=True, default=0)
    reel_old_amount = models.IntegerField( null=True, default=0)
    reel_new_amount = models.IntegerField( null=True, default=0)
    