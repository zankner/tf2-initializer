import setuptools

with open('README.md', 'r') as f:
  long_description = f.read()


setuptools.setup(
  name='tf2-initializer',
  version='0.3',
  scripts=['tf2-initializer'],
  author='Zack Ankner',
  author_email='zackankner@gmail.com',
  description='A tf2 project initializer',
  long_description=long_description,
  long_description_content_type='text/markdown',
  install_requires=[
    'importlib_resources'
  ],
  url='https://github.com/zankner/tf2-initializer',
  packages=setuptools.find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3',
    'Operating System :: Unix'
  ]
)
