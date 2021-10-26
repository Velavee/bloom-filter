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

def add_to_map(a_map, sha1_hash, md5_hash, blake2b_hash):
    a_map[sha1_hash] = 1
    a_map[md5_hash] =  1
    a_map[blake2b_hash] = 1


def create_map(dictionary):
    password_dict = {}

    for line in dictionary:
        sha1_hash = create_sha1_hash(line)
        md5_hash = create_md5_hash(line)
        blake2b_hash = create_blake3_hash(line)

        add_to_map(password_dict, sha1_hash, md5_hash, blake2b_hash)

    return password_dict


def main():
    dict = open('dictionary.txt', 'r')
    password_dict = create_map(dict)

if __name__ == '__main__':
    main()