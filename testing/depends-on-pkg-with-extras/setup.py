from setuptools import setup

setup(
    name='depends-on-pkg-with-extras',
    version='3.0.0',
    # In versions <= 0.7.4, when walking the requirements tree, we would
    # stop after seeing a requirement key once. So if we saw foo, a future
    # foo[bar] would be ignored. Or seeing foo[bar], we'd ignore foo[baz].
    install_requires=[
        'pkg-with-extras[extra1]',
        # this line should do nothing; foo is installed as part of foo[bar]
        'pkg-with-extras',
        'pkg-with-extras[extra2,extrapre]',
    ],
)
