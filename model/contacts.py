# -*- coding: utf-8 -*-
from sys import maxsize
class Contacts:


    def __init__(self, name=None, middleN=None, lastN=None, nickN=None, title=None, company=None, address=None, home=None,
                 mobile=None, work=None, fax=None, email1=None, email2=None, email3=None, HP=None, address2=None, phone2=None,
                 notes=None, id=None,  all_phones_from_HP=None, all_mails_from_HP=None):
        self.name = name
        self.middleN = middleN
        self.lastN = lastN
        self.nickN = nickN
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.HP = HP
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_HP =  all_phones_from_HP
        self.all_mails_from_HP = all_mails_from_HP


    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s" % (self.name, self.lastN, self.address, self.id, self.home, self.mobile , self.work, self.phone2)


    def __eq__(self, other):
        return self.name == other.name and self.lastN == other.lastN and (self.address == other.address or self.address is None or other.address is None) and (self.id is None or other.id is None or self.id == other.id)



    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize