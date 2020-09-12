import pytest
import json
import os

open_anilist = __import__('open-anilist-page')

class TestClass:
    def setup_method(self, test_method):
        # configure self.attribute
        fn = os.path.join(os.path.dirname(__file__), 'data.json')
        input_file = open(fn, "r")
        self.data = json.loads(input_file.read())
        input_file.close()

    def teardown_method(self, test_method):
        # tear down self.attribute
        pass

    def test_json_match(self):
        # get the filename and actual url in the JSON
        for anime_filename, anilist_url in self.data.items():
            # call script to see what we predict
            predicted_anilist_url = open_anilist.get_anilist_url(anime_filename)

            # check if we were right
            assert predicted_anilist_url == anilist_url