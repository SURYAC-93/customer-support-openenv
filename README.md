# AI Customer Support Agent (OpenEnv)

## Overview
This project simulates an AI-powered customer support agent that interacts with a custom environment to resolve user issues.

The agent performs tasks such as:
- Classifying customer queries
- Responding with appropriate solutions
- Closing resolved tickets

## Features
- Multi-task environment (easy, medium, hard)
- Reward-based evaluation system
- AI-driven decision making using LLM
- Dockerized for portability

## Tasks
- Easy: Refund policy inquiry
- Medium: Payment failure issue
- Hard: Angry customer escalation

## Reward System
- Keyword matching (refund/payment)
- Action sequencing (classify → reply → close)
- Penalties for repetition

## How to Run

### Local