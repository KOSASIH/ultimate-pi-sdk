# /pi_coin/examples/merchant_example.py
"""
Pi Coin Merchant Example - Ultimate Hyper-Tech Merchant Simulation
Features: AI Pricing, Real-Time Transactions, Ecosystem Analytics, Verification Integration.
"""

import asyncio
from pi_coin.core.stablecoin import PiCoin
from pi_coin.core.verification import verify_origin
from pi_coin.core.transaction import Transaction
from pi_coin.core.ecosystem import Merchant, dashboard
from pi_coin.utils.config import config_manager

async def run_merchant_simulation():
    """
    Simulate a merchant shop using Pi Coin.
    - Set AI-adjusted prices.
    - Process verified transactions.
    - Log to ecosystem dashboard.
    """
    print("=== Pi Coin Merchant Simulation ===")
    
    # Initialize Merchant
    shop = Merchant("PiTech Shop")
    
    # Set prices with AI adjustment
    shop.set_price("Laptop", 0.001)  # Base price in PI
    shop.set_price("Phone", 0.0005)
    
    print(f"Shop Prices: {shop.products}")
    
    # Simulate customer purchase
    customer_pi = PiCoin(0.001, "p2p")  # Customer has PI from P2P
    if verify_origin("p2p", customer_pi.coin_id, customer_pi.amount_pi):
        print(f"Verified Customer PI: {customer_pi.amount_pi} PI (${customer_pi.convert_to_usd()})")
        
        # Process transaction
        tx = Transaction("customer", "PiTech Shop", 0.001, "p2p")
        success = await tx.process()
        if success:
            print(f"Transaction Completed: {tx.tx_id}")
            dashboard.log_transaction(tx)
        else:
            print("Transaction Failed")
    else:
        print("PI Origin Rejected")
    
    # Ecosystem Analytics
    analytics = dashboard.get_analytics()
    print(f"Ecosystem Analytics: {analytics}")
    
    # Config Adjustment
    config_manager.ai_adjust_config({"anomaly_rate": 0.05})
    print(f"Updated PI Value: ${config_manager.get_pi_adjusted_value()}")

# Example Usage (Run this to test)
if __name__ == "__main__":
    asyncio.run(run_merchant_simulation())
