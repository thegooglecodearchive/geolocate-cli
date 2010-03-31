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
#    DETECTOR, LOCATOR, ENCODER = range(3)
#    def plugin_type(): abstract
    def needs_setup(): abstract
    def setup(): abstract
    def name(): abstract
    def can_run(): abstract

class Detector(object):
    def detection_capabilities(): abstract
    def detect(type): abstract

class Locator(object):
    def location_capabilities(): abstract
    def locate(type, detection): abstract


class Encoder(object):
    pass

def load_plugins(path):
    for name in glob.glob( os.path.join(path, '*.plugin') ):
        mod_name = "plugin__" + name.split(os.path.sep)[-1].split('.')[0]
        m = imp.load_source(mod_name, name)

def find_plugins():
    return Plugin.__subclasses__()

class StandardNames(object):
    detector_types = ["wifi", "cell", "ip", "ipself"]
    WIFI, CELL, IP, IPSELF = tuple(detector_types)

    # A dictionary containing all known names and aliases
    names = {
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
        'ip' : 'ip'
        }

    
