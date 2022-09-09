#!/usr/bin/env python

# This is an automatically generated script to run your query
# to use it you will require the intermine python client.
# To install the client, run the following command from a terminal:
#
#     sudo easy_install intermine
#
# For further documentation you can visit:
#     http://intermine.readthedocs.org/en/latest/web-services/

# The following two lines will be needed in every python script:
from intermine.webservice import Service
service = Service("https://yeastmine.yeastgenome.org/yeastmine/service")

# For a given human gene(s) retrieve associated OMIM disease phenotype(s) and
# yeast homolog(s).

template = service.get_template('HumanGene_YeastHomolog_Disease')

# You can edit the constraint values below
# C    Gene

rows = template.rows(
  C = {"op": "LOOKUP", "value": "LAL", "extra_value": ""}
)

for row in rows:
  print(row["symbol"], row["name"], row["homologues.homologue.symbol"])

# Next step would be to have a database of human genes, put them into here and then we get all our yeast homologs

# Put all human genes into list and pass into rows query