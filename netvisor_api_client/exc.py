"""
netvisor.exc
~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""


class NetvisorError(Exception):
    @staticmethod
    def from_status(status):
        code, message = status.split(" :: ", 1)
        error_cls = {
            "AUTHENTICATION_FAILED": AuthenticationFailed,
            "INVALID_DATA": InvalidData,
            "INVALID_DATA_SIZE": InvalidDataSize,
            "DUPLICATE_DATA": DuplicateData,
            "REQUEST_NOT_UNIQUE": RequestNotUnique,
            "PERIOD_LOCK": PeriodLock,
            "SERVICE_ACCESS_ERROR": ServiceAccessError,
            "SYSTEM_MAINTANANCE": SystemMaintenance,
            "TECHNICAL_ERROR": TechnicalError,
        }[code]
        return error_cls(message)


class AuthenticationFailed(NetvisorError):
    pass


class InvalidData(NetvisorError):
    pass


class InvalidDataSize(NetvisorError):
    pass


class DuplicateData(NetvisorError):
    pass


class RequestNotUnique(NetvisorError):
    pass


class PeriodLock(NetvisorError):
    pass


class ServiceAccessError(NetvisorError):
    pass


class SystemMaintenance(NetvisorError):
    pass


class TechnicalError(NetvisorError):
    pass


class UnknownError(NetvisorError):
    pass


class UnknownStatus(NetvisorError):
    pass


class InvalidResponse(NetvisorError):
    pass
