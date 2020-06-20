class UtilityHelper:

    @staticmethod
    def get_proper_id(data):
        if '_id' in data:
            if '$oid' in data['_id']:
                return data['_id']['$oid']
            else:
                return data['_id']
        else:
            return data['id']



