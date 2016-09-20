
class Contact:

    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        del cls.all_contacts[:]
        return cls.all_contacts


class Supplier(Contact):
    all_orders = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def order(self, str):
