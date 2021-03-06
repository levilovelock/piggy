from pigserver import pigserver
import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        pigserver.app.config['TESTING'] = True
        self.app = pigserver.app.test_client()

    # ====================================================
    # Unit Tests
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

    def test_single_quoted_consonant_string(self):
        assert self._test_string("'quoted'") == "'uotedqay'"

    def test_proceeding_consonant_elipses(self):
        assert self._test_string("bare...") == "arebay..."

    def test_apostrophe_in_consonant_string(self):
        assert self._test_string("don't") == "on'tday"

    def test_fullstop_end_of_consonant_string(self):
        assert self._test_string("bed.") == "edbay."

    def test_exclamation_end_of_consonant_string(self):
        assert self._test_string("gamma!") == "ammagay!"

    def test_comma_end_of_consonant_string(self):
        assert self._test_string("clock,") == "ockclay,"

    def test_capitlisation_consonant_string(self):
        assert self._test_string("BarBaRiAN") == "arBaRiANBay"
        assert self._test_string("BArBaRiAn") == "ArBaRiAnBay"
        assert self._test_string("BARBARIAn") == "ARBARIAnBay"
        assert self._test_string("bARBARIAN") == "ARBARIANbay"
        assert self._test_string("baRBARIAN") == "aRBARIANbay"
        assert self._test_string("BARBARIAn") == "ARBARIAnBay"

    def test_single_quoted_vowel_string(self):
        assert self._test_string("'early'") == "'earlyyay'"

    def test_proceeding_vowel_elipses(self):
        assert self._test_string("are...") == "areyay..."

    def test_apostrophe_in_vowel_string(self):
        assert self._test_string("eve's") == "eve'syay"

    def test_fullstop_end_of_vowel_string(self):
        assert self._test_string("eddy.") == "eddyyay."

    def test_exclamation_end_of_vowel_string(self):
        assert self._test_string("apricot!") == "apricotyay!"

    def test_comma_end_of_vowel_string(self):
        assert self._test_string("orange,") == "orangeyay,"

    def test_capitlisation_vowel_string(self):
        assert self._test_string("UgANDa") == "UgANDayay"
        assert self._test_string("ugANDa") == "ugANDayay"
        assert self._test_string("UGANDa") == "UGANDayay"
        assert self._test_string("UgANDA") == "UgANDAyay"
        assert self._test_string("UgANdA") == "UgANdAyay"
        assert self._test_string("ugAnDa") == "ugAnDayay"

    def test_paragraph_string_with_newlines(self):
        sample_input = """Today I went for a nice long walk in a park. There was a slight breeeze which shook the autumn leaves and frosted the tips of my ears. I enjoyed the piercing touch of my long friend right through to my lungs.

        When I was a child my Nana used to tell me it was 'Jack Frost' who laid those icey sheets... Oh what a chill that drove!"""
        expected_output = """odayTay Iyay entway orfay ayay icenay onglay alkway inyay ayay arkpay. ereThay asway ayay ightslay eeezebray ichwhay ookshay ethay autumnyay eaveslay andyay ostedfray ethay ipstay ofyay myay earsyay. Iyay enjoyedyay ethay iercingpay ouchtay ofyay myay onglay iendfray ightray oughthray otay myay ungslay.

        enWhay Iyay asway ayay ildchay myay anaNay usedyay otay elltay emay ityay asway 'ackJay ostFray' owhay aidlay osethay iceyyay eetsshay... Ohyay atwhay ayay illchay atthay ovedray!"""

        assert self._test_string(sample_input) == expected_output

    # ====================================================
    # Acceptance Tests
    # ====================================================
    def test_return_400_when_no_message_passed(self):
        response = self.app.post('/translate', data={})
        assert response.status_code == 400

    def test_return_404_when_trying_invalid_endpoints(self):
        response = self.app.post('/random_nonexistent_path', data={})
        assert response.status_code == 404

    def test_return_405_when_trying_unsupported_methods(self):
        response = self.app.get('/translate')
        assert response.status_code == 405
        response = self.app.delete('/translate')
        assert response.status_code == 405

    def test_return_200_with_response_for_valid_request(self):
        response = self.app.post('/translate', data={"message": "Hello World!"})
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
