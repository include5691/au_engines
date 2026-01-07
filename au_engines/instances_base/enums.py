from enum import Enum


class InstanceState(str, Enum):
    NOT_AUTHORIZED = "notAuthorized"
    AUTHORIZED = "authorized"
    BLOCKED = "blocked"
    STARTING = "starting"
    SUSPENDED = "suspended"
    SLEEP_MODE = "sleepMode"
    YELLOW_CARD = "yellowCard"
