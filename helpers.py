" Some helper functions"


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from empath import Empath
lexicon = Empath()

def plot_categories(data,topics,name_country):
    
    fig,ax = plt.subplots(1)

    # We infer the topics discussed in the retrieved tweets
    classified_topics = pd.DataFrame([lexicon.analyze(data.tweet.str.cat(sep = ' '),categories = topics, 
                                                  normalize = True)], index = [name_country]).T

    classified_topics = classified_topics.sort_values(by = [name_country], ascending = False)
    classified_topics.reset_index(inplace = True)
    sns.barplot(data = classified_topics, x = name_country, y = 'index')
    plt.ylabel('Topics', fontsize = 14)
    plt.title('Topics discussed in {} during the 3 weeks preceding the official lockdown'.format(name_country))
    plt.ylabel('Categories')
    plt.xlabel('Normalized Score')



