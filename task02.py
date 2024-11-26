import hashlib 

def hash_file(file_path):
    sha1_hash = hashlib.sha1()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha1_hash.update(chunk)
    return sha1_hash.hexdigest()

def compare_pdfs(file1, file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    if hash1 == hash2:
        print("The files are identical.")
    else:
        print("The files are different.")

pdf1 = "./File1.pdf"
pdf2 = "./File2.pdf"

compare_pdfs(pdf1, pdf2)
