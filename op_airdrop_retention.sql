-- Query Name: OP Airdrop Retention & Behavioral Profiling
-- Description: Analyzes the retention rate of Optimism (OP) airdrop receivers 
--              and profiles their behavior (Diamond Hands vs Dumpers).
-- =========================================================================

-- STEP 1: Identify Target Wallets (Airdrop Receivers)
WITH claims AS (
    SELECT 
        'OP' as protocol,
        recipient as wallet,
        amount_original as amount_claimed,
        block_time as claim_time
    FROM airdrop.claims
    WHERE token_symbol = 'OP'
      AND airdrop_number = 1  
      AND amount_original > 10  -- Filter out 'dust' (very small amounts)
      AND block_time >= TIMESTAMP '2022-05-31'
      AND block_time < TIMESTAMP '2022-06-30'
),

-- STEP 2: Track Dump Behavior (DEX Sales)
dex_sales AS (
    SELECT 
        taker as wallet,
        SUM(token_sold_amount) as amount_sold_dex
    FROM dex_optimism.trades
    WHERE token_sold_address = 0x4200000000000000000000000000000000000042 -- OP Token Smart Contract
      AND taker IN (SELECT wallet FROM claims) -- ONLY look at airdrop receivers
    GROUP BY 1
),

-- STEP 3: Business Logic & Behavioral Profiling
analysis AS (
    SELECT 
        c.wallet,
        c.amount_claimed,
        COALESCE(d.amount_sold_dex, 0) as total_sold,
        
        -- Calculate percentage sold (safeguard to max 100%)
        LEAST(COALESCE(d.amount_sold_dex, 0) / c.amount_claimed * 100, 100) as pct_sold
        
    FROM claims c
    LEFT JOIN dex_sales d ON c.wallet = d.wallet
)

-- STEP 4: Final Output with Psychological Labels
SELECT 
    wallet,
    amount_claimed,
    total_sold,
    pct_sold,
    
    -- Categorize wallets based on their sell pressure
    CASE 
        WHEN pct_sold < 5 THEN 'Diamond Hands 💎'
        WHEN pct_sold < 50 THEN 'Strong Holder 🛡️'
        WHEN pct_sold < 90 THEN 'Partial Seller ⚖️'
        ELSE 'Full Dumper 🏃‍♂️'
    END as behavior_profile
    
FROM analysis
ORDER BY amount_claimed DESC
LIMIT 2500 -- Take top 2500 receivers for Python API processing