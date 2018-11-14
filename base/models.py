# Django imports
from django.db import models


class ModelBase(models.Model):
    """A model base class to me inherited from. """
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_active = True
        self.save()