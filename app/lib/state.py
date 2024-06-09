import json
import logging
import os

log = logging.getLogger('state')

class State():

    # Init
    def __init__(self) -> None:
        self._states = {}

    @property
    def states(self):
        return self._states

    @states.setter
    def states(self, value):
        log.error('Can not set states directly')

    # Get metrics
    def getMetrics(self) -> list:
        metrics = []
        metrics.append('# HELP wcac_response_code An HTTP response code')
        metrics.append('# TYPE wcac_response_code summary')
        for s in self.states.values():
            metrics.append(
                'wcac_response_code{proto="%s",id="%s",path="%s"} %d' %
                (
                    s['proto'],
                    s['id'],
                    s['path'],
                    s['code']
                )
            )

        metrics.append('# HELP wcac_response_size An HTTP response length in bytes')
        metrics.append('# TYPE wcac_response_size gauge')
        for s in self.states.values():
            metrics.append(
                'wcac_response_size{proto="%s",id="%s",path="%s"} %d' %
                (
                    s['proto'],
                    s['id'],
                    s['path'],
                    s['size']
                )
            )

        metrics.append('# HELP wcac_response_time Number of seconds it took for the request ')
        metrics.append('# TYPE wcac_response_time gauge')
        for s in self.states.values():
            metrics.append(
                'wcac_response_time{proto="%s",id="%s",path="%s"} %f' %
                (
                    s['proto'],
                    s['id'],
                    s['path'],
                    s['time']
                )
            )

        return metrics

    # Set a state
    def setState(self, url, state) -> None:
        self.states[url] = state
