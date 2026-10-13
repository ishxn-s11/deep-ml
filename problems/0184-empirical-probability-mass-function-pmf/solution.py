from collections import Counter

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    pass

    if not samples:

        return []
    
    cnt=Counter(samples)
    n=len(samples)

    return [(i,cnt/n) for i,cnt in sorted(cnt.items())]