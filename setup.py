#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from distutils.core import setup
from lib.version import ELECTRUM_VERSION as version

setup(name = "Electrum",
    version = version,
    install_requires = ['slowaes','ecdsa'],
    package_dir = {'electrum': 'lib'},
    scripts= ['electrum'],
    data_files=[
          ('/usr/share/locale/de/LC_MESSAGES', ['locale/de/LC_MESSAGES/electrum.mo']),
          ('/usr/share/locale/fr/LC_MESSAGES', ['locale/fr/LC_MESSAGES/electrum.mo']),
          ],
    py_modules = ['electrum.version',
                  'electrum.wallet',
                  'electrum.interface',
                  'electrum.gui',
                  'electrum.gui_qt',
                  'electrum.icons_rc',
                  'electrum.mnemonic',
                  'electrum.pyqrnative',
                  'electrum.bmp',
                  'electrum.i18n'],
    description = "Lightweight Bitcoin Wallet",
    author = "thomasv",
    license = "GNU GPLv3",
    url = "http://ecdsa/electrum",
    long_description = """Lightweight Bitcoin Wallet""" 
)
