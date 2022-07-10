import sys
import logging
import requests
from os import environ

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger('google-ddns-sync')


def get_ip():
    logger.debug('Started finding gateway IP')

    response = requests.get('https://api64.ipify.org?format=json').json()
    ip = response["ip"]

    if not ip:
        logger.error(f'Could not find you gateway IP: {response.text}')
        sys.exit(1)

    logger.info(f'Your gateway IP is {ip}')
    logger.debug('Finished finding gateway IP')
    return ip


def main():
    ip = get_ip()

    response = requests.post(
        f'https://{environ["GMAIL_DDNS_USERNAME"]}:{environ["GMAIL_DDNS_PASSWORD"]}@domains.google.com/nic/update?hostname=hibbard.dev&myip={ip}'
    )

    if response.status_code != 200:
        logger.error(
            f'An error occurred when updating the Google DDNS: {response.text}')
        sys.exit(1)


if __name__ == '__main__':
    logger.info('Starting Google-DSN Integration')

    if 'GMAIL_DDNS_USERNAME' not in environ or 'GMAIL_DDNS_PASSWORD' not in environ:
        logger.error(
            'You must provide the GMAIL_DDNS_USERNAME and GMAIL_DDNS_PASSWORD.')
        sys.exit(1)

    main()

    logger.info('Finished Google-DDNS Integration')
