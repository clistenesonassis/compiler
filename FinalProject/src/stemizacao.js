const { apiGeneral } = require('../api/Api');
let specialCharacter = ['.', ',', ';', ':', '?', '!', '(', ')'];

const stemizacao = async (word) => {
    let gramClass = [];
    let rootWord = '';
    let wrapper = [];

    if( specialCharacter.includes(word) ) {
        return [word, ['caracter esp.']]
    }

    const response =  await apiGeneral.get(`/${word}`);
    let aux = response.data.split('<span class="varpt">', 2);

    rootWord = aux[1].split('</span>')[0];
    
    // verificar que existe mais alguma tag para retirar.
    if(rootWord[0] == '<') {
        let t1 = rootWord.split('>', 2)[1];
        rootWord = t1.split('<', 1);
    }

    // se for igual então a palavra retorna a classe gramatical correta.
    if(word == rootWord) {
        aux = aux[1].split('<em>');
        aux.shift();

        aux.map((value) => {
            gramClass.push(value.split('</em>')[0]);
        });
    }

    wrapper.push(rootWord.toString());
    wrapper.push(gramClass);
    console.log("stemização: " + word + ' - ', wrapper);
    return wrapper;
}

module.exports = { stemizacao };