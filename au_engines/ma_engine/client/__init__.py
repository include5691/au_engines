from .account import MaClientAccount
from .auth import MaClientAuth
from .contacts import MaClientContacts
from .messages import MaClientMessages


class MaClient(MaClientMessages, MaClientContacts, MaClientAuth, MaClientAccount): ...
