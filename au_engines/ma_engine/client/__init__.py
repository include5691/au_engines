from .account import MaxClientAccount
from .auth import MaxClientAuth
from .contacts import MaxClientContacts


class MaxClient(MaxClientContacts, MaxClientAuth, MaxClientAccount): ...
