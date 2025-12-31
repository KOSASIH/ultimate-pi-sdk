import pytest
import asyncio
from pi_coin.core.transaction import Transaction, process_batch_transactions

@pytest.mark.asyncio
async def test_transaction_process():
    tx = Transaction("sender", "receiver", 1.0, "mining")
    result = await tx.process()
    assert result == True
    assert tx.status == "completed"

@pytest.mark.asyncio
async def test_batch_transactions():
    txs = [Transaction("a", "b", 1.0), Transaction("c", "d", 2.0)]
    results = await process_batch_transactions(txs)
    assert all(results) == True
