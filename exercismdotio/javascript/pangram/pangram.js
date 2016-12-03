var Pangram = function(sentence) {
    this.sentence = sentence.toLowerCase().replace(/[^a-z]/g);
};

Pangram.prototype.isPangram = function() {
    foundLetters = {};

    // iterating over all the letters in sentence, noting the ones we find.
    for (var i = 0; i < this.sentence.length; i++) {
        if (foundLetters[this.sentence[i]] === undefined) {
            foundLetters[this.sentence[i]] = true;
        }
    }

    // check if all 26 letters are in foundLetters.
    return (Object.keys(foundLetters).length === 26);

    /*
    Old solution before I found out how to count the keys in an object.

    // check for any missing letters
    for (i = 97; i < 123; i++) {
        if (foundLetters[String.fromCharCode(i)] === undefined) {
            return false;
        }
    }

    // no missing letters, so return true
    return true;

    */
};

module.exports = Pangram;