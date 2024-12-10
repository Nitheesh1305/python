def data():
    """
    Data providing function:
    This function is separated from model() so that hyperopt
    won't reload data for each evaluation run.
    """
    # Load / Cleaning / Preprocessing
    ...
    return x_train, y_train, x_test, y_test
    
def model(x_train, y_train, x_test, y_test):
    """
    Model providing function:
    Create Keras model with double curly brackets dropped-in as needed.
    Return value has to be a valid python dictionary with two customary keys:
        - loss: Specify a numeric evaluation metric to be minimized
        - status: Just use STATUS_OK and see hyperopt documentation if not feasible
    The last one is optional, though recommended, namely:
        - model: specify the model just created so that we can later use it again.
    """
    # Model definition / hyperparameters space definition / fit / eval
    return {'loss': <metrics_to_minimize>, 'status': STATUS_OK, 'model': model}
    
# SMBO - TPE in action
best_run, best_model = optim.minimize(model=model,
                                      data=data,
                                      algo=tpe.suggest,
                                      max_evals=,
                                      trials=Trials())

# Show the results
x_train, y_train, x_test, y_test = data()
print("Evalutation of best performing model:")
print(best_model.evaluate(x_test, y_test))
print("Best performing model chosen hyper-parameters:")
print(best_run)