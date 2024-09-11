#Vamos a importar la biblioteca pandas y la llamamos pd
import pandas as pd
psg_players = pd.Series (
  ['Navas', 'Mbappe', 'Neymar', 'Messi'],
  index = [1, 7, 10, 30],
)
psg_dict = {1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi'}
psg_players_dict = pd.Series(psg_dict)
print(psg_players_dict)
print(psg_players_dict[7])