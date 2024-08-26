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

O resultado do scan pode ser visto na url. Como o modelo abaixo:
    {
        "host": "testasp.vulnweb.com",
        "host_ip": "44.238.29.244",
        "open_ports": {
            "80": "HTTP"
        }
    }

Além disso, é imprimido no terminal o status de cada porta (open/closed) e seu serviço caso esteja aberta.

**Fontes**
Projetos utilizados como base para montar o programa e a base de dados.
* https://github.com/filipe1417/python-portscan-rapido/blob/main/portScan.py 
* https://medium.com/@wizD/a-simple-port-scanner-using-python-e541454ea570
* https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml