from django.db import models


class Developer(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='name')
    last_name = models.CharField(max_length=60, verbose_name='family')
    email = models.EmailField()
    age = models.IntegerField()

    class Meta:
        db_table = 'developers'
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.id}_{self.first_name} {self.last_name}"


class Skill(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    developer = models.ForeignKey(
        Developer, related_name='skills', on_delete=models.CASCADE)
