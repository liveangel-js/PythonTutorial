# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'PythonTutorial'

import json

d = dict(name='Bob', age=20, score=88)
json_d = json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
str = json.loads(json_str)

print json_d
print str
print str["name"]
print json_d.decode("utf-8").encode("cp936")