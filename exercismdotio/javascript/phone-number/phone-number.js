/*jshint esversion: 6 */

var PhoneNumber = function(rawPhoneNumber) {
    'use strict';

    // removing all non-digits
    rawPhoneNumber = rawPhoneNumber.replace(/[^0-9]/g, '');

    if (rawPhoneNumber.length === 10) {
        this.phoneNumber = rawPhoneNumber;
    } 
    else if (rawPhoneNumber.length === 11 && rawPhoneNumber[0] === '1') {
        this.phoneNumber = rawPhoneNumber.slice(1); // chop off first digit, which is '1'
    }
    else {
        this.phoneNumber = '0000000000'; // bad phone numbers
    }
};


PhoneNumber.prototype.number = function() {
    return this.phoneNumber;
};

PhoneNumber.prototype.areaCode = function() {
    return this.phoneNumber.slice(0, 3);
};

PhoneNumber.prototype.toString = function() {
    return `(${this.areaCode()}) ${this.phoneNumber.slice(3, 6)}-${this.phoneNumber.slice(6,10)}`;
};



module.exports = PhoneNumber;