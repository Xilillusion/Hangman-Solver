from collections import defaultdict
import tqdm
from math import log2

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return list(file.read().splitlines())

class Solver:
    def __init__(self,  word_list):
        self.length = len(word_list[0])
        self.pattern = [None] * self.length
        self.word_list = word_list
        self.available_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def reset(self, word_list):
        self.pattern = [None] * self.length
        self.word_list = list(word_list)
        self.available_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    def respond_pattern(self, char, new_pattern):
        self.available_chars.discard(char)
        new_word_list = []

        # Incorrect guess
        if self.pattern == new_pattern:
            for w in self.word_list:
                if char not in w:
                    new_word_list.append(w)
        # Correct guess
        else:
            pos = []
            for i in range(self.length):
                if self.pattern[i] != new_pattern[i]:
                    self.pattern[i] = char
                    pos.append(i)
            # Filter words matching the new pattern
            for w in self.word_list:
                match = True
                for i in pos:
                    if w[i] != char:
                        match = False
                        break
                if match:
                    new_word_list.append(w)

        self.word_list = new_word_list
    
    def solve_dumb(self, order="EAROTILSNUCYHDPGMBFKWVXZQJ"):
        # Choose character in a given order
        for c in order:
            if c in self.available_chars:
                return c
        return None

    def solve_freq(self):
        # Choose character that commonly appears in most words
        freq_count = defaultdict(int)
        for w in self.word_list:
            for c in w:
                if c in self.available_chars:
                    freq_count[c] += 1
        return max(freq_count, key=freq_count.get)

    def solve_uniq(self):
        # Choose character that uniquely appears in most words
        unique_count = defaultdict(int)
        for w in self.word_list:
            seen = set()
            for i, c in enumerate(w):
                if self.pattern[i] is None and c not in seen and c in self.available_chars:
                    unique_count[c] += 1
                    seen.add(c)

        return max(unique_count, key=unique_count.get)
    
    def solve_baye(self):
        best_char = None
        best_entropy = -1.0
        best_occurrence = -1

        total_words = len(self.word_list)

        for char in sorted(self.available_chars):
            pattern_count = defaultdict(int)
            occurrence_count = 0

            for word in self.word_list:
                pattern = list(self.pattern)
                found = False

                for i in range(self.length):
                    if self.pattern[i] is None and word[i] == char:
                        pattern[i] = char
                        found = True

                if found:
                    occurrence_count += 1

                pattern_count[tuple(pattern)] += 1

            entropy = 0.0
            for count in pattern_count.values():
                p = count / total_words
                entropy -= p * log2(p)

            if (
                entropy > best_entropy
                or (entropy == best_entropy and occurrence_count > best_occurrence)
            ):
                best_char = char
                best_entropy = entropy
                best_occurrence = occurrence_count

        return best_char

class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.pattern = [None] * len(word)

    def respond(self, guess):
        correct = False
        for i, c in enumerate(self.word):
            if c == guess:
                self.pattern[i] = c
                correct = True
        return correct, self.pattern
    
    def is_solved(self):
        return all(c is not None for c in self.pattern)

def train_dumb(word_list):
    # Train a dumb solver by letter frequency in dataset
    freq_count = defaultdict(int)
    unique_count = defaultdict(int)
    for w in word_list:
        seen = set()
        for c in w:
            freq_count[c] += 1
            if c not in seen:
                unique_count[c] += 1
                seen.add(c)
    print("Most common letters:", ''.join(sorted(freq_count, key=freq_count.get, reverse=True)))
    print("Most unique letters:", ''.join(sorted(unique_count, key=unique_count.get, reverse=True)))

if __name__ == "__main__":
    word_length = 5

    word_list = load_dictionary(f'words{word_length}.txt')
    stats = {}

    for method in ['dumb', 'frequency', 'unique', 'bayesian']:
        # Reset solver for each method
        solver = Solver(word_list)
        stats[method] = []

        if method == 'dumb':
            solver_method = solver.solve_dumb
        elif method == 'frequency':
            solver_method = solver.solve_freq
        elif method == 'unique':
            solver_method = solver.solve_uniq
        elif method == 'bayesian':
            solver_method = solver.solve_baye
        else:
            continue

        total = 0
        progress_bar = tqdm.tqdm(word_list, desc=f"Testing {method} method")
        
        for w in progress_bar:
            game = HangmanGame(w)
            solver.reset(word_list)

            incorrect = 0
            while not game.is_solved():
                guess = solver_method()
                correct, pattern = game.respond(guess)
                if not correct:
                    incorrect += 1

                solver.respond_pattern(guess, pattern)

            total += incorrect
            stats[method].append(incorrect)
            progress_bar.set_postfix(avg=f"{total / (progress_bar.n + 1):.2f}")
    
    
    import matplotlib.pyplot as plt
    from collections import Counter

    for method, guesses in stats.items():
        freq = Counter(guesses)
        x = sorted(freq.keys())
        y = [freq[i] for i in x]
        plt.plot(x, y, marker='o', label=method, alpha=0.7)
    plt.xlabel("Number of Incorrect Guesses")
    plt.ylabel("Frequency")
    plt.title("Hangman Solver Performance")
    plt.legend()
    plt.show()
