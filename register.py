# -*- coding: utf-8 -*-

class CreateRegister():

    def __init__(self, fields):
        self.fields = dict()
        self.fields['is_error'] = False
        for key in fields.keys():
            self.fields[key] = fields[key]
        self.errors = list()

    def addError(self, item, type, message, value):
        assert item in self.fields.keys(), "The item '%s' was not found in key's field" % item
        error = dict()
        error['type'] = type
        error['location'] = item
        error['message'] = message
        error['value'] = value
        self.errors.append(error)

    def getList(self):
        registers = list()
        registers.append(self.fields)
        for error in self.errors:
            register = self.fields
            register['is_error'] = True
            register['description'] = error
            registers.append(register)
        return registers




