/*jshint esversion: 6 */

var ETL = function() {};



ETL.prototype.transform = function(oldScrabbleData) {
    var newScrabbleData = {};

    Object.keys(oldScrabbleData).forEach(function(key) { 
        // iterating over each number-points
        var letters = oldScrabbleData[key];
        for (var i = 0; i < letters.length; i++) {
            // looping over each letter worth `key` points
            newScrabbleData[letters[i].toLowerCase()] = parseInt(key);
        }
    });

    return newScrabbleData;
};


module.exports = ETL;