import requests
import lxml.html
import random
import sys
import string

SITE = 'http://www.thesaurus.com/browse/'
EXCEPTION_WORDS = ['i', 'me', 'a', 'an', 'the', 'and', 'is', 'or', 'but', 'if', 'then', 'else', 'when', 'at', 'from', 'by', 'on', 'off', 'for', 'in', 'out', 'over', 'to', 'into', 'with', 'you']
PROBABILITY_OF_SYNONYMISATION = 0.2


def get_synonyms(word, site=None):
    if site is None:
        site = requests.get(SITE + word).text
    tree = lxml.html.fromstring(site)
    words = []
    i = 1
    while True:
        try:
            words.append(tree.xpath(f'/html/body/div[1]/div[2]/div/div/div[2]/main/section/section/div[2]/div[2]/ul/li[{i}]/a/text()')[0])
            i += 1
        except IndexError:
            if not words:
                words = [word]
            break
    return words


def synonymise_sentance(words):
    if hasattr(words, 'split'):
        words = words.split(' ')
    for i, word in enumerate(words):
        if word[0] == '_' or word.lower() in EXCEPTION_WORDS:
            words[i] = word.replace('_', '')
            continue
        if random.random() > PROBABILITY_OF_SYNONYMISATION:
            continue
        # remove punctuation from word and add it to the end of the word after processing
        punctuation = ''
        for char in word:
            if char != "'" and char in string.punctuation:
                punctuation += char
        word = word.strip(string.punctuation)
        synonyms = get_synonyms(word)
        words[i] = random.choice(synonyms)+punctuation
    return ' '.join(words).capitalize()


if __name__ == '__main__':
    # sys.argv.extend("You'll have to _tell me how annoying this is".split())
    if len(sys.argv) < 2:
        print('Usage: python Thesaurusise.py [words ...]')
        sys.exit(-1)
    words = sys.argv[1:]
    print(synonymise_sentance(words))
