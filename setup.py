from setuptools import setup

package_name = 'matrix_implementation2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shikur_orin',
    maintainer_email='quantumrobotics.itesm@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'matrixsignalonlyblue = matrix_implementation2.MatrixSignalOnlyBlue:main', 'matrixsignalreceiver = matrix_implementation2.MatrixSignalReceiver:main'
        ],
    },
)
