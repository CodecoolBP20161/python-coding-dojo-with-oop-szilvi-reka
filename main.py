class ContactList(list):

    def search(self, search_str):
        contact_list = ContactList()
        for i in self:
            if search_str in i.name:
                contact_list.append(i)
        return contact_list

    def longest_name(self):
        


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
