# Hangman Solver #

A word-guesssing (Hangman) solver using heuritic (letter frequency) and bayesain appoarches

Similar to https://github.com/Xilillusion/Wordle-Solvers_Bayesian-Minimax-Heuristic.git 

## Methods ##
Solver class
- Dumb `solve_dumb`: return letters based on a fixed order
- Freqeuncy `solve_freq`: return letters based on the frequency in the dictionary
- Unique `solve_uniq`: return letters based on the frequency in the dictionary, count only once in each word
- Bayesian `solve_baye`: return letters based on the best entropy and occurrence

## Performance ##
Oxford 5000
| Method      | Average Fails | Time Consumption (Reference only)        |
| ----------- | ---------------------------- | -------------- |
| `Dumb`    | ~12.58                         | 5500 it/s              |
| `Frequncy`   | ~2.17                       | 1900 it/s         |
| `Unique` | ~2.08                       | 1200 it/s         |
| `Bayesian`  | ~2.08                       | 100 it/s         |

Wordle word list
| Method      | Average Fails | Time Consumption (Reference only)        |
| ----------- | ---------------------------- | -------------- |
| `Dumb`    | ~12.58                         | 2400 it/s              |
| `Frequncy`   | ~3.90                       | 650 it/s         |
| `Unique` | ~3.88                       | 650 it/s         |
| `Bayesian`  | ~3.82                       | 30 it/s         |

## Output ##

### Wordle ###
<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/960a362e-203e-4dbf-a48e-85e2960578b5" />

