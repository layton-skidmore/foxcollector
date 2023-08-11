from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

HABITATS = (
    ('F', 'Forest'),
    ('A', 'Arctic Tundra'),
    ('D', 'Desert')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Fox(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'fox_id': self.id})

class Habitats(models.Model):
    date = models.DateField('date discovered')
    habitat = models.CharField(
        max_length=1,
        choices=HABITATS,
        default=HABITATS[0][0]
    )

    fox = models.ForeignKey(Fox, on_delete=models.CASCADE, default=2) 

    class Meta:
        verbose_name_plural = "Habitats"  # Specify the plural name for the admin interface

    def __str__(self):
        return f"{self.get_habitat_display()} on {self.date}"