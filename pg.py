# -*- coding: utf-8 -*-
import hashlib

class PasswordGenerator:
    def __init__(self, master = 'password', domain = 'domain'):
        self.__seed = master + domain

    def __gen_password(self, method):
        if method in ('MD5', 'md5'):
            return hashlib.md5(self.__seed).hexdigest()
        elif method in ('SHA256', 'sha256'):
            return hashlib.sha256(self.__seed).hexdigest()
        elif method in ('SHA224', 'sha224'):
            return hashlib.sha224(self.__seed).hexdigest()
        elif method in ('SHA512', 'sha512'):
            return hashlib.sha512(self.__seed).hexdigest()
        elif method in ('SHA384', 'sha384'):
            return hashlib.sha384(self.__seed).hexdigest()
        else:
            return hashlib.sha1(self.__seed).hexdigest()

    def get_password(self, method = 'sha1', limit = 50):
        return self.__gen_password(method)[:limit]

def main():
    p = PasswordGenerator(master = 'ê≥ç_', domain = 'facebook')
    print p.get_password()

if __name__ == '__main__':
    main()
