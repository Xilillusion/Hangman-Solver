# Hangman Solver #

A Hangman (a word-guesssing game) solver using heuritic (letter frequency) and bayesain appoarches

## Methods ##
`Solver` class
- Dumb `solve_dumb`: return letters based on a fixed order
- Freqeuncy `solve_freq`: return letters based on the frequency in the dictionary
- Unique `solve_uniq`: return letters based on the frequency in the dictionary, count only once in each word
- Bayesian `solve_baye`: return letters based on the best entropy and occurrence

## Performance ##
### Wordle word list
| Method      | Average Fails | Time Consumption         |
| ----------- | ---------------------------- | -------------- |
| Dumb    | ~12.58                         | 2400 it/s              |
| Frequncy   | ~3.90                       | 650 it/s         |
| Unique | ~3.88                       | 650 it/s         |
| Bayesian  | ~3.82                       | 30 it/s         |

* Average Fails: The times that it guesses an incorrect letter
* Reference only. Average fails may varies due to the usage of set; time consumption varies on the devices

### Oxford 3000 ###
| Method      | Average Fails | Time Consumption        |
| ----------- | ---------------------------- | -------------- |
| Dumb    | ~11.39                         | 5700 it/s              |
| Frequncy   | ~2.17                       | 2700 it/s         |
| Unique | ~2.33                       | 1600 it/s         |
| Bayesian  | ~2.22                       | 150 it/s         |

### Oxford 5000
| Method      | Average Fails | Time Consumption        |
| ----------- | ---------------------------- | -------------- |
| Dumb    | ~12.58                         | 5500 it/s              |
| Frequncy   | ~2.17                       | 1900 it/s         |
| Unique | ~2.08                       | 1200 it/s         |
| Bayesian  | ~2.08                       | 100 it/s         |

## Output ##
### Wordle ###
<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/960a362e-203e-4dbf-a48e-85e2960578b5" />

### Oxford3000 ###
<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/17d9bccf-4b49-4f22-8e0b-eea71f5e69f7" />

### Oxford5000 ###
<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/800e133b-edd3-40f9-9312-bd2043086114" />
