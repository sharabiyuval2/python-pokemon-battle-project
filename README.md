# Pokemon Battle Project

This project is a Python implementation of a simple Pokemon battle system built using object-oriented programming principles.

The system models Pokemon, trainers, and battles, with support for different Pokemon types, evolution logic, attacks, damage handling, and trainer-based battle flow.

## Features

- Abstract base `Pokemon` class
- Type-based classes:
  - `Fire`
  - `Water`
  - `Electric`
- Specific Pokemon implementations:
  - `Charmander`
  - `Charmeleon`
  - `Charizard`
  - `Squirtle`
  - `Wartortle`
  - `Blastoise`
  - `Pikachu`
- `Trainer` class for managing a trainer's Pokemon
- `Battle` class for running Pokemon battles between trainers
- Support for:
  - attacks
  - absorbing damage
  - checking whether a Pokemon can still fight
  - leveling up
  - evolution
  - type effectiveness

## Project Structure

- `Pokemon.py` – abstract base class for all Pokemon
- `Fire.py`, `Water.py`, `Electric.py` – type-specific behavior
- `Charmander.py`, `Charmeleon.py`, `Charizard.py` – fire Pokemon evolution line
- `Squirtle.py`, `Wartortle.py`, `Blastoise.py` – water Pokemon evolution line
- `Pikachu.py` – electric Pokemon implementation
- `Trainer.py` – trainer management logic
- `Battle.py` – battle flow and battle logic
- `main.py` – example execution of the project

## Concepts Used

This project demonstrates several core object-oriented programming concepts:

- Inheritance
- Abstraction
- Polymorphism
- Encapsulation
- Class interaction and composition

## How to Run

Run the main file:

```bash
python main.py
