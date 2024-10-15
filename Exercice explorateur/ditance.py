import pandas

explorateur_df = pandas.read_csv("parcours_explorateurs.csv")
starting_nodes = explorateur_df[explorateur_df["type_aretes"] =="depart"]["noeud_amont"].values
ending_nodes = explorateur_df[explorateur_df["type_aretes"] == "arrivee"]["noeud_aval"].values
dict_amont_aval = {row["noeud_amont"] : row["noeud_aval"] for _, row in explorateur_df.iterrows()}

shortest_path = None
longest_path = None
shortest_path_length = float('inf')  # Initialize with positive infinity
longest_path_length = 0

for starting_node in starting_nodes:
    explorator_path = [starting_node]

    while explorator_path[-1] not in ending_nodes:
        current_node = explorator_path[-1]
        next_node = dict_amont_aval[current_node]
        explorator_path.append(next_node)

    path_length = len(explorator_path)
    if path_length < shortest_path_length:
        shortest_path_length = path_length
        shortest_path = explorator_path
    if path_length > longest_path_length:
        longest_path_length = path_length
        longest_path = explorator_path

print(f"Shortest path: {shortest_path} (length: {shortest_path_length})")
print(f"Longest path: {longest_path} (length: {longest_path_length})")