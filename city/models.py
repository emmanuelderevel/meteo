from django.db import models
from django.contrib.auth.models import User

class Alert(models.Model):
    user_id = models.ForeignKey(User)
    city_id = models.IntegerField()

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        city="Village numéro {0}".format(self.city_id)
        return city
