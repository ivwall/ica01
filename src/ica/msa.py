from bitcoin import *

private_key = random_key()
print (" private key : ", private_key)

public_key = privtopub( private_key )
print("  public key : ", public_key )
