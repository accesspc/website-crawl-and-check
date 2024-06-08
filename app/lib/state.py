import json
import logging
import os

log = logging.getLogger('state')

class State():

    states = {}
    stf = 'state/state.json'

    def __init__(self) -> None:
        if not os.path.isfile(self.stf):
            try:
                with open(self.stf, 'w') as fs:
                    fs.write({})
            except IOError as err:
                log.error('IOError writing file: ', err)
            except Exception as exc:
                log.error('Exception writing file: ', exc)

        try:
            with open(self.stf, 'r') as fs:
                self.states = json.load(fs)
        except IOError as err:
            log.error('IOError reading file: ', err)
        except Exception as exc:
            log.error('Exception reading file: ', exc)

    def save(self) -> None:
        try:
            with open(self.stf, 'w') as fs:
                fs.write(json.dumps(self.states))
        except IOError as err:
            log.error('IOError writing file: ', err)
        except Exception as exc:
            log.error('Exception writing file: ', exc)

    def update(self, url, states) -> None:
        self.states[url] = states
