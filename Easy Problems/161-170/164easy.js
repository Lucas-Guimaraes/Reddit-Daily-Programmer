//https://www.reddit.com/r/dailyprogrammer/comments/26ijiu/5262014_challenge_164_easy_assemble_this_scheme/

//Function #1: returns Hello World
function helloworld() {
	return "Hello World";
}

//#2: Returns every number from 1 to 100 divisible by 3 and 5
function fizzbuzz() {
	const fb_array = [];
	for (let i = 1; i < 101; i++) {
		if(i % 3 == 0 && i % 5 == 0) {
			fb_array.push(i);
		}
	}
  		
  return fb_array
}

//#3: Takes two words and checks if they're both anagrams
function anagram_checker(a, b) {
	var y = a.split("").sort().join("");
	var z = b.split("").sort().join("");
	if (z === y){
		return 'True'
	}
	else{
		return 'False'
	}
}

//#4: Takes word and letter, removes letter
function remove_letter(word, letter) {
	{
		return word.replace(letter, '')
	}
}
//Accum = Accumulator, curVal = currentValue
const reducer = (accum, curVal) => accum + curVal;
//Function #5: sums all numbers
function sum_array(arr) {
	return arr.reduce(reducer)
}

//calling functions to test
console.log(helloworld());
console.log(fizzbuzz());
console.log(anagram_checker("hello", "ellho"));
console.log(sum_array([3, 4, 1, 5, 6]));
console.log(remove_letter('hello', 'h'))