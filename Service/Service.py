import json


class Service:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.objects().order_by('position').to_json()

    def get_all_sorted_by_date(self):
        return json.loads(self.model.objects().order_by('-createdAt').to_json())

    def delete(self, model_item):
        self.model.objects(id=model_item['_id']['$oid']).delete()

    def update_position(self, data):
        for i, item in enumerate(data):
            self.model.objects(id=item['_id']['$oid']).update_one(set__position=i + 1)
        return self.model.objects().to_json()

    def bulk_activate(self, data):
        for i, item in enumerate(data):
            self.model.objects(id=item['_id']['$oid']).update_one(set__active=1)

    def bulk_deactivate(self, data):
        for i, item in enumerate(data):
            self.model.objects(id=item['_id']['$oid']).update_one(set__active=0)

    def bulk_delete(self, data):
        for i, item in enumerate(data):
            self.model.objects(id=item['_id']['$oid']).delete()
