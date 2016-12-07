/*jshint esversion: 6 */

var FoodChain = function() {};

FoodChain.prototype.verse = function(verseNum) {
    // special horse case
    if (verseNum === 8) {
        return 'I know an old lady who swallowed a horse.\n' + 'She\'s dead, of course!\n';
    }

    var primaryLyric = {
        1: 'I know an old lady who swallowed a fly.\n',
        2: 'I know an old lady who swallowed a spider.\nIt wriggled and jiggled and tickled inside her.\n',
        3: 'I know an old lady who swallowed a bird.\nHow absurd to swallow a bird!\n',
        4: 'I know an old lady who swallowed a cat.\nImagine that, to swallow a cat!\n',
        5: 'I know an old lady who swallowed a dog.\nWhat a hog, to swallow a dog!\n',
        6: 'I know an old lady who swallowed a goat.\nJust opened her throat and swallowed a goat!\n',
        7: 'I know an old lady who swallowed a cow.\nI don\'t know how she swallowed a cow!\n'
    };

    var secondaryLyric = {
        1: 'I don\'t know why she swallowed the fly. Perhaps she\'ll die.\n',
        2: 'She swallowed the spider to catch the fly.\n',
        3: 'She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.\n',
        4: 'She swallowed the cat to catch the bird.\n',
        5: 'She swallowed the dog to catch the cat.\n',
        6: 'She swallowed the goat to catch the dog.\n',
        7: 'She swallowed the cow to catch the goat.\n'
    };

    var allLyrics = primaryLyric[verseNum];

    for (var i = verseNum; i > 0; i--) {
        allLyrics += secondaryLyric[i];
    }

    return allLyrics;
};

FoodChain.prototype.verses = function(startingVerseNum, endingVerseNum) {
    var allLyrics = '';

    for (var i = startingVerseNum; i <= endingVerseNum; i++) {
        allLyrics += this.verse(i) + '\n';
    }

    return allLyrics;
};

module.exports = FoodChain;


//console.log((new FoodChain()).verse(1));