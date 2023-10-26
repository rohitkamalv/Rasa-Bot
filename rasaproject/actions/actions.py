# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetPokemonInfo(Action):
    def name(self) -> Text:
        return "action_get_pokemon_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pokemon_name = next(tracker.get_latest_entity_values('pokemon_name'))
        def get_pokemon_info(pokemon_name):
            response = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon_name.lower())

            if response.status_code == 200:
                data = response.json()
                height = data["height"]
                weight = data["weight"]
                stats = data["stats"]
                base_stats = {}
                for stat_info in stats:
                    stat_name = stat_info["stat"]["name"]
                    base_stat = stat_info["base_stat"]
                    base_stats[stat_name] = base_stat
                return f"{pokemon_name} is {height} decimetre tall and weighs {weight} hectagrams. It's stats are {base_stats}"
            else:
                return None
        # Replace with logic to retrieve and provide information about the specified Pokémon
        # You can call an API or access a database to fetch information about the Pokémon
        pokemon_info = get_pokemon_info(pokemon_name)
        
        if pokemon_info:
            dispatcher.utter_message("Here's some information about {}:\n{}".format(pokemon_name, pokemon_info))
        else:
            dispatcher.utter_message("I couldn't find information about {}. Please provide the name of a valid Pokémon.".format(pokemon_name))

        return []

class ActionGetPokemonType(Action):
    def name(self) -> Text:
        return "action_get_pokemon_type"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pokemon_name = next(tracker.get_latest_entity_values('pokemon_name'))

        def get_pokemon_type(pokemon_name):
            response = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon_name.lower())

            if response.status_code == 200:
                data = response.json()
                types = [t["type"]["name"] for t in data["types"]]
                return " and ".join(types)
            else:
                return None
        # Replace with logic to retrieve and provide the type of the specified Pokémon
        pokemon_type = get_pokemon_type(pokemon_name)
        
        if pokemon_type:
            dispatcher.utter_message("{} is a {}-type Pokémon.".format(pokemon_name, pokemon_type))
        else:
            dispatcher.utter_message("I couldn't determine the type of {}. Please provide the name of a valid Pokémon.".format(pokemon_name))

        return []

class ActionGetPokemonAbilities(Action):
    def name(self) -> Text:
        return "action_get_pokemon_abilities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pokemon_name = next(tracker.get_latest_entity_values('pokemon_name'))
        def get_pokemon_abilities(pokemon_name):
            response = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon_name.lower())

            if response.status_code == 200:
                data = response.json()
                abilities = (list(data['abilities'][i]['ability']['name'] for i in range(len(data['abilities']))))
                return abilities
            else:
                return None
        # Replace with logic to retrieve and provide the abilities of the specified Pokémon
        pokemon_abilities = get_pokemon_abilities(pokemon_name)
        
        if pokemon_abilities:
            dispatcher.utter_message("The abilities of {} are: {}".format(pokemon_name, ", ".join(pokemon_abilities)))
        else:
            dispatcher.utter_message("I couldn't find information about the abilities of {}. Please provide the name of a valid Pokémon.".format(pokemon_name))

        return []

# Define functions like get_pokemon_info, get_pokemon_type, and get_pokemon_abilities
# to retrieve actual data based on your data sources or APIs.
