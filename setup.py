setup(
    name='example',
    version='0.1.0',
    packages=find_packages(include=['dubo', 'dubo.*']),
    install_requires=[
        'pandas==0.23.3',
        'numpy>=1.14.5',
        'matplotlib>=2.2.0',
    ]
    extras_require={
        'interactive': ['jupyter'],
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
