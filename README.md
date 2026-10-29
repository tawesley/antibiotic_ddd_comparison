# Antibiotic DDD Comparison

## Oral Defined Daily Doses of antibacterials vs other drug classes
This repository contains the analysis for the dose comparison discussed in Ta, W. & Stokes, J.M. *An honest exploration of what AI can and cannot do for antibiotic discovery*.

This analysis compares the World Health Organization (WHO) Defined Daily Doses (DDDs) of oral antibacterials (Anatomical Therapeutic Chemical (ATC) group J01) with those of oral drugs from three ATC anatomical main groups:
- Cardiovascular system (C)
- Nervous system (N)
- Antineoplastic and immunomodulating agents (L)

The DDD is the assumed average maintenance dose per day for a drug used for its main indication in adults. For this analysis, only DDDs expressed in mass (g, mg, mcg) are kept.

## Data
DDD values are publicly available from the WHO Collaborating Centre for Drug Statistics Methodology's ATC/DDD Index 2026 https://atcddd.fhi.no/atc_ddd_index/. The analysis uses a snapshot `WHO ATC-DDD 2026-04-25.csv`, sourced from ATCD (https://github.com/fabkury/atcd). 

Download [`WHO ATC-DDD 2026-04-25.csv`](https://github.com/fabkury/atcd/blob/3424336/WHO%20ATC-DDD%202026-04-25.csv)
(ATCD version of 9 June 2026) and place it in the same folder as the script.

## Usage

Install pandas and SciPy:

```bash
pip install pandas scipy
```

With `WHO ATC-DDD 2026-04-25.csv` in the same folder as the script:

```bash
python antibiotic_doses.py
```

## Expected output

```text
oral level-5 codes with a mass-unit DDD: 1657

             group   n  median_mg  iqr_lo   iqr_hi  gmean_mg  min_mg    max_mg
J01 antibacterials 136   1,000.00  437.50 1,575.00    840.81   75.00 12,000.00
 C  cardiovascular 247      40.00   10.00   200.00     40.81    0.10 20,000.00
 N  nervous system 351     100.00   18.00   300.00     77.06    0.10  7,500.00
 L  antineoplastic 127     150.00   20.00   400.00     78.19    0.30  2,400.00
```
