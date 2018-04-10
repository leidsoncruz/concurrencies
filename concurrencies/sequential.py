import time
import sys

import requests

SHOWS = ['deus-salve-o-rei', 'malhacao', 'o-outro-lado-do-paraiso', 'orgulho-e-paixao']


def get_shows():
    for i in sorted(SHOWS):
        resp = requests.get('http://localhost:5000/{0}'.format(i))
        print(i)
        print(resp.json()['data-hoje'])
        print("=========================")
        for j in resp.json().get('anterior').get('cenas'):
            print(j.get('titulo'))

        print("=========================")

def main():
    now = time.time()
    get_shows()
    elapsed = time.time() - now
    msg = '\n{} shows downloaded in {:.2f}s'
    print(msg.format(len(SHOWS), elapsed))


if __name__ == '__main__':
    main()
