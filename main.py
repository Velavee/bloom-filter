import hashlib

def create_sha1_hash(word):
    bytes_word = bytes(word, 'utf-8')
    hash_setup = hashlib.sha1()
    hash_setup.update(bytes_word)
    return hash_setup

def create_md5_hash(word):
    bytes_word = bytes(word, 'utf-8')
    hash_setup = hashlib.md5()
    hash_setup.update(bytes_word)
    return hash_setup

def create_blake3_hash(word):
    bytes_word = bytes(word, 'utf-8')
    hash_setup = hashlib.blake2b()
    hash_setup.update(bytes_word)
    return hash_setup

def create_map(dictionary):
    for line in dictionary:
        sha1_hash = create_sha1_hash(line)
        md5_hash = create_md5_hash(line)
        blake2b_hash = create_blake3_hash(line)


def main():
    dict = open('dictionary.txt', 'r')
    create_map(dict)

if __name__ == '__main__':
    main()