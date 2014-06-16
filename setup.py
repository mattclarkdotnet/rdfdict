__author__ = 'Matt Clark'

with open('README.md') as f:
    long_desc = f.read()

from setuptools import setup
setup(
    name = "RDFdict",
    version = "0.1",
    py_modules = ['rdfdict'],

    # metadata for upload to PyPI
    author = "Matt Clark",
    author_email = "matt@mattclark.net",
    description = "A class for creating a nested dictionaries representation of RDF quads or triples",
    long_description = long_desc,
    license = "MIT",
    keywords = "rdf json dict",
    url = "http://github.com/mattclarkdotnet/rdfdict"

)
