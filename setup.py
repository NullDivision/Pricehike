from setuptools import setup

setup(name='pricehike',
      version='0.0.1',
      packages=['scraper'],
      entry_points={
          'console_scripts': [
              'pricehike = scraper.__main__:main'
          ]
      },
      install_requires=['beautifulsoup4']
      )
