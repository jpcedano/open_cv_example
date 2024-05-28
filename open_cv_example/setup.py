from setuptools import find_packages, setup

package_name = 'open_cv_example'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rolix57',
    maintainer_email='rolix57@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cv_example = open_cv_example.cv_example:main',
            'camara = open_cv_example.camara:main',
            'camara_sub = open_cv_example.camara_sub:main',
            'movimiento_camara = open_cv_example.movimiento_camara:main',
        ],
    },
)
