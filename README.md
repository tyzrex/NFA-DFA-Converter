
# NFA to DFA Converter

A python program to convert Non-deterministic Finite Automata (NFA) to Deterministic Finite Automata (DFA) and visualize the NFA and DFA using Graphviz library. 

## Features

* Easy to use interface that takes NFA as input
* Conversion of NFA to DFA
* PDF generation of NFA and DFA for better visualization
* Graphviz library for visualizing the NFA and DFA

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

## Requirements

* Python 3
* Pandas
* Graphviz
* Itertools

## Installing 

1. Clone the directory

   ```
   https://github.com/tyzrex/NFA-DFA-Converter
   ```
2. Go to the desired project directory

   ```bash
   cd NFA-DFA-Converter/
   ```
3. Install the requirements(if any)

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the project:

   ```bash
   python project.py
   ```
2. Follow the on-screen instructions to enter the NFA and visualize the NFA and DFA.

## How it works

The NFA to DFA Converter program works by taking a Non-Deterministic Finite Automata (NFA) as input and converting it into an equivalent Deterministic Finite Automata (DFA). The conversion process involves creating a state transition table for the DFA, which is based on the state transition rules of the NFA.

The program takes the following user inputs:

1. The number of states in the NFA (represented by integers).
2. The alphabet symbols that the NFA accepts as input (represented by characters).
3. The transition rules for the NFA, which define how the NFA moves from one state to another based on the input symbol. The transition rules are represented in the form (current state, input symbol) => next state.
4. The starting state of the NFA.
5. The set of accepting states in the NFA.

Based on the above inputs, the program generates the state transition table for the equivalent DFA and displays it to the user. The state transition table shows the state transition rules for the DFA, which define how the DFA moves from one state to another based on the input symbol.

## Result

The final result of the program is the transition table and states of the equivalent DFA, as well as a PDF that visually represents both the NFA and DFA. The PDF provides a visual representation of the states and transitions for both automata, making it easier for the user to understand the conversion process.

## Built With

* [Python 3](https://www.python.org/downloads/)
* [Graphviz library](https://www.graphviz.org/)
* [graphviz module](https://pypi.org/project/graphviz/)

## Contributing

We welcome contributions from the community. If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://chat.openai.com/chat/LICENSE.md) file for details.
