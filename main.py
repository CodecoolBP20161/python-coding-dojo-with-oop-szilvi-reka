
class ContactList(list):

    def search(self, search_str):
        return [i for i in self if search_str in i.name]

    def longest_name(self):
        try:
            names = [i.name for i in self]
            longest = max(names, key=len)
            return longest
        except:
            return None


class Contact:

    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        del cls.all_contacts[:]
        return cls.all_contacts


class Supplier(Contact):
    all_orders = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def order(self, order):
        Supplier.all_orders.setdefault(self.email, []).append(order)
