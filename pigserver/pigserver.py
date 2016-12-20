from flask import Flask
from flask import request
from flask import abort
app = Flask(__name__)

def _translate_to_pig_latin(message):
    # Split message into single words
    raw_tokens = message.split()
    processed_tokens = []

    # Turn all the single words into piglatin words
    for word in raw_tokens:
        processed_word = ""
        # Check for word beginning with vowel
        if word[0].lower() in "aeiou":
            processed_word = word + "yay"
        else: # Assume word begins with consonant sound
            # Find the first vowel
            vowel_index = -1
            for i, c in enumerate(word):
                if c.lower() in "aeiou":
                    vowel_index = i
                    break
            # Check if a vowel was found
            if vowel_index is not -1:
                processed_word = word[vowel_index:] + word[:vowel_index] + "ay"
            else: # If no vowel then just append "ay"
                processed_word = word + "ay"

        processed_tokens.append(processed_word)

    # Go through original message and replace origins with translated tokens
    return " ".join(processed_tokens)



@app.route("/translate", methods=["POST"])
def translate_handler():
    try:
        message = request.form["message"]
        # Expect the message to be passed in as "message" in the POST data, else return 400
        if message == None:
            abort(400)

        translated_text = _translate_to_pig_latin(message)
        return translated_text
    except Exception as e:
        app.logger.error("An error occured from /translate: '%s'".format(e))
        abort(500)


if __name__ == "__main__":
    app.run()
