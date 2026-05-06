# Time Series Forecasting Platform 🚖

> **A production-ready time series forecasting platform comparing SARIMAX, Prophet, and LightGBM on NYC taxi demand data.**

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-in%20development-orange.svg)]()

## Project Overview

This project builds an end-to-end time series forecasting platform that predicts NYC yellow taxi demand. The platform compares three modeling paradigms — classical statistical (SARIMAX), Bayesian decomposition (Prophet), and gradient boosting (LightGBM) — and exposes the best model via a FastAPI service, containerized with Docker.

**Why this project?** Demand forecasting is a real business problem: NYC taxi companies, ride-share platforms, and logistics firms need accurate hourly/daily demand predictions to optimize fleet allocation. This project demonstrates not just modeling, but the full ML lifecycle.

## Goals

- Compare three modeling approaches on the same dataset with the same evaluation protocol
- Deploy the best model as a REST API
- Containerize with Docker for reproducibility
- Add CI/CD via GitHub Actions
- Implement basic monitoring and model versioning

## Project Structure

```
.
├── configs/          # Configuration files (YAML)
├── data/
│   ├── raw/          # Original immutable data
│   ├── processed/    # Cleaned, transformed data
│   └── external/     # Third-party data (e.g., weather)
├── docs/             # Documentation
├── notebooks/        # Jupyter notebooks for exploration
├── scripts/          # Standalone scripts
├── src/
│   ├── data/         # Data loading and preprocessing
│   ├── features/     # Feature engineering
│   ├── models/       # Model training and evaluation
│   ├── api/          # FastAPI application
│   └── utils/        # Helper functions
└── tests/            # Unit and integration tests
```

## Getting Started

### Prerequisites

- Python 3.11+
- Conda (recommended)
- Git

### Installation

```bash
# Clone the repo
git clone https://github.com/daminabence/time-series-forecasting-platform.git
cd time-series-forecasting-platform

# Create environment
conda create -n tsf-platform python=3.11 -y
conda activate tsf-platform

# Install dependencies
pip install -r requirements.txt

# Download data
python scripts/download_data.py
```

## Dataset

**Source:** [NYC Taxi & Limousine Commission](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)  
**Period:** January 2023 – December 2023  
**Type:** Yellow Taxi Trip Records  
**Volume:** ~38M trips, ~2GB of data

## Roadmap

- [x] **Week 1:** Project setup + EDA
- [ ] **Week 2:** SARIMAX baseline
- [ ] **Week 3:** Prophet & LightGBM models
- [ ] **Week 4:** FastAPI + Docker deployment
- [ ] **Week 5:** Tests + CI/CD + monitoring
- [ ] **Week 6:** Cloud deploy + documentation

## References

- Hyndman, R.J., & Athanasopoulos, G. (2021) *Forecasting: principles and practice*, 3rd edition. [otexts.com/fpp3/](https://otexts.com/fpp3/)
- Huyen, C. (2022) *Designing Machine Learning Systems*. O'Reilly.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Author

**[Damina Bence]**
- GitHub: @daminabence(https://github.com/daminabence)