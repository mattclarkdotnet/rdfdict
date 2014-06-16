__author__ = 'matt'

from setuptools import setup
setup(
    name = "RDFdict",
    version = "0.1",
    py_modules = 'rdfdict',

    # metadata for upload to PyPI
    author = "Matt Clark",
    author_email = "matt@mattclark.net",
    description = "A class for creating a nested dictionaries representation of RDF quads or triples",
    license = "MIT",
    keywords = "rdf json dict",
    url = "http://github.com/mattclarkdotnet/rdfdict",
)
