import os
from pyotp import TOTP

totp = TOTP(os.getenv("TOTP_SECRET_KEY"))