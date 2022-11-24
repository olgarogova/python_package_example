import setuptools
from os.path import join, dirname


setuptools.setup(
    name="package-print-date",
    version="0.1",
    author="Olga Rogova",
    description="This is a test package.",
    long_description=open(join(dirname(__file__), 'package_print_date/README.md')).read(),
    long_description_content_type="text/markdown",
    packages=['package_print_date'],
    entry_points={'console_scripts': ['package_print_date = package_print_date.print_date:main']},
    python_requires='>=3.6'
)
