import firebase_admin
import os

from firebase_admin import credentials
from django.conf import settings

cred = credentials.Certificate(
    os.path.join(settings.BASE_DIR, "sportpro.json"))
firebase_admin.initialize_app(cred)
