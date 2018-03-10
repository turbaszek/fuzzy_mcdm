import numpy as np

class FPS():
    # This is Fuzzy Preference Structure represented as (s, phi)-FPS where automorphism phi is the identity function.
    # s = {0,1, 'inf'}
    #
    def __init__(self, array, s=0):

        if s != 0 or s != 1 or s != 'inf':
            self.s = 0
            #print("S must be {0, 1, inf}. Set default value s=0")
        else:
            self.s = s

        self.Rarray = array
        R = self.Rarray

        # initiate strict preference P array
        if self.s == 0:
            # max{R(a,b) - R(b,a), 0}
            self.Parray = np.maximum(R - R.T, 0)
        elif self.s == 1:
            # R(a,b)(1- R(b,a))
            self.Parray = R * (1 - R.T)
        elif self.s == "inf":
            # min{R(a,b), 1-R(b,a)}
            self.Parray = np.minimum(R, 1 - R.T)


        # initiate indifference relation I array
        if self.s == 0:
            # min{R(a,b), R(b,a)}
            self.Iarray = np.minimum(R, R.T)
        elif self.s == 1:
            # R(a,b)R(b,a)
            self.Iarray = R * R.T
        elif self.s == "inf":
            # max{R(a, b)+R(b, a)-1,0}
            self.Iarray = np.maximum(R + R.T - 1, 0)

        # initiate incomparability relation J array
        if self.s == 0:
            # min{(1-R(a,b), 1-R(b,a)}
            self.Jarray = np.minimum(1-R, 1-R.T)
        elif self.s == 1:
            # (1-R(a,b))(1-R(b,a))
            self.Jarray = (1-R) * (1-R.T)
        elif self.s == "inf":
            # max{1 - R(a,b) - R(b, a),0}
            self.Jarray = np.maximum(1 - R - R.T, 0)

def mcdm(alternatives, criteria_rarays, method=1, s=0):

    problem_size = len(alternatives)
    fps_list = []
    for r in criteria_rarays:
        fps_list.append(FPS(r,s))

    if method == 1:
        # aggregation
        minR = np.ones((problem_size,problem_size))
        for r in [fps.Rarray for fps in fps_list]:
            minR = np.minimum(minR, r)

        discrete_fps = FPS(minR, s)

        # scoring
        ND = 1 - np.nanmax(discrete_fps.Parray, axis=0)
        NDmax = np.max(ND)

        # optimal decision set
        nd_alternatives = []
        for i in range(ND.size):
            if ND[i] == NDmax:
                nd_alternatives.append(alternatives[i])

        # result type
        rtype = 'fuzzy'
        if NDmax == 1:
            rtype = 'crisp'

        return {'optimal_set': nd_alternatives, 'nd_set': ND, 'set_type': rtype}

    elif method == 2:
        # scoring
        ND_list = []
        for Pk in [fps.Parray for fps in fps_list]:
            NDk = 1 - np.nanmax(Pk, axis=0)
            ND_list.append(NDk)

        # aggregation
        ND_array = np.array(ND_list)
        nd_alternatives = np.nanmin(ND_array, axis=0)

        optimal_decision = []
        NDmax = np.max(nd_alternatives)
        for i in range(nd_alternatives.size):
            if nd_alternatives[i] == NDmax:
                optimal_decision.append(alternatives[i])

        # result type
        rtype = 'fuzzy'
        if NDmax == 1:
            rtype='crisp'

        return {'optimal_set': optimal_decision, 'nd_set': nd_alternatives, 'set_type': rtype}





