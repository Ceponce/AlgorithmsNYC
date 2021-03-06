#!/usr/env/python

def lev(w1, w2):
    """
    Implementation of Levenshtein Distance between two strings.
    """
    word_one_row = [0 for x in xrange(len(w1) + 1)]
    matrix = [list(word_one_row) for x in xrange(len(w2)+ 1)]
    
    for i in xrange(len(w1) + 1):
        matrix[0][i] = i
    for j in xrange(len(w2) + 1):
        matrix[j][0] = j

    for j in xrange(1, len(w2) + 1): 
        for i in xrange(1, len(w1) + 1):
            if w1[i-1] == w2[j-1]:
                matrix[j][i] = matrix[j-1][i-1] 
            else:
                matrix[j][i] = min([matrix[j-1][i] + 1, 
                               matrix[j][i-1] + 1,
                               matrix[j-1][i-1] + 1])
    return matrix[-1][-1] # bottom, right-most value


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        print(lev(sys.argv[1], sys.argv[2]))
    else:
        print("\nlevenshtein.py: calculate the Levenshtein Distance between 2 words\n\nUsage: \n$ python levenshtein.py <word1> <word2>\n")
        
