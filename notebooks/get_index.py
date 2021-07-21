def get_neuron_idx(AI_data):
    '''returns a list of tuples. Each element in the list corresponds to one run in the 
    AI_data input. First element in each tuple are the indices for left prefering neurons,
    second element are the indices for right prefering neurons'''
    
    idx_lst = []
    
    for i, dat in enumerate(AI_data):
        spks = dat['spks']
        response = dat['response']
        
        spks[spks == 0] = np.nan
        
        spks_avg = np.nanmean(spks, axis=2)
        
        reg = LogisticRegression(penalty="l1", solver='liblinear',  C = 1).fit(spks_avg.T, response)
        
        w = reg.coef_.squeeze()
        
        right_neurons = np.where(w > 0)
        left_neurons = np.where(w < 0)
        
        my_touple = (left_neurons[0], right_neurons[0])
        
        
        idx_lst.append(my_touple)
    
    return idx_lst
