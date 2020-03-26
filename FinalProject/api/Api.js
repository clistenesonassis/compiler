const axios = require('axios');

const api = axios.create({
    baseURL: 'https://api.dicionario-aberto.net',
});

const apiGeneral = axios.create({
    baseURL: 'https://dicionario.priberam.org',
});



module.exports = {api, apiGeneral};