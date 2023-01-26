# -*- coding: utf-8 -*-

"""Main code."""

from typing import List

from wdcuration import query_wikidata


def get_mitochondrial_genes(species: str) -> List[str]:
    """Get list of mitochondrial genes from Wikidata
    Args:
      species (str): Either "human" or "mouse".
    Returns:
        List(str): List of strings corresponding to the
            species' mitochondrial genes.
    """

    if species == "human":
        query_human = """
      SELECT ?hgnc WHERE {
        ?item wdt:P1057 wd:Q27973632 .
        ?item wdt:P353 ?hgnc .
      }
      """

        result = query_wikidata(query_human)
        gene_list = list(set([a["hgnc"] for a in result]))
        return gene_list

    elif species == "mouse":
        query_human = """
      SELECT ?mgi WHERE {
        ?item wdt:P1057 wd:Q28377921 .
        ?item wdt:P2394 ?mgi .
      }
      """

        result = query_wikidata(query_human)
        gene_list = list(set([a["mgi"] for a in result]))
        return gene_list

    else:
        raise ValueError("'species' can only be one of 'human' or 'mouse'")
