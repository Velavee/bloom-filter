from hashing import *

def add_to_map(a_map, sha1_hash, md5_hash, blake2b_hash):
    a_map[sha1_hash] = 1
    a_map[md5_hash] =  1
    a_map[blake2b_hash] = 1


def create_map(dictionary):
    password_dict = {}

    for line in dictionary:
        line_hashes = Word_Hashes(line)
        sha1_hash = line_hashes.create_sha1_hash()
        md5_hash = line_hashes.create_md5_hash()
        blake2b_hash = line_hashes.create_blake3_hash()

        add_to_map(password_dict, sha1_hash, md5_hash, blake2b_hash)

    return password_dict

def check_map(hash, password_map):
    if password_map.get(hash) == 1:
        return True

    return False

def process_input(input_list, password_hashes):
    input_num = int(input_list.readline())

    for x in range(input_num):
        password = input_list.readline()
        hashes = Word_Hashes(password)
        sha1_hash = hashes.create_sha1_hash()
        md5_hash = hashes.create_md5_hash()
        blake2b_hash = hashes.create_blake3_hash()

        if check_map(sha1_hash, password_hashes) and check_map(md5_hash, password_hashes) and check_map(blake2b_hash, password_hashes):
            print('maybe')
            continue

        print('no')


def main():
    dict = open('dictionary.txt', 'r')
    password_dict = create_map(dict)

    input = open('sample_input.txt', 'r')
    process_input(input, password_dict)


if __name__ == '__main__':
    main()