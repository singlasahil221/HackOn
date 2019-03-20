
from django.db import models

class BaseModel(models.Model):
    """
    Provides default timestamp model
    All models to extend this base class
    """
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % self.id

    def __unicode__(self):
        return "%s" % self.id
