# Misc shared functions.
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

import plugins, sys

VERSION = "0.1"

def print_err(msg):
    sys.stderr.write(msg + "\n")
    sys.exit(1)

def init_plugin_system():
    #  Detect plugins
    path = os.path.abspath(os.path.dirname(sys.argv[0])) + os.path.sep
    plugins_path = path + "plugins/"
    
    if not (os.path.exists(plugins_path) and os.path.isdir(plugins_path)):
        print_err("Could not find plugins, expected at: " + plugins_path)
        
    # Try and load plugins
        plugins.load_plugins(plugins_path)
        
