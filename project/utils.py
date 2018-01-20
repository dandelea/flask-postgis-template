
import hashlib

def hash(password):
	return hashlib.md5(p.encode('utf8')).hexdigest()