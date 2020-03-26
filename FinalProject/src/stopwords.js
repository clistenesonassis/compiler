let artigos = ['o', 'a', 'os', 'as'];
let preposicao = ['da', 'de', 'do', 'das', 'dos'];
let arrayFinal = [];

// remove os artigos, conjunções e 
const stopwords = (array) => {

    array.map((element) => {
        if( !(artigos.includes(element) || preposicao.includes(element)) ) {
            arrayFinal.push(element);
        }
    });

    return arrayFinal;
}

module.exports = { stopwords };