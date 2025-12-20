# Hangman Solver #

A Hangman (a word-guesssing game) solver using heuritic (letter frequency) and Bayesain appoarches

## Methods ##
`Solver` class
- Dumb `solve_dumb`: return letters based on a fixed order
- Freqeuncy `solve_freq`: return letters based on the frequency in the dictionary
- Unique `solve_uniq`: return letters based on the frequency in the dictionary, count only once in each word
- Bayesian `solve_baye`: return letters based on the best entropy and occurrence

## Files ##
```plaintext
├── hangman_solver.py  Solver for Hangman
├── library
│   ├── wordle.txt     A word list from Wordle; 2309 5-chars words
│   ├── oxford3000.txt A word list from Oxford 3000; 2979 daily words
│   └── oxford5000.txt A word list from Oxford 5000; 4954 daily words
└── crawler.py         Crawler for oxford3000.txt and oxford5000.txt
```

## Performance ##
### Wordle word list ###
| Method | Average Fails | Death Rate | Time Consumption |
| ------ | ------------- | ---------- | ---------------- |
| Dumb | 12.58 | 99% | 2400 it/s |
| Frequncy | 3.90 | 21% | 650 it/s |
| Unique | 3.88 | 21% | 650 it/s |
| Bayesian | 3.82 | 21% | 30 it/s |

Note
- Average Fails: The average times that it guesses an incorrect letter
- Death Rate: In a traditional Hangman game, 6 fails indicates a death
- Reference only. Numbers may vary due to the usage of unordered set

### Oxford 3000 ###
| Method | Average Fails | Death Rate | Time Consumption |
| ------ | ------------- | ---------- | ---------------- |
| Dumb | 11.39 | 95% | 5700 it/s |
| Frequncy | 2.30 | 8% | 2700 it/s |
| Unique | 2.30 | 8% | 1600 it/s |
| Bayesian | 2.22 | 8% | 150 it/s |

### Oxford 5000
| Method | Average Fails | Death Rate | Time Consumption |
| ------ | ------------- | ---------- | ---------------- |
| Dumb | 11.11 | 90% | 5500 it/s |
| Frequncy | 2.10 | 7% | 1900 it/s |
| Unique | 2.08 | 7% | 1200 it/s |
| Bayesian | 2.07 | 7% | 100 it/s |

## Output ##
Based on different dictionaries
### Wordle ###
<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/960a362e-203e-4dbf-a48e-85e2960578b5" />

### Oxford3000 ###
<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/17d9bccf-4b49-4f22-8e0b-eea71f5e69f7" />

### Oxford5000 ###
<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/800e133b-edd3-40f9-9312-bd2043086114" />

## Libraries ##
- tqdm
- matplotlib
- BeautifulSoup (for `crawler.py`)

## References ##
1. `wordle.txt`: 2308 Wordle words from [Silicon Valley Daily](https://svdaily.com/2022/04/15/all-of-the-words-used-in-ny-times-wordle-game/ )
2. `oxford3000.txt` and `oxford5000.txt` crawled from [Oxford Learner's Dictionaries](https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000 )
