
from django.shortcuts import get_object_or_404

class BaseModel():
    SKIPPED_ATTRIBTES = ['id']

    @staticmethod
    def getAll(cls):
        # print(cls)
        dataset = []
        items = cls.objects.all()
        return cls.getAllToArray(items)
    
    @staticmethod
    def getAllToArray(objects):
        dataset = []
        for item in objects:
            dataset.append(item.toDic())
        return dataset

    @staticmethod
    def getById(cls, id):
        try:
            record = cls.objects.get(id=id)
        except cls.DoesNotExist:
            return False
        return record

    def setAttribute(self, attribute, value):
        if(attribute in self.SKIPPED_ATTRIBTES):
            print('Skipped attribute')
            return
        if(self.isPropertyExists(attribute)):
                setattr(self, attribute, value)


    def setAll(self, values):
        for key, value in values.items():
            self.setAttribute(key, value)
            
    def isPropertyExists(self, attribute):
        return hasattr(self, attribute)
    