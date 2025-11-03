# Hangman Solver #

A word-guesssing (Hangman) solver using heuritic (letter frequency) and bayesain appoarches

Similar to https://github.com/Xilillusion/Wordle-Solvers_Bayesian-Minimax-Heuristic.git 

### Solver Methods ###
- solve_dumb: return letters based on a fixed order
- solve_freq: return letters based on the frequency in the dictionary
- solve_uniq: return letters based on the frequency in the dictionary, count only once in each word
- solve_baye: return letters based on the best entropy and occurrence

### Output ###

words_wordle.txt

<img width="571" height="455" alt="image" src="https://github.com/user-attachments/assets/6c0649b6-513a-4f32-a4c1-e4e49984b5d5" />

words_oxford5000.txt from https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000 

<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/70e75fdc-725c-46b3-8f15-c215dec33fe7" />
