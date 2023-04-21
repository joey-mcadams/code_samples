from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        raise Exception('Editing Dimensions is disabled for this assignment')


class Dimension(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=False)
    has_children = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        raise Exception('Editing Dimensions is disabled for this assignment')
