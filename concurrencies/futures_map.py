import time
import sys
from concurrent import futures

import requests

MAX_WORKERS = 4
SHOWS = ['deus-salve-o-rei', 'malhacao', 'o-outro-lado-do-paraiso', 'orgulho-e-paixao']

def get_show(show):
    resp = requests.get('http://127.0.0.1:5000/{0}'.format(show))
    print(show)
    print(resp.json()['data-hoje'])
    print("=========================")
    for i in resp.json().get('anterior').get('cenas'):
        print(i.get('titulo'))

    print("=========================")

def get_shows():
    # workers = 2
    # Estou usando map, mas poderia fazer um for fazendo com que o executor
    # use o .submit(get_show, show) e depois fazer um outro for para percorrer
    # as futures appendadas no for anterior e percorrer as dones através do
    # futures.as_completed([array appendado]) e colher seu resultado pelo
    # indice.result()

    # o que o executor.map faz: chama a função de forma concorrente a partir de
    # várias threads . Ele devolve

    workers = min(MAX_WORKERS, len(SHOWS))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(get_show, sorted(SHOWS))


def main():
    now = time.time()
    get_shows()
    elapsed = time.time() - now
    msg = '\n{} shows downloaded in {:.2f}s'
    print(msg.format(len(SHOWS), elapsed))


if __name__ == '__main__':
    main()
