let specialCharacter = ['.', ',', ';', ':', '?', '!', '(', ')'];
let arrayFinal = [];


//pega um elemento do array e coloca todas as letras em caixa baixa.
removeSpecialElement = (arrayWords) => {

    arrayWords.map((element) => {
        _remove(element.toLowerCase());
    });

    return arrayFinal;
};


//remove os elementos especiais das palavras.
_remove = (element) => {
       
    //retira todos os \n dos elementos. retorna um array.
    let word = element.split('\n');

    // varre todo o array.
    word.map((value, indice) => {
        let special = false;

        //verifica se existe algum caracter na palavra, se tiver então é retirado.
        for(var i in value) {
            if(special) {
                throw `Error. Não é esperado "${value[i]}" depois de "${value[i-1]} na linha: ${indice + 1}"`;
            }

            if(specialCharacter.includes(value[i])) {
                let array = value.split(value[i]);
                arrayFinal.push(array[0]);
                arrayFinal.push(value[i]);
                special = true;
            }
        }

        if(!special) {
            arrayFinal.push(value);
        }

    });
};

module.exports = { removeSpecialElement };