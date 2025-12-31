import pytest
from pi_coin.core.stablecoin import PiCoin

def test_pi_coin_creation():
    PiCoin.reset_supply()  # Reset for test
    coin = PiCoin(5.0, "mining")
    assert coin.convert_to_usd() == 5.0 * 314159
    assert coin.verify_signature() == True

def test_supply_cap():
    PiCoin.reset_supply()
    with pytest.raises(OverflowError):
        PiCoin(100_000_000_001, "mining")  # Exceeds cap

def test_invalid_source():
    with pytest.raises(ValueError):
        PiCoin(1.0, "exchange")  # Invalid source
