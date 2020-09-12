def clustering(students, k, linkage, criterion):
    feature_set = students[['Religijność', 'Stosunek do homoseksualizmu', 'Chodzę spać',
    'Porządek to dla mnie', 'O pokój dba', 'Papierosy',
    'Żyjesz fit czy fat?', 'Kąpiel', 'Imprezy', 'Goście w pokoju', 'Stosunek do obcokrajowców']]

    feature_set = feature_set.fillna(3)
    from sklearn.preprocessing import MinMaxScaler

    x = feature_set.values
    min_max_scaler = MinMaxScaler()
    feature_mtx = min_max_scaler.fit_transform(x)

    import scipy
    leng = feature_mtx.shape[0]
    D = scipy.zeros([leng,leng])
    for i in range(leng):
        for j in range(leng):
            D[i,j] = scipy.spatial.distance.euclidean(feature_mtx[i], feature_mtx[j])


    from scipy.cluster import hierarchy
    Z = hierarchy.linkage(D, linkage)
    from scipy.cluster.hierarchy import fcluster

    clusters = fcluster(Z, k, criterion)

    def llf(id):
            return str(students['Numer wniosku o akademik'][id])

    import matplotlib.pyplot as plt
    fig =plt.figure(k)
    print(students['Numer wniosku o akademik'])
    dendro = hierarchy.dendrogram(Z, leaf_label_func=llf,leaf_rotation=0, leaf_font_size =12, orientation = 'right')
    plt.title(students["Płeć"][0])
    plt.show()