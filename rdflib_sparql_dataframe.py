"""
Taken from https://github.com/RDFLib/sparqlwrapper/issues/125#issuecomment-704291308 resp. https://github.com/RDFLib/rdflib/issues/1179#issuecomment-704299074 .

Posted by [Daniel Himmelstein](https://github.com/dhimmel)
"""

from pandas import DataFrame
from rdflib.plugins.sparql.processor import SPARQLResult

def sparql_results_to_df(results: SPARQLResult) -> DataFrame:
    """
    Export results from an rdflib SPARQL query into a `pandas.DataFrame`,
    using Python types. See https://github.com/RDFLib/rdflib/issues/1179.
    """
    return DataFrame(
        data=([None if x is None else x.toPython() for x in row] for row in results),
        columns=[str(x) for x in results.vars],
    )
