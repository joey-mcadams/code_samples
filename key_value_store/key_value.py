class KeyValue:
    def __init__(self):
        self.store = {}
        self.store_backup = []
        self.value_count = {}

    def set_value(self, key_, value="NULL"):
        old_value = self.store.get(key_, None)
        if old_value in self.value_count.keys():
            self.value_count[old_value] = self.value_count.get(old_value, 1) - 1

        self.store[key_] = value
        self.value_count[value] = self.value_count.get(value, 0) + 1

    def get_value(self, key_):
        try:
            print(self.store.get(key_, "NULL"))
            return self.store.get(key_)
        except KeyError:
            print("NULL")
            return None

    def delete_key(self, key_):
        try:
            value = self.store.pop(key_)
            self.value_count[value] -= 1
        except KeyError:
            pass

    def count(self, value):
        print(self.value_count.get(value, 0))
        return self.value_count.get(value, 0)

    def begin(self):
        self.store_backup.append(self.store)
        self.store = {}
        self._sync_counts()

    def commit(self):
        if not self.store_backup:
            print("ERROR, no transaction")
            return
        old_store = self.store_backup.pop()
        old_store.update(self.store)
        self.store = old_store
        self._sync_counts()

    def rollback(self):
        if not self.store_backup:
            print("ERROR, no transaction")
            return
        self.store = self.store_backup.pop()
        self._sync_counts()

    def _sync_counts(self):
        value_list = []
        for key in self.store.keys():
            value_list.append(self.store[key])

        values = list(set(value_list))

        self.value_count = {}
        for value in values:
            self.value_count[value] = value_list.count(value)