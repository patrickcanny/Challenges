// Author: Patrick Canny
//  r/dailyprogrammer - Defusing the Bomb
// To disarm the bomb you have to cut some wires. These wires are either white, black, purple, red, green or orange.
// The rules for disarming are simple:
//
// 1. If you cut a white cable you can't cut white or black cable.
// 2. If you cut a red cable you have to cut a green one
// 3. If you cut a black cable it is not allowed to cut a white, green or orange one
// 4. If you cut a orange cable you should cut a red or black one
// 5. If you cut a green one you have to cut a orange or white one
// 6. If you cut a purple cable you can't cut a purple, green, orange or white cable
//
// If you have anything wrong in the wrong order, the bomb will explode.
// There can be multiple wires with the same colour and these instructions are for one wire at a time.
// Once you cut a wire you can forget about the previous ones.

function diffuseBomb(input){
  let params = {
    white:    ['purple', 'green', 'red', 'orange'],
    red:       ['green'],
    black:    ['red','black','purple'],
    orange: ['red','black'],
    green:   ['orange', 'white'],
    purple:  ['black','red']
  };
  function lookAtWire(cut){
    let [current, next] = cut;
    return !next || params[current].includes(next) && diffuseBomb(cut.slice(1));
  }
  return lookAtWire(input.split('\n')) ? "Diffused" : "Boom";
}

console.log(diffuseBomb("white\nred\ngreen\nwhite"));
console.log(diffuseBomb("white\norange\ngreen\nwhite"));
