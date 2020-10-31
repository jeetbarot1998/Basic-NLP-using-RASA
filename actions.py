# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

timezones={
    "London": "UTC 0",
    "Mumbai":"UTC +5:30",
    "Berlin": "UTC +1:00"
}
class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        city=tracker.get_slot("city")
        timezone=timezones.get(city)
        if timezone is None:
            op="Couldnt find the time zone of{}".format(city)
        else:
            op="Time zone of {} is {}".format(city,timezone)
        
        dispatcher.utter_message(text=op)

        return []
