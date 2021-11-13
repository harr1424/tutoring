# This script will compare two hashsums and output true if they match, else false

download = "3ee4e9145b0545ba4e5c47b89b64bc558c8eeb7887d260b3bd30f6a215029964"

signature = "3ee4e9145b0545ba4e5c47b89b64bc558c8eeb7887d260b3bd30f6a215029964"

def verify(hash1, hash2):
    authentic = False

    for i in range(len(download)):
        if download[i] == signature[i]:
            authentic = True
        else:
            return False

    return authentic

print("Hash is verified: : ",verify(download, signature))
