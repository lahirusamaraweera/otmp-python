
class BaseModel():
    @staticmethod
    def getAll(cls):
        print(cls)
        dataset = []
        items = cls.objects.all()
        for item in items:
            dataset.append(item.toDic())
        return dataset