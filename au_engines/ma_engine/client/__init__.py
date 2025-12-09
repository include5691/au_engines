from .account import MaClientAccount
from .auth import MaClientAuth
from .contacts import MaClientContacts


class MaClient(MaClientContacts, MaClientAuth, MaClientAccount): ...
