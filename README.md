# CALIS: AI-Driven Context-Aware Encryption for SDN-Enabled Smart-Home IoT

[![Paper](https://img.shields.io/badge/Paper-Journal%20Article-blue)](https://rdcu.be/fd4dN)
[![DOI](https://img.shields.io/badge/DOI-10.1007%2Fs44443--025--00404--9-green)](https://doi.org/10.1007/s44443-025-00404-9)
[![Code](https://img.shields.io/badge/Code-GitHub-black)](https://github.com/eseinctz/calis)

---

## Authors

**Ezekia Gilliard**, **Jinshuo Liu**

*Journal of King Saud University Computer and Information Sciences (2026)*

---

## Overview

CALIS is an AI-driven, context-aware encryption framework designed for Software-Defined Networking (SDN)-enabled smart-home IoT environments. It dynamically selects lightweight authenticated encryption algorithms and adaptive key-rotation intervals using real-time device and network telemetry. By integrating SDN control, machine learning, and lightweight cryptography, CALIS achieves strong security guarantees while significantly improving efficiency in resource-constrained IoT systems.

---

## Abstract

Smart-home IoT devices face tight memory, energy, and latency budgets, yet deployments still apply a single heavyweight cipher and fixed key lifetimes to all flows. We introduce CALIS, an SDN-based, AI-driven framework that uses real-time device/network telemetry to select, per flow, a lightweight AEAD cipher (ASCON-128, AES-128-GCM, or ChaCha20-Poly1305) and an adaptive key-rotation interval. A compact gradient-boosting policy (XGBoost) executes at the controller and enforces decisions through standard SDN rules; mutual authentication and ECDH handle key establishment. Using a Raspberry Pi smart-home testbed and a public multi-device traffic corpus, CALIS reduced memory footprint by 86%, energy consumption by 58%, execution time by 58%, and communication overhead by 50% versus a static AES-256 baseline. Formal PySMT/Z3 verification under a Dolev–Yao adversary confirmed secrecy and authentication in all modeled scenarios with solver times less than 1 ms. Ablation studies show that disabling adaptive rotation or ML decisions consistently degrades efficiency. These results demonstrate that controller-side, context-aware crypto agility and adaptive key freshness can deliver substantial resource savings without weakening security.

---

## 📄 Paper

* 🔗 **Read the paper:** https://rdcu.be/fd4dN
* 📥 **DOI link:** https://doi.org/10.1007/s44443-025-00404-9
* 💻 **Code repository:** https://github.com/eseinctz/calis

---

## Keywords

Software-defined networking · Context-aware encryption · Lightweight AEAD · Adaptive key rotation · Smart-home IoT · Artificial intelligence

---

## Features

* AI-driven encryption selection per network flow
* Adaptive key-rotation mechanism based on real-time context
* Lightweight AEAD support (ASCON-128, AES-128-GCM, ChaCha20-Poly1305)
* SDN-based enforcement through controller-level control
* Formal verification using PySMT/Z3 under a Dolev–Yao adversary model
* Significant reductions in memory, energy, latency, and communication overhead

---

## Installation

### Requirements

Python 3.6+

### Install dependencies

```bash
pip install -r requirements.txt
```
```bash
pysmt-install --z3
```
### Clone repository

```bash
git clone https://github.com/eseinctz/calis.git
cd calis
```

---

## Citation

If you use this work, please cite:

### BibTeX

```bibtex
@article{Gilliard2026,
  title   = {CALIS: AI-driven context-aware encryption for SDN-enabled smart-home IoT},
  author  = {Gilliard, Ezekia and Liu, Jinshuo},
  journal = {Journal of King Saud University Computer and Information Sciences},
  year    = {2026},
  doi     = {10.1007/s44443-025-00404-9},
  url     = {https://rdcu.be/fd4dN},
  issn    = {2213-1248}
}
```

### Plain Text

Gilliard, E., & Liu, J. (2026). *CALIS: AI-driven context-aware encryption for SDN-enabled smart-home IoT*. Journal of King Saud University Computer and Information Sciences. https://doi.org/10.1007/s44443-025-00404-9

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
