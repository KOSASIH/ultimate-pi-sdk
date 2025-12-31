# /pi_coin/examples/p2p_example.py
"""
Pi Coin P2P Example - Ultimate Hyper-Tech P2P Simulation
Features: AI-Optimized Matching, Real-Time Consensus, Batch Transactions, Ecosystem Integration.
"""

import asyncio
from pi_coin.core.stablecoin import PiCoin
from pi_coin.core.verification import verify_origin, batch_verify
from pi_coin.core.transaction import Transaction, process_batch_transactions
from pi_coin.core.ecosystem import dashboard
from pi_coin.utils.config import config_manager

async def run_p2p_simulation():
    """
    Simulate P2P Pi Coin trading.
    - AI matches buyers/sellers.
    - Process verified batch transactions.
    - Log to ecosystem dashboard.
    """
    print("=== Pi Coin P2P Simulation ===")
    
    # Simulate P2P marketplace
    offers = [
        {"seller": "user1", "amount_pi": 5.0, "id": "offer1"},
        {"seller": "user2", "amount_pi": 3.0, "id": "offer2"},
        {"seller": "user3", "amount_pi": 1.0, "id": "offer3"}
    ]
    
    buyers = [
        {"buyer": "buyer1", "amount_pi": 5.0},
        {"buyer": "buyer2", "amount_pi": 3.0}
    ]
    
    # AI-Optimized Matching (Simple mock: Match by amount)
    matches = []
    for buyer in buyers:
        for offer in offers:
            if buyer["amount_pi"] == offer["amount_pi"]:
                matches.append({
                    "buyer": buyer["buyer"],
                    "seller": offer["seller"],
                    "amount_pi": buyer["amount_pi"],
                    "offer_id": offer["id"]
                })
                offers.remove(offer)  # Remove matched offer
                break
    
    print(f"AI Matched Trades: {matches}")
    
    # Batch Verify Origins
    verify_data = [{"source": "p2p", "id": match["offer_id"], "amount": match["amount_pi"]} for match in matches]
    verifications = batch_verify(verify_data)
    valid_matches = [match for match, valid in zip(matches, verifications) if valid]
    
    print(f"Verified Matches: {len(valid_matches)}/{len(matches)}")
    
    # Process Batch Transactions
    transactions = [Transaction(match["buyer"], match["seller"], match["amount_pi"], "p2p") for match in valid_matches]
    results = await process_batch_transactions(transactions)
    
    for i, (tx, success) in enumerate(zip(transactions, results)):
        if success:
            print(f"Trade {i+1} Completed: {tx.tx_id}")
            dashboard.log_transaction(tx)
        else:
            print(f"Trade {i+1} Failed")
    
    # Ecosystem Analytics
    analytics = dashboard.get_analytics()
    print(f"Ecosystem Analytics: {analytics}")
    
    # Config Adjustment
    config_manager.ai_adjust_config({"anomaly_rate": 0.03})
    print(f"Updated PI Value: ${config_manager.get_pi_adjusted_value()}")

# Example Usage (Run this to test)
if __name__ == "__main__":
    asyncio.run(run_p2p_simulation())
