const sintaticAnalyzer = (log) => {
    analizer = new Analyzer(log);
    analizer.startAnalyzer();
}

class Analyzer {

    constructor(log) {
        this.log = log;
        this.pos = 0;
    }

    next = () => {
        this.pos += 1;
    }

    startAnalyzer = () => {
        if(this.log.length > 0 ) {

            if(this.log[this.pos][1] != 'substantivo' && this.log[this.pos][1] != 'verbo') {
                return console.error('Esperado um substantivo ou um verbo. ' + this.log[this.pos][1] + ' não experado.');
            }
            this._grammaticalClassAnalyzer(this.log[this.pos][1]);
        }
    }

    _grammaticalClassAnalyzer = (gramClass) => {
        if(this.pos + 1 == this.log.length) {
            console.log("## SINTAXE GRAMATICAL APROVADA ##");
            return true;
        }

        switch(gramClass) {
            case 'verbo':
                this._verbo();
                break;

            case 'substantivo':
                this._substantivo();
                break;

            case 'adjetivo':
                this._adjetivo();
                break;

            case 'advérbio':
                this._adverbio();
                break;

            case 'pronome indefinido':
                this._pronomeIndefinido();
                break;

            case 'caracter especial':
                this._caracterEspecial();
                break;
            default:
                console.error('Classe gramatical desconhecida.');
                return false;
        }
    }

    _verbo = () => {
        this.next();

        if(this.log[this.pos][1] != 'substantivo' && this.log[this.pos][1] != 'verbo' && this.log[this.pos][1] != 'advérbio'
        && this.log[this.pos][1] != 'adjetivo'  && this.log[this.pos][1] != 'caracter especial' && this.log[this.pos][1] != 'pronome indefinido') {
            return console.error(this.log[this.pos][1] + ' não experado depois de um '+ this.log[this.pos-1][1]);
        }
        this._grammaticalClassAnalyzer(this.log[this.pos][1]);
    }

    _substantivo = () => {
        this.next();

        if(this.log[this.pos][1] != 'substantivo' && this.log[this.pos][1] != 'verbo' && this.log[this.pos][1] != 'caracter especial' && this.log[this.pos][1] != 'adjetivo') {
            return console.error(this.log[this.pos][1] + ' não experado depois de um '+ this.log[this.pos-1][1]);
        }
        this._grammaticalClassAnalyzer(this.log[this.pos][1]);
    }

    _adjetivo = () => {
        this.next();

        if(this.log[this.pos][1] != 'substantivo' && this.log[this.pos][1] != 'caracter especial' && this.log[this.pos][1] != 'adjetivo') {
            return console.error(this.log[this.pos][1] + ' não experado depois de um '+ this.log[this.pos-1][1]);
        }
        this._grammaticalClassAnalyzer(this.log[this.pos][1]);
    }

    _adverbio = () => {
        this.next();

        if(this.log[this.pos][1] != 'verbo') {
            return console.error(this.log[this.pos][1] + ' não experado depois de um '+ this.log[this.pos-1][1]);
        }
        this._grammaticalClassAnalyzer(this.log[this.pos][1]);
    }

    _pronomeIndefinido = () => {
        this.next();

        if(this.log[this.pos][1] != 'substantivo') {
            return console.error(this.log[this.pos][1] + ' não experado depois de um '+ this.log[this.pos-1][1]);
        }
        this._grammaticalClassAnalyzer(this.log[this.pos][1]);
    }

    _caracterEspecial = () => {
        this.next();

        if(this.log[this.pos][1] != 'substantivo' && this.log[this.pos][1] != 'verbo' && this.log[this.pos][1] != 'advérbio' && this.log[this.pos][1] != 'adjetivo') {
            return console.error(this.log[this.pos][1] + ' não experado depois de um '+ this.log[this.pos-1][1]);
        }
        this._grammaticalClassAnalyzer(this.log[this.pos][1]);
    }

}

module.exports = { sintaticAnalyzer };