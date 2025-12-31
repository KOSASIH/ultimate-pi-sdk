# Pi Coin API Reference - Ultimate Hyper-Tech API Docs

**Comprehensive API Reference for Pi Coin Stablecoin Module**

This reference covers all classes, functions, and utilities in the Pi Coin module. Each entry includes parameters, return types, and hyper-tech features (e.g., AI, quantum security). See `/examples/` for usage demos.

## Table of Contents
- [Core Module](#core-module)
- [Utils Module](#utils-module)
- [Ecosystem Module](#ecosystem-module)
- [Global Functions](#global-functions)

## Core Module
Located in `/pi_coin/core/`.

### PiCoin Class
**Location**: `core/stablecoin.py`  
**Description**: Represents a Pi Coin stablecoin instance with fixed value and supply tracking.  
**Hyper-Tech**: AI-modulated supply, quantum signatures.

- `__init__(amount_pi: float, source: str)`  
  Creates PI with amount and source. Enforces supply cap and verifies source.  
  - `amount_pi`: Amount in PI.  
  - `source`: Origin (e.g., "mining").  
  - Raises: `ValueError` for invalid source, `OverflowError` for supply exceed.

- `convert_to_usd() -> float`  
  Converts PI to fixed USD value ($314,159 per PI).

- `get_supply_status() -> dict`  
  Returns global supply metrics (current, remaining, utilization %).

- `verify_signature() -> bool`  
  Verifies quantum RSA signature.

**Example**:
```python
pi = PiCoin(10.0, "mining")
print(pi.convert_to_usd())  # 3141590.0
```

### Transaction Class
**Location**: `core/transaction.py`  
**Description**: Handles PI transactions with consensus and routing.  
**Hyper-Tech**: Async consensus, AI routing.

- `__init__(sender: str, receiver: str, amount_pi: float, source: str)`  
  Initializes transaction.  
  - `sender/receiver`: User IDs.  
  - `amount_pi`: Amount.  
  - `source`: Origin.

- `process() -> bool` (async)  
  Processes transaction with verification and consensus.

**Example**:
```python
tx = Transaction("a", "b", 1.0, "p2p")
await tx.process()
```

### Verification Functions
**Location**: `core/verification.py`  
**Description**: Origin verification with AI and quantum hashing.

- `verify_origin(source: str, pi_coin_id: str, amount: float, freq: int) -> bool`  
  Verifies PI origin.  
  - `source`: e.g., "mining".  
  - Returns: True if valid.

- `batch_verify(coins: list) -> list`  
  Batch verifies multiple coins.

**Example**:
```python
verify_origin("mining", "id123", 1.0)
```

## Utils Module
Located in `/pi_coin/utils/`.

### PiMath Class
**Location**: `utils/pi_math.py`  
**Description**: Pi computation utilities.  
**Hyper-Tech**: AI-optimized algorithms, quantum error correction.

- `generate_pi_chudnovsky(digits: int) -> str`  
  Generates Pi to specified digits.

- `benchmark_pi_generation(method: str, param: int) -> dict`  
  Benchmarks generation (time, accuracy).

**Example**:
```python
pi_math.generate_pi_chudnovsky(100)
```

### HashEngine Class
**Location**: `utils/hashing.py`  
**Description**: Hashing with AI selection and quantum signing.

- `compute_hash(data: str) -> str`  
  Computes hash with Pi entropy.

- `quantum_sign_hash(data: str) -> bytes`  
  Signs hash quantum-resistantly.

**Example**:
```python
hash_engine.compute_hash("data")
```

### ConfigManager Class
**Location**: `utils/config.py`  
**Description**: Dynamic config management.

- `ai_adjust_config(ecosystem_data: dict)`  
  AI adjusts settings.

- `get_pi_adjusted_value() -> float`  
  Gets tuned PI value.

**Example**:
```python
config_manager.ai_adjust_config({"anomaly_rate": 0.1})
```

## Ecosystem Module
Located in `/pi_coin/core/ecosystem.py`.

### Merchant Class
**Location**: `core/ecosystem.py`  
**Description**: Merchant pricing tools.

- `set_price(product: str, base_price_pi: float)`  
  Sets AI-adjusted price.

- `get_price_usd(product: str) -> float`  
  Gets USD price.

### ServiceProvider Class
**Location**: `core/ecosystem.py`  
**Description**: Service wage calculators.

- `set_rate(service: str, rate_pi: float)`  
  Sets rate.

- `calculate_payment(service: str, hours: float) -> float`  
  Calculates PI payment.

### EcosystemDashboard Class
**Location**: `core/ecosystem.py`  
**Description**: Analytics dashboard.

- `log_transaction(tx: Transaction)`  
  Logs transaction.

- `get_analytics() -> dict`  
  Returns metrics.

## Global Functions
From `__init__.py` and utils.

- `pi_based_hash(data: str) -> str`  
  Convenience hashing.

- `simulate_blockchain_transaction(data: dict) -> str` (async)  
  Mocks blockchain TX.

- `get_config(key: str)` / `set_config(key: str, value)`  
  Config access.

For full code, see source files. Report issues in the repo.
```
