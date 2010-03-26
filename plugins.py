import os, glob, imp

# Loosely based on http://lucumr.pocoo.org/2006/7/3/python-plugin-system

class Plugin(object):
#    DETECTOR, LOCATOR, ENCODER = range(3)
#    def plugin_type(): abstract
    def needs_setup(): abstract
    def setup(): abstract
    def name(): abstract
    def can_run(): abstract

class Locator(object):
    def locate(): abstract

class Detector(object):
    types = ["wifi", "cell", "ip"]
    WIFI, CELL, IP = tuple(types)
    def detection_capabilities(): abstract
    def detect(type): abstract

class Encoder(object):
    pass

def load_plugins(path):
    for name in glob.glob( os.path.join(path, '*.plugin') ):
        mod_name = "plugin__" + name.split(os.path.sep)[-1].split('.')[0]
        m = imp.load_source(mod_name, name)

def find_plugins():
    return Plugin.__subclasses__()
