from reader import vowel_counter_enhanced
import matplotlib.pyplot as plt

def visualize_vowels(file):
    results=vowel_counter_enhanced(file)
    x=results.keys()
    h=results.values()
    c=['blue','pink']
    plt.bar(x,h,color=c)
    plt.show()

file='data/Richardson_Clarissa.txt'
visualize_vowels(file)