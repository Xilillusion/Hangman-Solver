# Hangman Solver #

A word-guesssing (Hangman) solver using heuritic (letter frequency) and bayesain appoarches

Similar to https://github.com/Xilillusion/Wordle-Solvers_Bayesian-Minimax-Heuristic.git 

### Solver Methods ###
- solve_dumb: return letters based on a fixed order (the overall frequency of alphabets)
- solve_freq: return letters that commonly appears in most words
- solve_uniq: return letters that uniquely appears in each word
- solve_baye: return letters based on the best entropy and occurrence

### Result ###

words_wordle.txt
<img width="571" height="455" alt="image" src="https://github.com/user-attachments/assets/6c0649b6-513a-4f32-a4c1-e4e49984b5d5" />

words_oxford5000.txt from https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000 
<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/70e75fdc-725c-46b3-8f15-c215dec33fe7" />

Note that freq and uniq solvers share a similar result, but freq is much faster
