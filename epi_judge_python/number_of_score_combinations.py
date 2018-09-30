from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    cache = {}
    def combinationsFrom(score):
        nonlocal cache
        nonlocal individual_play_scores
        if score < 0:
            return 0
        elif score == 0:
            return 1

        if score not in cache:
            cache[score] = sum([combinationsFrom(score - ps) for ps in individual_play_scores])
        return cache[score]
    return combinationsFrom(final_score)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
