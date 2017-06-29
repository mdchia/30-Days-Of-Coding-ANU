process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function main() {
    var m_temp = readLine().split(' ');
    var m = parseInt(m_temp[0]);
    var n = parseInt(m_temp[1]);
    magazine = readLine().split(' ');
    ransom = readLine().split(' ');
    if (n>m){ // Check that we have enough words in the magazine to start with
        process.stdout.write("No");
        return false;
    }
    for (var i = 0, len = ransom.length; i < len; i++) { // Loop through all ransom words
        var mag_word = magazine.indexOf(ransom[i]);
        if (mag_word===-1){ // if we can't find the word
            process.stdout.write("No");
            return false;
        } else { // else remove the word once
            magazine.splice(mag_word, 1);
        }
    }
    process.stdout.write("Yes");
    return true;
}
