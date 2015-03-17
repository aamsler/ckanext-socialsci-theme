from setuptools import setup, find_packages

version = '0.0'

setup(
    name='ckanext-socialsci-theme',
    version=version,
    description="CKAN theme for Open Social Sciences Data",
    long_description="""\
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Liip AG',
    author_email='ogd@liip.ch',
    url='http://www.liip.ch/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.socialscitheme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=
    """
    [ckan.plugins]
    socialscitheme=ckanext.socialscitheme.plugin:SocialSciThemePlugin
    """,
)
