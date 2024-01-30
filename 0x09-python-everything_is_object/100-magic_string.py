#!/usr/bin/python3
def magic_string(to=[0]):
    to[0] += 1
    return ('BestSchool, ' * (to[0] - 1)) + 'BestSchool'
