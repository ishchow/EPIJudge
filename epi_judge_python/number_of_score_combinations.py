from test_framework import generic_test

def num_combinations_for_final_score(final_score, individual_play_scores):
    # One way to reach 0.
    num_combinations_for_score = [[1] + [0] * final_score for _ in individual_play_scores]
    for psIdx, currPs in enumerate(individual_play_scores):
        for score in range(1, final_score + 1):
            without_this_play = 0
            if psIdx >= 1:
                without_this_play = num_combinations_for_score[psIdx - 1][score]

            with_this_play = 0
            if score >= currPs:
                with_this_play = num_combinations_for_score[psIdx][score - currPs]
            num_combinations_for_score[psIdx][score] = without_this_play + with_this_play
    return num_combinations_for_score[-1][-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
