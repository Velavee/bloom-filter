from hashing import *
from dict_actions import *

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

    bloom_filter = Bloom_Filter_Dict(dict)
    bloom_filter.create_dict()

    input = open('sample_input.txt', 'r')
    process_input(input, bloom_filter.password_dict)


if __name__ == '__main__':
    main()