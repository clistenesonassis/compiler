// retorna a classe gramatical da palavra.
function readXML(data) {

    xmlDoc = parser.parseFromString(data, "text/xml")

    // Armazena na var registro o conteudo de uma tag "doc"
    entry = xmlDoc.getElementsByTagName("entry")[0];

    // Armazena na var registro o conteudo de uma tag "doc"
    gramGrp = entry.getElementsByTagName("gramGrp");

    let arrayGramGrp = [];

    for(var i in gramGrp) {
        arrayGramGrp.push(gramGrp[i].firstChild.textContent);
    }

    return arrayGramGrp.toString();
}

module.exports = { readXML };