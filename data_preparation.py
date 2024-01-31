import pandas
import numpy
import matplotlib.pyplot as plt

class DataPreparation:
	def __init__(self, csv_path):
		"""
		Cette classe prend en entrée un chemin de fichier csv.
		Elle split le jeu de donnée en 2 bases 
		+ une train 75 %
		+ une test 25 %
		Ce 2 bases, la classe va les splits en 2 

		+ un vecteur x (qui contient les indexs temporels)
		+ un vecteyr y (qui contient les valeurs à prédire)
		En tout cette va extraire 4 arrays.
		x_train # problème train
		y_train # solution train
		x_test # problème test
		y_test # solution test
		"""
		self.dataset_df = pandas.read_csv(csv_path)
		self.dataset_df["Years"] = pandas.to_datetime(self.dataset_df["Years"])
		self.dataset_df["month_name"] = self.dataset_df["Years"].dt.strftime('%B')
		self.dataset_df = pandas.get_dummies(self.dataset_df, columns =['month_name'], drop_first=True)
		self.prepare_data()

		

	
	def afficher_dataframe(self):
		print(self.dataset_df)


	def prepare_data(self):
		number_of_rows = len(self.dataset_df)
		self.dataset_df["index_mesure"] = numpy.arange(0, number_of_rows, 1)

		dataset_train_df = self.dataset_df.iloc[ : int(number_of_rows*0.75)]
		dataset_test_df = self.dataset_df.iloc[int(number_of_rows*0.75): ]

		x_columns = ['index_mesure'] + [col for col in self.dataset_df if col.startswith('month_name')]
		self.x_train = dataset_train_df[x_columns].values 
		self.y_train = dataset_train_df[['Sales']].values

		self.x_test = dataset_test_df[x_columns].values  
		self.y_test = dataset_test_df[['Sales']].values


	def show_graph(self):
		plt.figure(figsize=(15, 6))
		plt.plot(self.dataset_df["Years"], self.dataset_df["Sales"], "o:")
		
		
		plt.show()
