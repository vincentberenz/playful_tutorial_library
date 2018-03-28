
# variables declared in any config/globals.py files will be
# accessible in all playful python library via the
# playful.get_global(key) function
# e.g. playful.get_global("POSITION_LOGGER_FREQUENCY") should return 5.
# see this being used in ../py/position_logger_play.py
# note that is abritrary python code

POSITION_LOGGER_FREQUENCY = 5
