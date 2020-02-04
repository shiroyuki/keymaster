import hashlib


def compute_hash(content: str):
    h = hashlib.new('sha512')
    h.update(content.encode())
    return h.hexdigest()