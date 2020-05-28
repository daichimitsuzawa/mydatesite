'use strict'

const maleNumberInput = document.getElementById('search-text-male');
const femaleNumberInput = document.getElementById('search-text-female');
const situationInput = document.getElementById('search-text-situation');
const timeLeftInput = document.getElementById('time-text-left');
const timeRightInput = document.getElementById('time-text-right');

function removeAllChildren(element) {
    while (element.firstChild) { element.removeChild }
}