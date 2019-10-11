# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").
    user_history = {}

    for site, user in zip(site_list, user_list):
        if user not in user_history:
            user_history[user] = set()
        
        user_history[user].add(site)

    affinities = {}
    
    for user, history in user_history.items():
        history = list(history)
        history.sort()
        for i, site1 in enumerate(history):
            for site2 in history[i+1:]:
                pair = (site1, site2)
                if pair not in affinities:
                    affinities[pair] = 0
                affinities[pair] += 1

    if affinities is None:
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        i = 0
        j = 0
        k = 0
        l = 0
        m = 0
        n = 0
        o = 0
        p = 0
        q = 0
        r = 0
        s = 0
        t = 0
        u = 0
        v = 0
        w = 0
        x = 0
        y = 0
        z = 0

    return max(affinities, key=affinities.get)
