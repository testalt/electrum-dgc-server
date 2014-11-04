from setuptools import setup

setup(
    name="electrum-dgc-server",
    version="0.9",
    scripts=['run_electrum_dgc_server','electrum-dgc-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'electrumdgcserver':'src'
        },
    py_modules=[
        'electrumdgcserver.__init__',
        'electrumdgcserver.utils',
        'electrumdgcserver.storage',
        'electrumdgcserver.deserialize',
        'electrumdgcserver.networks',
        'electrumdgcserver.blockchain_processor',
        'electrumdgcserver.server_processor',
        'electrumdgcserver.processor',
        'electrumdgcserver.version',
        'electrumdgcserver.ircthread',
        'electrumdgcserver.stratum_tcp',
        'electrumdgcserver.stratum_http'
    ],
    description="Dogecoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/testalt/electrum-dgc-server/",
    long_description="""Server for the Electrum Lightweight Dogecoin Wallet"""
)


