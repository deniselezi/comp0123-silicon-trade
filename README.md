# comp0123-silicon-trade

GitHub repository for the COMP0123 coursework.

Run `pip install -r requirements.txt` to install the dependencies.

To request data from UN Comtrade, run the `get_data.py` script. (you will need to request an API key from the UN Comtrade website and assign it to the `primary_key` variable)

Afterwards, run the scripts `filter_rows.py` and `filter_columns.py` in that order.

Then, run `generate_nodes.py` and `generate_edges.py` in that order to generate the csv files of nodes and edges to be imported into Gephi.

For your convenience, a set of nodes and edges and the Gephi network file has been provided in the network directory.

