__author__ = 'matt'

import logging
logger = logging.getLogger()


class RDFdict(object):
    def __init__(self, triples=(), quads=(), default_graph='DEFAULT'):
        self._maindict = dict()
        self._default_graph_name = default_graph
        self._maindict[default_graph] = dict()
        for (s, p, o) in triples:
            self.add_triple(s, p, o)
        for (s, p, o, g) in quads:
            self.add_quad(s, p, o, g)

    def graph_names(self):
        return self._maindict.keys()

    def default_graph_name(self):
        return self._default_graph_name

    def graphs(self):
        return self._maindict.iteritems()

    def graph(self, graphname):
        return self._maindict[graphname]

    def default_graph(self):
        return self.graph(self._default_graph_name)

    def add_triple(self, s, p, o):
        self.add_quad(s, p, o, self._default_graph_name)

    def add_quad(self, s, p, o, g):
        if not g:
            g = self._default_graph_name
        graphdict = self._maindict.setdefault(g, dict())
        self._add_triple_to_graph_dict(graphdict, s, p, o)

    def _add_triple_to_graph_dict(self, graphdict, s, p, o):
        subjectdict = graphdict.setdefault(s, dict())
        if p in subjectdict:
            try:
                subjectdict[p].append(o)
            except AttributeError:
                subjectdict[p] = list((subjectdict[p], o))
        else:
            subjectdict[p] = o

    def __str__(self):
        return self._maindict.__str__()