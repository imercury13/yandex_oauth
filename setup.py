from setuptools import setup, find_packages
from os.path import join, dirname
import yandex_oauth

setup(
    name='yandex_oauth',
    version=yandex_oauth.__version__,
    packages=find_packages(),
    description='Yandex OAuth Lib',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    author=yandex_oauth.__author__,
    author_email='ya360@uh.net.ru',
    maintainer=yandex_oauth.__author__,
    maintainer_email='ya360@uh.net.ru',
    download_url='https://github.com/imercury13/yandex_oauth',
    #url='https://ya360.uh.net.ru',
    license='MIT',
    project_urls={
        "Documentation": "https://yandex-oauth.readthedocs.io/ru/1.1.2",
        "Bug Tracker": "https://github.com/imercury13/yandex_oauth/issues"
    },
    classifiers=[
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python'
    ],
    install_requires=[
        'jreq>=1.1.0',
    ],
    include_package_data=True,
)
