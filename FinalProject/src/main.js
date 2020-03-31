let fs = require( 'fs');
let { stopwords } = require('./stopwords');
let { removeSpecialElement } = require('./removeSpecialElement');
let { startTokerization } = require('./tokerization');
let { sintaticAnalyzer } = require('./sintaticAnalyzer');
let DOMParser = require('dom-parser');
let parser = new DOMParser();

//Vetor para armazenar todos os nomes dos arquivos lidos
let logfinalWord = [];

fs.readFile('./Tests/test01','utf8', async function(err,data){
    
    //Enviando para o console o resultado da leitura
    let arrayWords = data.split(' ');
    console.log('## ENTRADA ##');
    console.log(arrayWords);

    //pega um elemento do array e coloca todas as letras em caixa baixa.
    logfinalWord = removeSpecialElement(arrayWords);
    console.log('## CARACTERES ESPECIAIS REMOVIDOS ##');
    console.log(logfinalWord);
    
    // Removendo os artigos e preposições básicos.
    logfinalWord = stopwords(logfinalWord);
    console.log('## ARTIGOS E PREPOSIÇÕES BÁSICOS REMOVIDOS ##');
    console.log(logfinalWord);

    logfinalWord = await startTokerization(logfinalWord);
    console.log('## TOKERIZAÇÃO ##');
    console.log(logfinalWord);

    // bag of words.
    console.log('## TOTAL DE PALAVRAS ##');
    console.log(logfinalWord.length);

    console.log('## VERIFICANDO SINTAXE ##');
    sintaticAnalyzer(logfinalWord);
    return;

});