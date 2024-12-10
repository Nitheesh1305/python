# Load the dataset
x, y = load_dataset()

# Create model for KerasClassifier
def create_model(hparams1=dvalue,
                 hparams2=dvalue,
                 ...
                 hparamsn=dvalue):
    # Model definition
    ...

model = KerasClassifier(build_fn=create_model) 

# Define the range
hparams1 = [2, 4, ...]
hparams2 = ['elu', 'relu', ...]
...
hparamsn = [1, 2, 3, 4, ...]

# Prepare the Grid
param_grid = dict(hparams1=hparams1, 
                  hparams2=hparams2, 
                  ...
                  hparamsn=hparamsn)

# GridSearch in action
grid = GridSearchCV(estimator=model, 
                    param_grid=param_grid, 
                    n_jobs=, 
                    cv=,
                    verbose=)
grid_result = grid.fit(x, y)

# Show the results
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))
