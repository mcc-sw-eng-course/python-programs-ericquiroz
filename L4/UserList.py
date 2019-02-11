import json

class User:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'Name:{self.name};Address:{self.address};Phone:{self.phone};Email:{self.email}'

    def __repr__(self):
        return str(self)


class UserList:
    def __init__(self):
        self.list = []

    def isValueUser(self, value):
        if type(value) is User:
            return True;
        else:
            return False;

    def __str__(self):
        return ','.join(map(str, self.list))

    def jsonVal(self):
        jsonString = json.dumps([user.__dict__ for user in self.list])

        return jsonString;

    def addItem(self, item):
        if self.isValueUser(item):
            # print(f'Adding {item} to list')
            self.list.append(item)
        else:
            # print(f'Invalid User: {item}')
            raise TypeError

    def exportList(self, fileName):
        # print(f'Exporting list "{str(self)}" to file {fileName}')
        file = open(fileName, 'w')
        try:
            file.write(self.jsonVal())
        finally:
            file.close()

    def importList(self, fileName):
        # print(f'Exporting list to file {fileName}')
        file = open(fileName, 'r')
        try:
            textList = file.readline()
            # print(textList)
            loadedJson = json.loads(textList)
            # print(loadedJson)

            for user in loadedJson:
                # print("Creating user")
                user = User(user['name'], user['address'], user['phone'], user['email'])

                self.addItem(user)
        finally:
            file.close()

    def searchByUserName(self, username):

        search = str(username)

        for u in self.list:
            if u.name == search:
                return u

        raise KeyError
