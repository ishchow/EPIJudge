from test_framework import generic_test


def find_nearest_repetition(paragraph):
    if not paragraph or len(paragraph) <= 1:
        return -1
    minDist = float('inf')
    wordToLastIndex = {}
    for i in range(0, len(paragraph)):
        word = paragraph[i]
        if word not in wordToLastIndex:
            wordToLastIndex[word] = i
        else:
            lastIdx = wordToLastIndex[word]
            minDist = min(minDist, i - lastIdx)
            wordToLastIndex[word] = i
    return minDist if minDist < float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
