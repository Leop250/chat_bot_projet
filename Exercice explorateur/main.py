import pandas

explorateur_df = pandas.read_csv("parcours_explorateurs.csv")

starting_nodes = explorateur_df[explorateur_df["type_aretes"] =="depart"]["noeud_amont"].values
ending_nodes = explorateur_df[explorateur_df["type_aretes"] == "arrivee"]["noeud_aval"].values


dict_amont_aval = {row["noeud_amont"] : (row["noeud_aval"], row["distance"]) for _, row in explorateur_df.iterrows()}




for starting_node in starting_nodes:
	# sur une itération de cette boucle nous allons construire le chemin parcouru par un explorateur
	explorator_path = [starting_node]
	distance_for_current_explorateur = 0

	# cette boucle reccupère et stocke le noeud aval du noeud aval du noeud aval .......
	# tant que le noeud actuel n'appartient pas à la liste des noeuds d'arrivé.
	while explorator_path[-1] not in ending_nodes:
		current_node = explorator_path[-1]
		next_node, distance = dict_amont_aval[current_node]
		
		explorator_path.append(next_node)
		distance_for_current_explorateur += distance


	print(f"l'explorateur a parcouru {distance_for_current_explorateur:.2f} kms et voici le chemin parcouru :\n{explorator_path}")
	print("_"*20)