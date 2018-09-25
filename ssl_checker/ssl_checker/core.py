# -*- coding: utf-8 -*-

import re
import socket
import ssl


PATTERN = '^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$'


class SSLChecker:

    hostname = None
    re_hostname = re.compile(PATTERN, re.IGNORECASE)

    def __init__(self, hostname):
        self.hostname = hostname

        if not self.validate_hostname():
            print('hostname is not valid')

        self.get_certificate()

    def validate_hostname(self):
        return bool(self.re_hostname.match(self.hostname))

    def get_certificate(self):
        context = ssl.create_default_context()

        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=self.hostname)
        try:
            conn.connect((self.hostname, 443))
            certificate = conn.getpeercert()
            print('Valid until {}'.format(certificate.get('notAfter')))

        except ssl.CertificateError as error:
            print(error)

        except ssl.SSLError as error:
            print(error.reason)
            print('self signed or expired certificate')
