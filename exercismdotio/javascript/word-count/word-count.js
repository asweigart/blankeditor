

var Words = function() {};

Words.prototype.count = function(sentence) {
    sentence = sentence.toLowerCase().trim();

    wordCount = {};
    wordCount.constructor = 0; // because JS is weird
    words = sentence.split(/[ \n\t]+/);

    for (var i = 0; i < words.length; i++) {
        if (wordCount[words[i]] === undefined) {
            // this is a new word, start it at one
            wordCount[words[i]] = 1;
        }
        else {
            // we've seen this word before, just increment the count
            wordCount[words[i]]++;
        }
    }

    // because JS is weird
    if (wordCount.constructor === 0) {
        delete wordCount.constructor;
    }

    return wordCount;
};

module.exports = Words;
