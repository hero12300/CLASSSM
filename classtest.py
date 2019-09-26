#!/usr/bin/env python3


class UserData:

    def __init__ (self,id,name):
        self.id = id
        self._name = name

    def __repr__(self):
       return 'ID:{} Name:{}'.format(self.id,self._name)


class NewUser(UserData):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if len(value) <= 3:
            print('ERROR')
        else:
            self._name = value

    def __call__(self):
        print('{}\'s id is {}'.format(self._name, self.id))


if __name__ == '__main__':
    user = NewUser(101,'Jack')
    user()
