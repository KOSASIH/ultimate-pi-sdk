# /pi_coin/examples/service_example.py
"""
Pi Coin Service Provider Example - Ultimate Hyper-Tech Service Simulation
Features: AI-Optimized Rates, Real-Time Wage Calculations, Transaction Processing, Ecosystem Integration.
"""

import asyncio
from pi_coin.core.stablecoin import PiCoin
from pi_coin.core.verification import verify_origin
from pi_coin.core.transaction import Transaction
from pi_coin.core.ecosystem import ServiceProvider, dashboard
from pi_coin.utils.config import config_manager

async def run_service_simulation():
    """
    Simulate a service provider using Pi Coin for wages.
    - Set AI-adjusted rates.
    - Calculate and process payments.
    - Log to ecosystem dashboard.
    """
    print("=== Pi Coin Service Provider Simulation ===")
    
    # Initialize Service Provider
    freelancer = ServiceProvider("PiDev Freelancer")
    
    # Set rates with ecosystem standardization
    freelancer.set_rate("Coding", 0.0001)  # PI per hour
    freelancer.set_rate("Design", 0.00008)
    
    print(f"Service Rates: {freelancer.services}")
    
    # Simulate client hiring for 10 hours of coding
    hours = 10
    service = "Coding"
    total_pi = freelancer.calculate_payment(service, hours)
    print(f"Total Payment for {hours} hours: {total_pi} PI (${total_pi * config_manager.get_pi_adjusted_value()})")
    
    # Client pays with verified PI
    client_pi = PiCoin(total_pi, "rewards")  # From rewards
    if verify_origin("rewards", client_pi.coin_id, client_pi.amount_pi):
        print(f"Verified Client PI: {client_pi.amount_pi} PI")
        
        # Process transaction
        tx = Transaction("client", "PiDev Freelancer", total_pi, "rewards")
        success = await tx.process()
        if success:
            print(f"Payment Completed: {tx.tx_id}")
            dashboard.log_transaction(tx)
        else:
            print("Payment Failed")
    else:
        print("PI Origin Rejected")
    
    # Ecosystem Analytics
    analytics = dashboard.get_analytics()
    print(f"Ecosystem Analytics: {analytics}")
    
    # Config Adjustment
    config_manager.ai_adjust_config({"anomaly_rate": 0.02})
    print(f"Updated PI Value: ${config_manager.get_pi_adjusted_value()}")

# Example Usage (Run this to test)
if __name__ == "__main__":
    asyncio.run(run_service_simulation())
