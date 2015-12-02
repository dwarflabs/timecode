from setuptools import setup, find_packages
import os

version_file = os.path.join(os.path.dirname(__file__), 'timecode', '__VERSION__.py')

with open(version_file, 'r') as fh:
    version_tag = open(version_file).read().strip().split('=')[-1].replace('"','').replace("'", '').replace(" ", "")
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()
CHANGES = open(os.path.join(here, 'CHANGELOG')).read()

kwargs = {}

kwargs['install_requires'] = [
]

kwargs['extras_require'] = {
}

kwargs['entry_points'] = {
}

setup(
    name='timecode',
    version=version_tag,
    description="SMPTE Time Code Manipulation Library",
    long_description='%s\n\n%s' % (README, CHANGES),
    author=['Erkan Ozgur Yilmaz', "Julien Brasseur"],
    author_email=['eoyilmaz@gmail.com', "julien.brasseur@dwarf-labs.com"],
    keywords=['video', 'timecode', 'smpte'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    **kwargs
)
