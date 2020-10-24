from time import process_time

doc =  " paragraph is a series of related sentences developing a central idea, called the topic. Try to think about paragraphs in terms of thematic unity: a paragraph is a sentence or a group of sentences that supports one central, unified idea. Paragraphs add one idea at a time to your broader argument"
start= process_time()
letters = ''.join(c for c in doc if c.isalpha())
stop= process_time()
print("Elapsed time:", stop, start)
print("Elapsed time during the whole program in seconds:", 
                                         stop-start)  

