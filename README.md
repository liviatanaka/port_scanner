# port_scanner

Esse repositório contém uma aplicação que realiza o escaneamento de portas de comunicação de um destino.
Para rodar o programa basta rodar o arquivo `main.py` e acessar a url [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Na api, temos duas rotas. Uma para scan de url (sem o https://) e a outra para fazer o scan do IP. Ambas as rotas são `post` e possuem como entrada um json no seguinte formato.

    {
        "host": "string",
        "start_port": 0,
        "end_port": 0
    }

Exemplo de como fazer scan do endereço [testasp.vulnweb.com](testasp.vulnweb.com) da porta 1 a 100.

    {
        "host": "testasp.vulnweb.com",
        "start_port": 1,
        "end_port": 100
    }


**Fontes**
Projetos utilizados como base para montar o programa e a base de dados.
* https://github.com/filipe1417/python-portscan-rapido/blob/main/portScan.py 
* https://medium.com/@wizD/a-simple-port-scanner-using-python-e541454ea570
* https://www.geeksforgeeks.org/50-common-ports-you-should-know/
* https://www.ibm.com/docs/en/zos/2.4.0?topic=reference-well-known-port-assignments