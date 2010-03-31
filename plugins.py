# A very crude plugin system that suits our needs.
# Copyright (C) 2010 Francis Markham
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version. This program is distributed in the 
# hope that it will be useful, but WITHOUT ANY WARRANTY; without 
# even the implied warranty of MERCHANTABILITY or FITNESS FOR 
# A PARTICULAR PURPOSE. See the GNU General Public License 
# for more details. You should have received a copy of the GNU General 
# Public License along with this program. If not, see <http://www.gnu.org/licenses/>. 

import os, glob, imp

# Inpired by http://lucumr.pocoo.org/2006/7/3/python-plugin-system

class Plugin(object):
    def needs_setup(): abstract
    def setup(): abstract
    @staticmethod    
    def name(): abstract
    def can_run(): abstract

class Formatter(object):
    def needs_setup(): return False
    def setup(): pass
    def can_run(): return True

    def needs_input_specifiers(): abstract
    def needs_output_specifiers(): abstract
    def parse_input(input, specifiers): abstract
    def format_output(output, specifiers): abstract


class Detector(object):
    def detection_capabilities(): abstract
    def detect(type): abstract

class Locator(object):
    @classmethod
    def can_locate(cls, names):
        okay = cls.location_capabilities()
        for n in names:
            if not n in okay:
                return False
        else:
            return True

    @classmethod
    def location_capabilities(cls): abstract
    def locate(detection): abstract


class Encoder(object):
    pass

def load_plugins(path):
    for name in glob.glob( os.path.join(path, '*.plugin') ):
        mod_name = "plugin__" + name.split(os.path.sep)[-1].split('.')[0]
        m = imp.load_source(mod_name, name)

def find_plugins():
    return Plugin.__subclasses__()

def find_plugin_by_name(name, type=None):
    name = name.lower()
    for p in find_plugins():
        if p.name().lower() == name:
            if type:
                if type in p.__bases__:
                    return p
                else:
                    continue
            else:
                return p
    return None



class StandardNames(object):
    detector_types = ["wifi", "cell", "ip", "ipself"]
    WIFI, CELL, IP, IPSELF = tuple(detector_types)

    # A dictionary containing all known names and aliases
    canonical_names = {
        # canonical geographic names
        'lat' : 'lat', 
        'long' : 'long',
        'accuracy' : 'accuracy',
        'country' : 'country',
        'city' : 'city',
        'zip' : 'zip',
        'address' : 'address',
        
        # geographic name aliases
        'latitude' : 'lat',
        'y' : 'lat',
        'longitude': 'long',
        'x' : 'long',
        'acc' : 'accuracy',
        'iso-3166-1' : 'country',
        'zipcode' : 'zip',
        'postcode' : 'postcode',
        'addr' : 'address',

        # canonical detection data names
        'mac' : 'mac',
        'ssid' : 'ssid',
        'signal_strength' : 'signal_strength',
        'ip' : 'ip',
        'ipself' : 'ipself'
        }
    
    # Returns a tuple of the format:
    #    (specifier, description)
    names = {
        'lat' : ('y', 'Latitude'),
        'long' : ('x', 'Longitude'),
        'accuracy' : ('a', 'Accuracy of geocode'),
        'country' : ('c', 'Country'),
        'city' : ('t', 'City'),
        'zip' : ('z', 'Zip code'),
        'address' : ('d', 'Street address'),
        'mac' : ('m', 'MAC address'),
        'ssid' : ('e', 'SSID'),
        'signal_strength' : ('s', 'Signal strength'),
        'ip' : ('i', 'IP address')
        }

    @staticmethod
    def find_name(specifier):
        for name, (spec, desc) in StandardNames.names.items():
            if specifier == spec:
                return name
        return None
