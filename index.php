<?php

// URL da API
$apiUrl = 'https://api.exemplo.com/dados';

// opções para a chamada à API
$options = [
    'http' => [
        'method' => 'GET',
        'header' => 'Content-type: application/x-www-form-urlencoded\r\n',
    ],
];

// cria o contexto de stream
$context = stream_context_create($options);

// faz a chamada à API e armazena a resposta em uma variável
$response = file_get_contents($apiUrl, false, $context);

// imprime os dados de resposta
print_r($response);

?>
<!--                        -----2                             -->

<?php

// URL da API
$apiUrl = 'https://api.exemplo.com/dados';

// inicializa o curl
$curl = curl_init();

// define as opções para a chamada à API
curl_setopt($curl, CURLOPT_URL, $apiUrl);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_FOLLOWLOCATION, true);

// faz a chamada à API e armazena a resposta em uma variável
$response = curl_exec($curl);

// fecha a conexão curl
curl_close($curl);

// imprime os dados de resposta
print_r($response);

?>
