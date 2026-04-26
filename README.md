# 🪂 Web3 User Behavior: Optimism (OP) Airdrop Retention Analysis

## 📖 Business Context
Airdrops are a primary user acquisition strategy in Web3, costing protocols millions of dollars. However, the critical business question remains: **Does free money build loyal communities, or does it attract opportunistic 'Sybil' farmers who dump the token?**

This project investigates the retention rate and psychological behavior of wallets that received the Optimism ($OP) Airdrop (Round 1).

## 🛠️ Data Pipeline & Methodology
1. **Data Extraction (Dune Analytics & SQL):** - Extracted raw `airdrop.claims` data to identify target wallets.
   - Used `LEFT JOIN` on `dex.trades` to track which claiming wallets immediately sold their tokens on Decentralized Exchanges (DEXs).
2. **Data Ingestion:** Automated data pipeline using Python (`dune-client` API) to fetch live SQL results.
3. **Behavioral Profiling:** Categorized wallets based on sell pressure:
   - 💎 **Diamond Hands:** Sold < 5% of airdrop.
   - 🛡️ **Strong Holder:** Sold < 50% of airdrop.
   - ⚖️ **Partial Seller:** Sold < 90% of airdrop.
   - 🏃‍♂️ **Full Dumper:** Sold > 90% of airdrop.

## 📊 Visual Insights
*(Note: I built this Donut Chart using Python's Matplotlib to visualize the ratio of loyalists vs. opportunists).*

![OP Airdrop Retention]<img width="1486" height="1534" alt="image (2)" src="https://github.com/user-attachments/assets/59f7512d-c7a1-446b-9d25-2f20505a3ca6" />

## 💡 Business Conclusion & Recommendations
Based on the on-chain data analysis, the airdrop experienced significant immediate sell pressure. A large majority of the analyzed wallets fall into the **"Full Dumper"** category, having liquidated over 90% of their free tokens shortly after claiming. Conversely, only a smaller fraction demonstrated **"Diamond Hands"** loyalty.

**Strategic Recommendations for Future Airdrops:**
1. **Anti-Sybil Filtering:** The high dump rate suggests many wallets were opportunistic farmers rather than real users. Stricter on-chain identity (e.g., Gitcoin Passport) should be required.
2. **Vested Airdrops:** Instead of 100% unlocked tokens at Token Generation Event (TGE), protocols should implement linear vesting or "unlock-by-playing" mechanics to force users to interact with the ecosystem before they can sell.

---
