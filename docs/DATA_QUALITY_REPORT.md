# Data Quality Report — NYC Yellow Taxi 2023

**Generated:** 2026-05-06
**Source:** [NYC TLC Trip Records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

## Executive Summary

Of 38,310,226 raw trips, **2,726,335 (7.12%) were removed** during cleaning.

**Critical finding:** Data quality is **non-stationary** — significantly worse 
in Q4 2023 (Sept-Dec), which could bias time series models if uncorrected.

## Cleaning Pipeline Results

| Filter | Removed | % | Severity |
|--------|--------:|--:|---------|
| Non-positive amount | 382,882 | 1.00% | Standard |
| Non-positive distance | 728,205 | 1.90% | **Non-stationary** ⚠️ |
| Non-positive duration | 3,262 | 0.01% | Edge case |
| Duration > 12h | 28,770 | 0.08% | Forgotten meter |
| Missing/zero passengers | 1,583,150 | 4.13% | **Non-stationary** ⚠️ |
| Year ≠ 2023 | 66 | 0.0002% | Clock errors |

## Critical Finding #1: Zero Distance Trend

Zero-distance trips show a **clear systematic increase from September 2023**:

| Month | Zero Distance | Ratio vs Jan |
|------:|--------------:|-------------:|
| Jan | 45,861 | 1.0x |
| Mar | 48,450 | 1.1x |
| Jun | 47,472 | 1.0x |
| **Sep** | **98,546** | **2.15x** ⚠️ |
| **Oct** | **121,689** | **2.65x** ⚠️ |
| Nov | 102,667 | 2.24x |
| Dec | 73,333 | 1.60x |

**Hypothesis:** Vendor software update or new device deployment in Sept 2023.

## Critical Finding #2: Passenger Count Reliability

NaN passenger counts spike from September:
- Jan: 71,743 NaN
- Aug: 87,886 NaN
- **Sep: 140,225** (+59%)
- **Dec: 180,003** (+150% vs Jan)

The **same months** show issues across both fields → likely same root cause.

## Critical Finding #3: "Forgotten Meter" Trips

28,770 trips lasted > 12 hours. Pattern analysis:
- 80%+ have **$4.50 base fare and 0 distance**
- Likely: driver forgot to press "trip end"
- These are NOT real trips, but **system stuck states**

## Modeling Implications

**Risk:** If we drop more rows in Q4 than Q1, the **modeled time series** 
will show artificially lower demand in Q4 — a **data quality artifact**, 
not real seasonality.

**Mitigations:**
1. Apply identical cleaning rules across all months (we do this) ✓
2. Consider hourly aggregation tolerance: a few % missing per hour 
   should not significantly bias the count
3. Document for downstream consumers

## Decisions

- ✅ Drop all 7.12% rather than impute (small enough)
- ✅ Apply rules globally (not per-month)
- ✅ Aggregate to hourly level (smooths individual record loss)
- ⏳ Future: investigate VendorID correlation with anomalies (currently `VendorID` not retained)