def duration_spread(tests, seconds, pct=.75):
    average_velocity = seconds/tests
    reduced_average_velocity = pct * average_velocity
    acceleration = reduced_average_velocity/tests
    multiplier_list = get_multipliers(tests)
    results = []
    for multiplier in multiplier_list:
        results.append(average_velocity + (multiplier * acceleration))
    return results


def get_multipliers(tests):
    odd = tests % 2
    half_tests = tests // 2
    result = list(range(-half_tests, half_tests+1))
    if not odd:
        result.remove(0)
    return result


print(duration_spread(10, 10), sum(duration_spread(10, 10)))
print(duration_spread(1, 10), sum(duration_spread(1, 10)))
print(duration_spread(5, 10), sum(duration_spread(5, 10)))
print(duration_spread(7, 5), sum(duration_spread(7, 5)))
