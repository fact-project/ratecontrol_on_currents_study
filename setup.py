from setuptools import setup

setup(
    name='ratecontrol_on_currents_study',
    version='0.0.1',
    description='A FACT study - currents, thresholds and rates',
    url='https://github.com/fact-project/ratecontrol_on_currents_study',
    author='Dominik Neise',
    author_email='neised@phys.ethz.ch',
    license='MIT',
    packages=['ratecontrol_on_currents_study'],
    install_requires=[
        'pandas',
        'astropy',
    ],
    test_requires=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [],
    },
    zip_safe=False,
)
