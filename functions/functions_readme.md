This file is made of python notebook that are defining different functions used across the master notebooks. 

# [Functions Fixed Tables](https://github.com/jeanbouteiller-ds/tennis_prediction/blob/main/functions/functions_fixed_table.ipynb)

## Matchs Tables function

- find_matchs(tournament_row):
  - input:
    - tournament_url (string) - represents the tournament wihtout the date (ex: en/tournaments/paris/352/overview) - needs to contain the "overview" mention
    - tournament_date (string) -  represents the date of the tournament (first week)
    - tournament_name (string) - identifier of the tournament name according to the atp website
  - returns:
    -  list_past_matchs_tournament: list of dict with all past games in the tournament. Each game (represented by a dict) contains (winner_name, loser_name, date = tournament_date, tournament_name, round.
    -  list_incoming_matchs_tournament: list of dict with all incoming games in the tournament. Each game contains (date = tournament_date, tournament_name, round, player_1_name, player_2_name)
