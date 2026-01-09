from setuptools import find_packages, setup
import os
from glob import glob
# As importações duplicadas foram removidas.

package_name = 'urdf_tutorial_r2d2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Garante que os arquivos .py sejam instalados na pasta 'launch'
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        # Garante que os arquivos URDF/XACRO sejam instalados
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')), # Correção: deve ser 'urdf' e não o root do pacote
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hiago',
    maintainer_email='hiago@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'state_publisher = urdf_tutorial_r2d2.state_publisher:main'
        ],
    },
)