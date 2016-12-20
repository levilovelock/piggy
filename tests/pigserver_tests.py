import os
from pigserver import pigserver
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        pigserver.app.config['TESTING'] = True
        self.app = pigserver.app.test_client()

    # ====================================================
    # Acceptance Tests
    # ====================================================

    def _test_string(self, data):
        response = self.app.post('/translate', data=dict(
            message=data
        ))
        return response.data

    def test_example_consonant_strings(self):
        assert self._test_string("pig") == "igpay"
        assert self._test_string("banana") == "ananabay"
        assert self._test_string("trash") == "ashtray"
        assert self._test_string("happy") == "appyhay"
        assert self._test_string("duck") == "uckday"
        assert self._test_string("glove") == "oveglay"

    def test_example_vowel_strings(self):
        assert self._test_string("eat") == "eatyay"
        assert self._test_string("omelet") == "omeletyay"
        assert self._test_string("are") == "areyay"

    def test_paragraph_string(self):
        sample_input = """Today I went for a nice long walk in a park. There was a slight breeeze which shook the autmn leaves and frosted the tips of my ears. I enjoyed the piercing touch of my long friend right through to my lungs.

        When I was a child my Nana used to tell me it was 'Jack Frost' who laid those icey sheets... Oh what a chill that drove!"""
        expected_output = """odayTay Iyay entway orfay ayay icenay onglay alkway inyay ayay arkpay. ereThay asway ayay ightslay eeezebray ichwhay ookshay ethay autumnyay eaveslay andyay ostedfray ethay ipstay ofyay ymay earsyay. Iyay enjoyedyay ethay iercingpay ouchtay ofyay ymay onglay iendfray ightray oughthray otay ymay ungslay.

        enWhay Iyay asway ayay ildchay ymay anaNay usedyay otay elltay emay ityay asway 'ackJay ostFray' owhay aidlay osethay iceyyay eetsshay... Ohyay atwhay ayay illchay atthay ovedray!"""

        print self._test_string(sample_input)
        assert self._test_string(sample_input) == expected_output

if __name__ == '__main__':
    unittest.main()
