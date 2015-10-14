# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------


## This file defines parameters for a prediction experiment.

###############################################################################
#                                IMPORTANT!!!
# This params file is dynamically generated by the RunExperimentPermutations
# script. Any changes made manually will be over-written the next time
# RunExperimentPermutations is run!!!
###############################################################################


from nupic.frameworks.opf.expdescriptionhelpers import importBaseDescription

# the sub-experiment configuration
config ={
  'aggregationInfo' : {'seconds': 0, 'fields': [], 'months': 0, 'days': 0, 'years': 0, 'hours': 0, 'microseconds': 0, 'weeks': 0, 'minutes': 0, 'milliseconds': 0},
  'modelParams' : {'sensorParams': {'encoders': {u'ReadError20': None, u'Servo9': None, u'Writes': None, u'FlyHeight11': None, u'FlyHeight16': None, u'ReadError12': None, u'FlyHeight14': None, u'FlyHeight15': None, u'FlyHeight12': None, u'FlyHeight13': None, u'FlyHeight10': None, u'Servo8': None, u'Servo7': None, u'Servo6': None, u'Servo5': None, u'Servo4': None, u'Servo3': None, u'PList': None, u'Servo1': None, u'Hours': None, u'Servo2': None, u'HoursBeforeFail': None, u'Temp1': None, u'WriteError': None, u'ReadError8': None, u'ReadError9': None, u'ReadError1': None, u'ReadError2': None, u'ReadError3': None, u'ReadError4': None, u'ReadError5': None, u'ReadError6': None, u'ReadError7': None, u'FlyHeight4': None, u'FlyHeight5': None, u'FlyHeight6': None, u'FlyHeight7': None, u'FlyHeight1': None, u'FlyHeight2': None, u'FlyHeight3': None, u'serial': None, u'FlyHeight8': None, u'FlyHeight9': None, u'GList3': None, u'GList2': None, u'GList1': None, u'class': None, u'CSS': {'name': 'CSS', 'clipInput': True, 'n': 272, 'fieldname': 'CSS', 'w': 21, 'type': 'AdaptiveScalarEncoder'}, '_classifierInput': {'fieldname': 'class', 'classifierOnly': True, 'type': 'SDRCategoryEncoder', 'w': 21, 'n': 121}, u'ReadError13': None, u'ReadError10': None, u'ReadError11': None, u'ReadError16': None, u'ReadError14': None, u'ReadError15': None, u'ReadError18': None, u'ReadError19': None, u'Temp3': None, u'Temp2': None, u'Reads': None, u'Temp6': None, u'Temp5': None, u'Temp4': None, u'Frame': None, u'Servo10': None}}, 'spParams': {'synPermInactiveDec': 0.05015}, 'tpParams': {'minThreshold': 11, 'activationThreshold': 14, 'pamLength': 3}, 'clParams': {'alpha': 0.050050000000000004}},

}

mod = importBaseDescription('../description.py', config)
locals().update(mod.__dict__)
