if __name__ == '__main__':
    import numpy as np
    from fps import mcdm

    # R1 = np.array([[1, 0.6, 0.7],
    #             [0.8, 1, 0.6],
    #             [0.3, 0.8, 1]])
    # R2 = np.array([[1, 0.2, 0.7],
    #               [0.1, 1, 0.6],
    #               [0.3, 0.7, 1]])
    # R3 = np.array([[1, 0.2, 0.7],
    #               [0.5, 1, 0.4],
    #               [0.3, 0.8, 1]])
    # R4 = np.array([[1, 0.6, 0.7],
    #               [0.3, 1, 0.3],
    #               [0.1, 0.8, 1]])

    # Example 2 H.Borzęcka [2012]
    R1 = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [0.88, 0.88, 1]])
    R2 = np.array([[1, 0.88, 0.24],
                   [1, 1, 0.88],
                   [1, 1, 1]])
    R3 = np.array([[1, 1, 1],
                   [0.88, 1, 1],
                   [0.88, 1, 1]])

    # Fuzzy vector of large preferences corresponding to criteria 1,2,3
    r =[R1,R2,R3]

    # Crisp set of alternatives
    a = ['a', 'b', 'c']

    decision1 = mcdm(a,r, 1, 0)
    decision2 = mcdm(a, r, 2, 0)

    print('Set of optimal decision for method {} (aggregation -> scoring): {}, type of result: {}.'.format(
        1, decision1['optimal_set'], decision1['set_type']))
    print('Set of optimal decision for method {} (scoring -> aggregation): {}, type of result: {}.'.format(
        2, decision2['optimal_set'], decision2['set_type']))
