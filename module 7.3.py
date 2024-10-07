class WordsFinder:
    def __init__(self, *file_names):
        print(file_names)
        self.file_names = file_names
    def get_all_words(self,):

        all_words = {}

        b = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for fl in self.file_names:
            a = ""
            with open(fl, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for i in line:
                        if i in b:
                            line = line.replace(i, '')
                    a += line
            all_words.update({fl: a.split()})
        return all_words
    def find(self, word):
        Slovarik = {}

        ll_word = self.get_all_words()
        for name, words in ll_word.items(): ##### вопросики
                for number, text in enumerate(words, 0): ####### вопросики
                    if text == word.lower():
                        Slovarik[name] = number
                        break
        return Slovarik


    def count(self, word):
        Spisok_ = {}
        pp_word = self.get_all_words()
        for f, fj in pp_word.items():
            count_ = fj.count(word.lower()) # количество повторений
            Spisok_[f] = count_
        return Spisok_













finder2 = WordsFinder('test_file.txt', 'test_file2.txt', 'test_file3.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего