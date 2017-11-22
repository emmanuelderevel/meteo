from django.db import models
from django.contrib.auth.models import User

class Alert(models.Model):
    user_id = models.ForeignKey(User)
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=50, verbose_name="City Name")
    class Meta:
        unique_together = ["user_id", "city_id"]

    def __str__(self):
        city="City id : {0}".format(self.city_id)
        return city
