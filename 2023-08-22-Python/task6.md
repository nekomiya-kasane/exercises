The data flow of the implementation of this title analysis programs is like this:

1. Normalize data, turn quantitive cell into integers of the same unit
2. Tokenize words in titles
3. Find the word that results in high view counts  

Since I process the data row by row, the total time complexity of this piece of program is O(n).

From the plot image of task 3, we can notice that basically, the longer time a article is posted, the higher view count there will be, but for articles too old, the view counts are rather lower. There're some particular articles that are posted near now, but received high view counts. These articles may be welcomed by the readers.

From the plot image of task 5, we can observe that the words "liberal," "Jesse," "bombshell," "Kamala," and "Watters" appear most frequently in popular articles. Upon revisiting the original CSV file, we discover that Jesse Watters is a journalist who writes articles about politics, "bombshell" is an attention-grabbing adjective, and Kamala is the first name of Kamala Harris, one of the Vice Presidents of the United States. Therefore, we can conclude that people are most interested in political topics and are drawn to titles that incorporate impactful adjectives.

The text pre-processing steps are improper sometimes, with the following reasons:

- All non-alphabetic characters are removes, then some words like 'Smith's property' will become 'Smiths property' in which 'Smiths' is not the original word. Another example: 'attention-grabbing' will become 'attentiongrabbing', which is not a valid word.
- Some words that are not important will have the same weights with normal word, this may lead to bad word pool. Such word includes 'of', 'in', 'and' etc.

