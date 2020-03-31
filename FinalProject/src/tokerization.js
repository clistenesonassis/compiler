const { stemizacao } = require('./stemizacao');
let arrayFinal = [];
let gramClass = new Map();

// Classes Gramaticais //
gramClass.set('s. m.', 'substantivo');
gramClass.set('s. f.', 'substantivo');
gramClass.set('s. m. pl.', 'substantivo');
gramClass.set('v. tr.', 'verbo');
gramClass.set('v. intr.', 'verbo');
gramClass.set('v. pron.', 'verbo');
gramClass.set('v. cop.', 'verbo');
gramClass.set('v. auxil.', 'verbo');
gramClass.set('v. tr. e intr.', 'verbo');
gramClass.set('v. tr. e pron.', 'verbo');
gramClass.set('adj.', 'adjetivo');
gramClass.set('adj. 2 g.', 'adjetivo');
gramClass.set('adv.', 'advérbio');
gramClass.set('prep.', 'preposição');
gramClass.set('pron. indef.', 'pronome indefinido');
gramClass.set('caracter esp.', 'caracter especial');


// inicia o processo de tokerização.
const startTokerization = async (arrayWord) => {
    console.log('#### INICIANDO O PROCESSO DE TOKERIZAÇÃO ####');

    //Analisa a classe gramatical de cada palavra.
    for(var i in arrayWord) {
        await _queryWord(arrayWord[i]);
    }
    
    //atribui a classe gramatical por extenso.
    _token();

    console.log('#### PROCESSO DE TOKERIZAÇÃO FINALIZADO ####');
    return arrayFinal;
}

//Analisa a classe gramatical de cada palavra.
async function _queryWord(value) {
    //envia requisição para o servidor.
    let response = await stemizacao(value);
    
    //se falhou ao capturar a classe gramatical por não ter usado a palavra raiz. enviar uma nova requisição com a palavra raiz.
    if(response[0] != value && response[0] != '') {
        response = await stemizacao(response[0]);
    }

    //salva elemento.
    arrayFinal.push(response);
}

//atribui a classe gramatical por extenso.
function _token() {
    arrayFinal.map((value, indice) => {
        arrayFinal[indice][1] = gramClass.get(value[1][0]);
    });
}

module.exports = { startTokerization };