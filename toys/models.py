from django.db import models

class Toy(models.Model):
    # o django adiciona automaticamente a PK
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=250, blank=False, default='')
    toy_category = models.CharField(max_length=200, blank=False, default='')
    release_date = models.DateTimeField()
    was_included_in_home = models.BooleanField(blank=False)
    teste = models.CharField(max_length=10)

    # estabelece um padrão de ordenacao pelo nome
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

