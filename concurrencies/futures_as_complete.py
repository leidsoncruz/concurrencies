import time
import sys
from concurrent import futures

import requests

MAX_WORKERS = 4
SHOWS = ['deus-salve-o-rei', 'malhacao', 'o-outro-lado-do-paraiso', 'orgulho-e-paixao']

def get_show(show):
    resp = requests.get('http://127.0.0.1:5000/{0}'.format(show))
    print('______{}______'.format(show))
    print(resp.json()['data-hoje'])
    print("=========================")
    for i in resp.json().get('anterior').get('cenas'):
        print(i.get('titulo'))

    return show
    print("=========================")

def get_shows():
    futures_pending = []
    workers = min(MAX_WORKERS, len(SHOWS))

    with futures.ThreadPoolExecutor(workers) as executor:
        for show in sorted(SHOWS):
            future_submit = executor.submit(get_show, show)
            futures_pending.append(future_submit)
            print('FUTURE IS SUBMIT {}'.format(future_submit))

        for future in futures.as_completed(futures_pending):
            print('=====>RESULTADO DA FUTURE {}'.format(future.result()))
            future.result()



def main():
    now = time.time()
    get_shows()
    elapsed = time.time() - now
    msg = '\n{} shows downloaded in {:.2f}s'
    print(msg.format(len(SHOWS), elapsed))


if __name__ == '__main__':
    main()
