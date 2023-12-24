import json
import os


class State():
    states = {}
    stf = 'state.json'

    def __init__(self):
        if not os.path.isfile(self.stf):
            try:
                with open(self.stf, 'w') as fs:
                    fs.write({})
            except IOError as err:
                print('IOError writing file: ', err)
            except Exception as exc:
                print('Exception writing file: ', exc)

        try:
            with open(self.stf, 'r') as fs:
                self.states = json.load(fs)
        except IOError as err:
            print('IOError reading file: ', err)
        except Exception as exc:
            print('Exception reading file: ', exc)

    def save(self):
        try:
            with open(self.stf, 'w') as fs:
                fs.write(json.dumps(self.states))
        except IOError as err:
            print('IOError writing file: ', err)
        except Exception as exc:
            print('Exception writing file: ', exc)
