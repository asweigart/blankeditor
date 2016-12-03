var Isogram = function(word) { 
    this.word = word.toLowerCase().replace(/[^a-z\u00C0-\u017F]/g, ''); 
    
};

Isogram.prototype.isIsogram = function() {
    foundLetters = {}; // keeps track of all the letters seen as we iterate

    // iterate over each character in this.word
    for (var i = 0; i < this.word.length; i++) {
        if (foundLetters[this.word[i]] === undefined) {
            // we haven't seen this letter yet
            foundLetters[this.word[i]] = true;
        }
        else {
            // we have seen this letter previously
            return false;
        }
    }

    return true;
};


module.exports = Isogram;
