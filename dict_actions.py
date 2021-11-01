from hashing import *

class Bloom_Filter_Dict:
    def __init__(self, common_passwords):
        self.password_dict = {}
        self.common_passwords = common_passwords

    def create_dict(self):
        for line in self.common_passwords:
            line_hashes = Word_Hashes(line)
            sha1_hash = line_hashes.create_sha1_hash()
            md5_hash = line_hashes.create_md5_hash()
            blake2b_hash = line_hashes.create_blake3_hash()

            self.add_to_dict(sha1_hash, md5_hash, blake2b_hash)

        return

    def add_to_dict(self, sha1_hash, md5_hash, blake2b_hash):
        self.password_dict[sha1_hash] = 1
        self.password_dict[md5_hash] = 1
        self.password_dict[blake2b_hash] = 1

    def check_dict(self, hash_val):
        if self.password_dict.get(hash_val) == 1:
            return True

        return False

