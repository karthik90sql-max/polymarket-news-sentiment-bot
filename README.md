# Polymarket News Sentiment Bot

A beginner-friendly Python project that collects public news headlines and Polymarket market data, with the long-term goal of comparing sentiment signals to market probabilities.

## Current Scope
This version is read-only and does not place trades.

It currently:
- fetches RSS news headlines
- fetches public Polymarket market data
- stores raw JSON locally
- prints sample outputs

## Project Goal
Later phases will add:
- sentiment scoring
- topic matching
- signal generation
- dashboards and alerts
- optional paper trading

## Setup
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py