from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


class GetAnswerFAQ(Action):
    def __init__(self):
        self.faq_data = pd.read_csv(
            "./data/faq_data.csv")

    def name(self):
        return "actions_GetAnswerFAQ"

    def run(self, dispatcher, tracker, domain):
        query = tracker.latest_message["text"]
        questions = self.faq_data["question"].values.tolist()

        mathed_question, score = process.extractOne(
            query, questions, scorer=fuzz.token_set_ratio
        )  # use process.extract(.. limits = 3) to get multiple close matches

        if (
            score > 50
        ):  # arbitrarily chosen 50 to exclude matches not relevant to the query
            matched_row = self.faq_data.loc[
                self.faq_data["question"] == mathed_question,
            ]

            match = matched_row["question"].values[0]
            answer = matched_row["answers"].values[0]
            response = answer

        else:
            response = "Sorry I couldn't find anything relevant to your query!"

        dispatcher.utter_message(response)


class GetAnswerEvent(Action):
    def __init__(self):
        self.faq_data = pd.read_csv(
            "./data/event.csv")

    def name(self):
        return "actions_GetAnswerEvent"

    def run(self, dispatcher, tracker, domain):
        query = tracker.latest_message["text"]
        questions = self.faq_data["question"].values.tolist()

        mathed_question, score = process.extractOne(
            query, questions, scorer=fuzz.token_set_ratio
        )  # use process.extract(.. limits = 3) to get multiple close matches

        if (
            score > 50
        ):  # arbitrarily chosen 50 to exclude matches not relevant to the query
            matched_row = self.faq_data.loc[
                self.faq_data["question"] == mathed_question,
            ]

            match = matched_row["question"].values[0]
            answer = matched_row["answer"].values[0]
            response = answer

        else:
            response = "Sorry I couldn't find anything relevant to your query!"

        dispatcher.utter_message(response)


class GetAnswerFAQIECSE(Action):
    def __init__(self):
        self.faq_data = pd.read_csv(
            "./data/iecse_faq.csv")

    def name(self):
        return "actions_GetAnswerFAQIECSE"

    def run(self, dispatcher, tracker, domain):
        query = tracker.latest_message["text"]
        questions = self.faq_data["question"].values.tolist()

        mathed_question, score = process.extractOne(
            query, questions, scorer=fuzz.token_set_ratio
        )  # use process.extract(.. limits = 3) to get multiple close matches

        if (
            score > 50
        ):  # arbitrarily chosen 50 to exclude matches not relevant to the query
            matched_row = self.faq_data.loc[
                self.faq_data["question"] == mathed_question,
            ]

            match = matched_row["question"].values[0]
            answer = matched_row["answer"].values[0]
            response = answer

        else:
            response = "Sorry I couldn't find anything relevant to your query!"

        dispatcher.utter_message(response)


class GetAnswerContact(Action):
    def __init__(self):
        self.faq_data = pd.read_csv(
            "./data/contact.csv")

    def name(self):
        return "actions_GetAnswerContact"

    def run(self, dispatcher, tracker, domain):
        query = tracker.latest_message["text"]
        questions = self.faq_data["question"].values.tolist()

        mathed_question, score = process.extractOne(
            query, questions, scorer=fuzz.token_set_ratio
        )  # use process.extract(.. limits = 3) to get multiple close matches

        if (
            score > 50
        ):  # arbitrarily chosen 50 to exclude matches not relevant to the query
            matched_row = self.faq_data.loc[
                self.faq_data["question"] == mathed_question,
            ]

            match = matched_row["question"].values[0]
            answer = matched_row["answer"].values[0]
            response = answer

        else:
            response = "Sorry I couldn't find anything relevant to your query!"

        dispatcher.utter_message(response)


class GetAnswerGeneral(Action):
    def __init__(self):
        self.faq_data = pd.read_csv(
            "./data/general.csv")

    def name(self):
        return "actions_GetAnswerGeneral"

    def run(self, dispatcher, tracker, domain):
        query = tracker.latest_message["text"]
        questions = self.faq_data["question"].values.tolist()

        mathed_question, score = process.extractOne(
            query, questions, scorer=fuzz.token_set_ratio
        )  # use process.extract(.. limits = 3) to get multiple close matches

        if (
            score > 50
        ):  # arbitrarily chosen 50 to exclude matches not relevant to the query
            matched_row = self.faq_data.loc[
                self.faq_data["question"] == mathed_question,
            ]

            match = matched_row["question"].values[0]
            answer = matched_row["answer"].values[0]
            response = answer

        else:
            response = "Sorry I couldn't find anything relevant to your query!"

        dispatcher.utter_message(response)


class GetAnswerRecruitment(Action):
    def __init__(self):
        self.faq_data = pd.read_csv(
            "./data/recruitment.csv")

    def name(self):
        return "actions_GetAnswerRecruitment"

    def run(self, dispatcher, tracker, domain):
        query = tracker.latest_message["text"]
        questions = self.faq_data["question"].values.tolist()

        mathed_question, score = process.extractOne(
            query, questions, scorer=fuzz.token_set_ratio
        )  # use process.extract(.. limits = 3) to get multiple close matches

        if (
            score > 50
        ):  # arbitrarily chosen 50 to exclude matches not relevant to the query
            matched_row = self.faq_data.loc[
                self.faq_data["question"] == mathed_question,
            ]

            match = matched_row["question"].values[0]
            answer = matched_row["answer"].values[0]
            response = answer

        else:
            response = "Sorry I couldn't find anything relevant to your query!"

        dispatcher.utter_message(response)


class GetAnswerComplete(Action):
    def __init__(self):
        self.faq_data = pd.read_csv(
            "./data/complete_dataset.csv")

    def name(self):
        return "actions_GetAnswerComplete"

    def run(self, dispatcher, tracker, domain):
        query = tracker.latest_message["text"]
        questions = self.faq_data["question"].values.tolist()

        mathed_question, score = process.extractOne(
            query, questions, scorer=fuzz.token_set_ratio
        )  # use process.extract(.. limits = 3) to get multiple close matches

        if (
            score > 50
        ):  # arbitrarily chosen 50 to exclude matches not relevant to the query
            matched_row = self.faq_data.loc[
                self.faq_data["question"] == mathed_question,
            ]

            match = matched_row["question"].values[0]
            answer = matched_row["answer"].values[0]
            response = answer

        else:
            response = "Sorry I couldn't find anything relevant to your query!"

        dispatcher.utter_message(response)
