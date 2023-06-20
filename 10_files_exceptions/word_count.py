from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry, the file {path} does not exist.")
        pass
    else:
        #Count the approximate number of words in the file
        words = contents.split()
        num_word = len(words)
        print(f"The file {path} has about {num_word} words.")

filenames = ['little_women.txt', 'moby_dick.txt', 'alice.txt']
for file in filenames:
    path = Path(file)
    count_words(path)


