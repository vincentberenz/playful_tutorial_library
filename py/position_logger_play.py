# Copyright 2018 Max Planck Society. All rights reserved.
# Author: Vincent Berenz

# This file is part of Playful Tutorial Library.
 
# Playful Tutorial Library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Playful Tutorial Library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Playful Tutorial Library.  If not, see <http://www.gnu.org/licenses/>.

####################################################################################



import playful

class position_logger(playful.Node):
    def execute(self):
        # value of POSITION_LOGGER_FREQUENCY is declared in ../config/globals.py
        frequency = playful.get_global("POSITION_LOGGER_FREQUENCY")
        while not self.should_pause():
            # returns a dict key: scheme_id, value: position
            # this dict will contain information on all schemes
            # having a position property
            positions = playful.memory.get_property_value("position")
            # returns a dict key: scheme_type (e.g. ball), value: list of scheme_ids of this type
            type_id = playful.memory.get_scheme_type_scheme_id()
            # function to get the type of a scheme based on the scheme_id
            def get_type(type_id,scheme_id):
                for type in type_id.keys():
                    ids = type_id[type]
                    if scheme_id in ids : return type
                return None
            # print in console list: scheme type: position
            r = ["\nPOSITIONS:"]
            for scheme_id,position in positions.iteritems():
                type = get_type(type_id,scheme_id)
                if type: r.append("\t"+type+": "+str(position))
            playful.console(str(id(self)),"\n".join(r)+"\n")
            # running at configured frequency
            self.spin(frequency)
            
