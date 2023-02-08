from setuptools import setup

package_name = 'cmd_bridge'

setup(
  name=package_name,
  version='0.0.1',
  packages=[package_name],
  data_files=[
    ('share/ament_index/resource_index/packages',
      ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
  ],
  install_requires=['setuptools'],
  zip_safe=True,
  maintainer='Rafael Martin',
  maintainer_email="rmartin@robotnik.es",
  description='This package provides a bridge between ROS and ROS2 for the command interface.',
  license='BSD',
  tests_require=['pytest'],
  entry_points={
    'console_scripts': [
      'cmd_bridge = cmd_bridge.cmd_bridge:main',
    ],
  },
)
