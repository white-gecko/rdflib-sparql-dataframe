# RDFLib SPARQL DataFrame

Export results from an rdflib SPARQL query into a `pandas.DataFrame`, using Python types.

Taken from https://github.com/RDFLib/sparqlwrapper/issues/125#issuecomment-704291308 resp. https://github.com/RDFLib/rdflib/issues/1179#issuecomment-704299074 .

## Install

```sh
pip install rdflib-sparql-dataframe
# or
poetry add rdflib-sparql-dataframe
```

## Use

```python
from rdflib import Graph
from rdflib_sparql_dataframe import sparql_results_to_df

data = """
@prefix ex: <https://example.org/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

ex:Petra a foaf:Person ;
  foaf:name "Petra" ;
  foaf:knows ex:Peter .

ex:Peter a foaf:Person ;
  foaf:name "Peter" .
"""

query = """
prefix foaf: <http://xmlns.com/foaf/0.1/>
select ?person ?name ?friend ?friendname {
  ?person foaf:name ?name ;
    foaf:knows ?friend .
  ?friend foaf:name ?friendname .
}
"""

graph = Graph()
graph.parse(data=data)

dataframe = sparql_results_to_df(graph.query(query))
```
