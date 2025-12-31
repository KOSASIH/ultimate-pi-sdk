import pytest
from pi_coin import PI_SYMBOL, TOTAL_SUPPLY, pi_based_hash

def test_constants():
    assert PI_SYMBOL == "PI"
    assert TOTAL_SUPPLY == 100_000_000_000

def test_pi_hash():
    hash_val = pi_based_hash("test")
    assert len(hash_val) == 128  # SHA3-512 hex length
