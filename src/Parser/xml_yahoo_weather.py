# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'PythonTutorial'


from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        if name == 'yweather:forecast':
            self.add_data(attrs)
            # print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        return
        # print('sax:end_element: %s' % name)

    def char_data(self, text):
        return
        # print('sax:char_data: %s' % text)

    def __init__(self):
        self._weather = list()

    def add_data(self,name):
        self._weather.append(name)




try:
    f = open('yahoo_weather.xml', 'r')
    content = f.read()

finally:
    if f:
        f.close()

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(content)
print handler._weather