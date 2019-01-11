from distutils.core import setup
setup(
  name = 'streamsvg',
  packages = ['streamsvg'],
  version = '1.1.1',
  description = 'Small library to draw stream graphs into SVG format',
  author = 'Ioannis SIglidis',
  author_email = 'yiannis.siglidis@lip6.fr',
  url = 'https://github.com/ysig/streamsvg',
  keywords = ['stream graphs', 'visualization', 'temporal networks', 'svg'], 
  classifiers = [],
  install_requires=['svgwrite >= 1.1.9']
)
