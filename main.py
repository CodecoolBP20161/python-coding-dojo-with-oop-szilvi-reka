
class ContactList(list):

    def search(self, search_str):
        contact_list = ContactList()
        for i in self:
            if search_str in i.name:
                contact_list.append(i)
        return contact_list

    def longest_name(self):
        try:
            contact_len = []
            for i in self:
                name_len = len(i.name)
                new = [name_len, i.name]
                contact_len.append(new)
            sorted_contact = sorted(contact_len, key=lambda contact: contact[0])
            return sorted_contact[-1][1]
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

contact1 = Contact("Some", "somebody@example.net")
contact2 = Contact("Sandor", "sandor.brody@example.net")
contact3 = Contact("Elek Benedek", "elek.benedek@example.net")
print(Contact.all_contacts.longest_name())
