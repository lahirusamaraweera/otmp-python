from django.db import models
from common.baseModel import BaseModel

class category(models.Model, BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    deleted = models.BooleanField(default=False)

    def toDic(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "description" : self.description,
            "deleted" : self.deleted
        } 