class WordsFinder:
    def __init__(self, *files):
        self.file_names = []
        for file in files:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = dict()
        for file_name in self.file_names:
            with (open(file_name, encoding="utf-8") as file):
                string = file.read()
                string = string.lower()

                for symb in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    string = string.replace(symb, '')

                string = string.split()
                all_words.update({file_name: string})

        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            return {name: words.index(word.lower()) + 1}

    def count(self, word):
        for name, words in self.get_all_words().items():
            return {name: words.count(word.lower())}


finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())
print(finder1.find("TEXT"))  # 3 слово по счёту
print(finder1.count('teXT'))  # 4 слова teXT в тексте всего
