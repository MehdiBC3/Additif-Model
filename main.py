from data_preparation import DataPreparation
from Additif import Regression


csv_path = "./vente_maillots_de_bain.csv"
data_preparation_object = DataPreparation(csv_path)
regression_object = Regression(data_preparation_object)
data_preparation_object.afficher_dataframe()

# data_preparation_object.show_graph()
