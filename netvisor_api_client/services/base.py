"""
netvisor.services.base
~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""


class Service(object):
    def __init__(self, client):
        self.client = client
