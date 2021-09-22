function pop() {
	var event = new KeyboardEvent('keydown', {key:'k'});
	document.dispatchEvent(event);
}

var intervalID = setInterval(pop, 1);