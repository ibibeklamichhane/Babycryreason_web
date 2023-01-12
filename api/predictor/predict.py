def predict_gen(meta1):
    import pickle
    import os
    from django.conf import settings
    path = os.path.join(settings.MODELS, 'model.pkl')
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
  # # svmp = data['svmp']
  #     norma = data['norma']
  # # lgn = data['lgn']
  #  x = norma.transform([meta1])
    pred = data.predict(meta1)
    return([pred[0]])
  
  