/*jshint esversion: 6 */

var BeerSong = function() {};

BeerSong.prototype.verse = function(verseNum) {
    if (verseNum === 0) {
        return 'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n';
    }
    else if (verseNum === 1) {
        return '1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n';
    }
    else if (verseNum === 2) {
        return '2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n';
    }
    else {
        return `${verseNum} bottles of beer on the wall, ${verseNum} bottles of beer.\nTake one down and pass it around, ${verseNum - 1} bottles of beer on the wall.\n`;
    }
};

BeerSong.prototype.sing = function(startVerseNum, stopVerseNum) {
    if (stopVerseNum === undefined) {
        stopVerseNum = 0;
    }

    var allLyrics = '';

    for (var i = startVerseNum; i >= stopVerseNum; i--) {
        allLyrics += this.verse(i) + '\n';
    }

    // chop off final unneeded \n character
    allLyrics = allLyrics.slice(0, -1);

    return allLyrics;
};

module.exports = BeerSong;