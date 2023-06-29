from requests import get as _get
from cssdotpy import license_raw

def license_short():
    print("""
CSS.py is licensed under GNU GPL 3.0
""")

def license_full():
    print(license_raw.gnugpl3)