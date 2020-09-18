# Computer Architecture

## Project

* [Implement the LS-8 Emulator](ls8/)

## Task List: add this to the first comment of your Pull Request

### Day 1: Get `print8.ls8` running

- [X] Inventory what is here
- [X] Implement the `CPU` constructor _ Step 1 in ls8/README.MD
- [X] Add RAM functions `ram_read()` and `ram_write()` _ Step 2 in ls8/README.MD
- [X] Implement the core of `run()` _ Step 3 in ls8/README.MD
- [X] Implement the `HLT` instruction handler _ Step 4 in ls8/README.MD
- [X] Add the `LDI` instruction _ Step 5 in ls8/README.MD
- [X] Add the `PRN` instruction _ Step 6 in ls8/README.MD

### Day 2: Add the ability to load files dynamically, get `mult.ls8` running

- [X] Un-hardcode the machine code instruction _ Step 7 in ls8/README.MD
- [X] Implement the `load()` function to load an `.ls8` file given the filename
      passed in as an argument instruction _ Also Step 7 in ls8/README.MD
- [X] Implement a Multiply instruction (run `mult.ls8`) instruction _ Step 8 in ls8/README.MD

- [X] Beautify the run loop instruction _ Step 9 in ls8/README.MD

### Day 3: Stack

- [X] Implement the System Stack and be able to run the `stack.ls8` program instruction _ Step 10 in ls8/README.MD

### Day 4: Get `call.ls8` running

- [X] Implement the CALL and RET instructions
- [X] Implement Subroutine Calls and be able to run the `call.ls8` program

### Stretch

- [ ] Add the timer interrupt to the LS-8 emulator
- [ ] Add the keyboard interrupt to the LS-8 emulator
- [ ] Write an LS-8 assembly program to draw a curved histogram on the screen
