from django.db import models


class Policeorders(models.Model):
    orderid = models.AutoField(primary_key=True)
    crimeid = models.IntegerField()
    originalcrimetypename = models.CharField(max_length=128, blank=True, null=True)
    reportdate = models.DateTimeField(blank=True, null=True)
    calldate = models.DateTimeField(blank=True, null=True)
    offensedate = models.DateTimeField(blank=True, null=True)
    calltime = models.TimeField(blank=True, null=True)
    calldatetime = models.DateTimeField(blank=True, null=True)
    disposition = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    state = models.CharField(max_length=8, blank=True, null=True)
    agencyid = models.IntegerField(blank=True, null=True)
    addresstype = models.CharField(max_length=64, blank=True, null=True)
    commonlocation = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'policeorders'
