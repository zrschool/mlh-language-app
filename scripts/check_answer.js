var answer_choice = document.querySelector('input[name=answer]:checked').value;

console.log(answer_choice)

var answer = '';

if ('{{answer}}' == '\u3042') {
  answer = 'a';
} else if ('{{answer}}' == '\u3048') {
  answer = 'e';
} else if ('{{answer}}' == '\u3044') {
  answer = 'i';
} else if ('{{answer}}' == '\u3046') {
  answer = 'u';
} else {
  answer = 'e';
}

if (answer == answer_choice) {
  alert('Correct!');
} else {
  alert('Incorrect!');
}
