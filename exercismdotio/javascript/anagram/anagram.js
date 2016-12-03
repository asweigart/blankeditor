var Anagram = function(originalWord) {
    this.originalWord = originalWord.toLowerCase();
};

Anagram.prototype.matches = function(words) {
    // putting the arguments into a single array in allWords
    var allWords = [];
    var i; // loop variable

    if (typeof words === 'string') {
        for (i in arguments) {
            allWords.push(arguments[i]);
        }
    }
    else {
        allWords = words;
    }

    // collect the actual anagrams and return them
    var actualAnagrams = [];

    for (i = 0; i < allWords.length; i++) {
        if (isAnagram(this.originalWord, allWords[i].toLowerCase()) &&
            this.originalWord !== allWords[i].toLowerCase()) {
            actualAnagrams.push(allWords[i]);
        }
    }


    return actualAnagrams;
};


function isAnagram(wordA, wordB) {
    return wordA.split('').sort().join('') === wordB.split('').sort().join('');
}


module.exports = Anagram;