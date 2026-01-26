from setuptools import find_packages, setup

package_name = 'meu_py'

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
    maintainer='thiros',
    maintainer_email='thiros@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "pynode = meu_py.meu_node:main",
            'robot_news_station = meu_py.robot_news_station:main',
            'smartphone = meu_py.smartphone:main'
        ],
    },
)
