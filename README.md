# Hangman Solver #

A word-guesssing (Hangman) solver using heuritic (letter frequency) and bayesain appoarches

Similar to https://github.com/Xilillusion/Wordle-Solvers_Bayesian-Minimax-Heuristic.git 

### Solver Methods ###
- solve_dumb: return letters based on a fixed order (the overall frequency of alphabets)
- solve_freq: return letters that commonly appears in most words
- solve_uniq: return letters that uniquely appears in each word
- solve_baye: return letters based on the best entropy and occurrence
