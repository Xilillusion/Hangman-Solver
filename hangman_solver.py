from collections import defaultdict
from math import log2

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return list(file.read().splitlines())

def init_search_space(word_list, length):
    def binary_search(length, find_first=True):
        low, high = 0, len(word_list) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2
            l = len(word_list[mid])

            if l < length:
                low = mid + 1
            elif l > length:
                high = mid - 1
            else:  # l == length
                result = mid
                if find_first:
                    high = mid - 1
                else:
                    low = mid + 1

        return result
    start = binary_search(length, True)
    end = binary_search(length, False)

    if start == -1 or end == -1:
        return set()  # No words of the target length found
    
    return set(word_list[start:end + 1])

class Solver:
    def __init__(self, search_space, search_chars="abcdefghijklmnopqrstuvwxyz"):
        self.search_chars = set(search_chars)
        self.reset(search_space)
        
    def reset(self, search_space):
        self.search_space = search_space
        self.length = len(next(iter(search_space), ""))
        self.pattern = [None] * self.length
        self.available_chars = self.search_chars.copy()

    def respond_pattern(self, char, new_pattern):
        self.available_chars.discard(char)
        new_search_space = set()

        # Incorrect guess
        if self.pattern == new_pattern:
            for w in self.search_space:
                if char not in w:
                    new_search_space.add(w)
        # Correct guess
        else:
            pos = []
            for i in range(self.length):
                if self.pattern[i] != new_pattern[i]:
                    self.pattern[i] = char
                    pos.append(i)
            # Filter words matching the new pattern
            for w in self.search_space:
                match = True
                for i in pos:
                    if w[i] != char:
                        match = False
                        break
                if match:
                    new_search_space.add(w)

        self.search_space = new_search_space

    def solve_dumb(self, order="earotilsnucyhdpgmbfkxwvzqj '-"):
        # Choose character in dictionary frequency order
        for c in order:
            if c in self.available_chars:
                return c
        return self.available_chars[0]

    def solve_freq(self):
        # Choose character that commonly appears in most words
        freq_count = defaultdict(int)
        for w in self.search_space:
            for c in w:
                if c in self.available_chars:
                    freq_count[c] += 1
        return max(freq_count, key=freq_count.get)

    def solve_uniq(self):
        # Choose character that uniquely appears in most words
        unique_count = defaultdict(int)
        for w in self.search_space:
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

        total_words = len(self.search_space)

        for char in self.available_chars:
            pattern_count = defaultdict(int)
            occurrence_count = 0

            for word in self.search_space:
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


def plot_stats(stats, file_name):
    # Visualize the statistics
    import matplotlib.pyplot as plt
    from collections import Counter

    for method, guesses in stats.items():
        freq = Counter(guesses)
        x = sorted(freq.keys())
        y = [freq[i] for i in x]
        plt.plot(x, y, marker='o', label=method, alpha=0.7)
    plt.xlabel("Number of Incorrect Guesses")
    plt.ylabel("Frequency")
    plt.title(f"Hangman Solver Performance on {file_name}")
    plt.legend()
    plt.show()


def main(file_path: str, methods: list[str]):
    import tqdm

    word_list = load_dictionary(file_path)
    if 'oxford' in file_path:
        # Oxford words may contain apostrophes and hyphens
        solver = Solver(word_list, search_chars="abcdefghijklmnopqrstuvwxyz '-")
    else:
        solver = Solver(word_list)

    stats = {}
    for method in methods:
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
        curr_word_len = 0
        search_space = set()

        progress_bar = tqdm.tqdm(word_list, desc=f"Testing {method} method")
        for w in progress_bar:
            game = HangmanGame(w)

            # Initialize search space for the word length
            if len(w) != curr_word_len:
                curr_word_len = len(w)
                search_space = init_search_space(word_list, curr_word_len)
            solver.reset(search_space)

            # Game simulation
            incorrect = 0
            while not game.is_solved():
                guess = solver_method()
                correct, pattern = game.respond(guess)
                if not correct:
                    incorrect += 1

                solver.respond_pattern(guess, pattern)

            # Record statistics
            total += incorrect
            stats[method].append(incorrect)
            progress_bar.set_postfix(avg=f"{total / (progress_bar.n + 1):.2f}")
    
    return stats

if __name__ == "__main__":
    file_name = 'oxford5000.txt'
    #file_name = 'oxford3000.txt'
    #file_name = 'wordle.txt'
    methods = ['dumb', 'frequency', 'unique', 'bayesian']

    stats = main(f"dictionary/{file_name}", methods)
    plot_stats(stats, file_name)