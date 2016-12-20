from flask import Flask
from flask import request
from flask import abort
app = Flask(__name__)

def _index_first_char(word):
    index = -1
    for i, c in enumerate(word):
        if c.lower() in "abcdefghijklmnopqrstuvwxyz":
            index = i
            break
    return index

def _index_last_char(word):
    index = -1
    for i, c in enumerate(word[::-1]):
        if c.lower() in "abcdefghijklmnopqrstuvwxyz":
            index = len(word) - i - 1
            break
    return index

def _translate_to_pig_latin(message):
    # Split message into single words
    raw_tokens = message.split()
    processed_tokens = []

    # Turn all the single words into piglatin words
    for word in raw_tokens:
        start_char_index = _index_first_char(word)
        last_char_index = _index_last_char(word)

        # Skip token if there's no alphabet characters
        if start_char_index == -1 or last_char_index == -1:
            continue

        processed_word = ""
        # Check for word beginning with vowel
        if word[start_char_index].lower() in "aeiou":
            processed_word = word[:last_char_index+1] + "yay" + word[last_char_index+1:]
        else: # Assume word begins with consonant sound
            # Find the first vowel
            vowel_index = -1
            for i, c in enumerate(word):
                if c.lower() in "aeiou":
                    vowel_index = i
                    break
            # Check if a vowel was found
            if vowel_index is not -1:
                processed_word = word[:start_char_index] + word[vowel_index:last_char_index+1] + \
                                 word[start_char_index:vowel_index] + "ay" + word[last_char_index+1:]
            else: # If no vowel then just append "ay"
                processed_word = word + "ay"

        processed_tokens.append(processed_word)

    # Go through original message and replace origins with translated tokens
    result_string = ""

    if len(raw_tokens) != len(processed_tokens):
        raise Exception("A fatal error has occured translating into Pig Latin")

    # Go through every token, find the original token in the original message, grab any
    #  preceding whitespace from it and append the whitespace and processed token to the result string,
    #  we will finish with a result that has all of the original whitespace in tact.
    num_tokens = len(processed_tokens)
    for i in range(0, num_tokens):
        token_index = message.find(raw_tokens[0])
        result_string = result_string + message[:token_index] + processed_tokens[0]
        # If not on last iteration, trim token lists and raw string
        if i < num_tokens - 1:
            message = message[token_index + len(raw_tokens[0]):]
            raw_tokens = raw_tokens[1:]
            processed_tokens = processed_tokens[1:]

    return result_string


@app.route("/translate", methods=["POST"])
def translate_handler():
    message = request.form["message"]
    # Expect the message to be passed in as "message" in the POST data, else return 400
    if message == None:
        abort(400)

    # Attempt to translate to piglatin
    try:
        translated_text = _translate_to_pig_latin(message)
        return translated_text
    except Exception as e:
        app.logger.error("An error occured from /translate: " + str(e))
        abort(500)

def fuu():
    rawstring = """Today I went for a nice long walk in a park. There was a slight breeeze which shook the autmn leaves and frosted the tips of my ears. I enjoyed the piercing touch of my long friend right through to my lungs.

    When I was a child my Nana used to tell me it was 'Jack Frost' who laid those icey sheets... Oh what a chill that drove!"""
    refined = "odayTay Iyay entway orfay ayay icenay onglay alkway inyay ayay arkpay. ereThay asway ayay ightslay eeezebray ichwhay ookshay ethay autmnyay eaveslay andyay ostedfray ethay ipstay ofyay myay earsyay. Iyay enjoyedyay ethay iercingpay ouchtay ofyay myay onglay iendfray ightray oughthray otay myay ungslay. enWhay Iyay asway ayay ildchay myay anaNay usedyay otay elltay emay ityay asway 'ackJay ostFray' owhay aidlay osethay iceyyay eetsshay... Ohyay atwhay ayay illchay atthay ovedray!"
    result = ""
    rawlist = rawstring.split()
    refinedlist = refined.split()

    if len(rawlist) != len(refinedlist):
        print "A fatal error has occured"
        exit(1)

    numtokens = len(refinedlist)
    for i in range(0, numtokens):
        token_index = rawstring.find(rawlist[0])
        result = result + rawstring[:token_index] + refinedlist[0]
        # If not on last iteration, trim token lists and raw string
        if i < numtokens - 1:
            rawstring = rawstring[token_index + len(rawlist[0]):]
            rawlist = rawlist[1:]
            refinedlist = refinedlist[1:]

    print "RESULT: " + result


if __name__ == "__main__":
    # fuu()
    app.run()
    # raw_tokens = message.split()
    # processed_tokens = []

