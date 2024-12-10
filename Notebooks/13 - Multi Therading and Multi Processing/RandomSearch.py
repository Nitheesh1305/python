# Load the dataset
X, Y = load_dataset()

# Create model for KerasClassifier
def create_model(hparams1=dvalue,
                 hparams2=dvalue,
                 ...
                 hparamsn=dvalue):
    # Model definition
    ...

model = KerasClassifier(build_fn=create_model) 

# Specify parameters and distributions to sample from
hparams1 = randint(1, 100)
hparams2 = ['elu', 'relu', ...]
...
hparamsn = uniform(0, 1)

# Prepare the Dict for the Search
param_dist = dict(hparams1=hparams1, 
                  hparams2=hparams2, 
                  ...
                  hparamsn=hparamsn)

# Search in action!
n_iter_search = 16 # Number of parameter settings that are sampled.
random_search = RandomizedSearchCV(estimator=model, 
                                   param_distributions=param_dist,
                                   n_iter=n_iter_search,
                                   n_jobs=, 
								   cv=, 
								   verbose=)
random_search.fit(X, Y)

# Show the results
print("Best: %f using %s" % (random_search.best_score_, random_search.best_params_))
means = random_search.cv_results_['mean_test_score']
stds = random_search.cv_results_['std_test_score']
params = random_search.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))