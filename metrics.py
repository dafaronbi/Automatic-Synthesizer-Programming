import numpy as np
from data import one_hot

def predict_decode(params,synth):

    if synth == "serum":
        params = one_hot.predict(params, one_hot.serum_oh)
        params = one_hot.decoded(params, one_hot.serum_oh)
    
    if synth == "diva":
        params = one_hot.predict(params, one_hot.diva_oh)
        params = one_hot.decoded(params, one_hot.diva_oh)
    
    if synth == "tyrell":
        params = one_hot.predict(params, one_hot.tyrell_oh)
        params = one_hot.decoded(params, one_hot.tyrell_oh)

    
    return params

def class_acuracy(y_true,y_predict):
    oh_code = None

    if len(y_true) == 480:
        oh_code = one_hot.serum_oh

    if len(y_true) == 759:
        oh_code = one_hot.diva_oh

    if len(y_true) == 327:
        oh_code = one_hot.tyrell_oh

    y_true = one_hot.predict(y_true,oh_code)
    y_true = one_hot.decoded(y_true,oh_code)

    y_predict = one_hot.predict(y_predict,oh_code)
    y_predict = one_hot.decoded(y_predict,oh_code)

    total_classes = 0
    correct_classes = 0
    i = 0
    for c in oh_code:
        if c <= 1:
            i += 1

        else:
            total_classes += 1
            #decode one hot
            for n in range(c):
                if y_true[i] == 1:
                    if y_predict[i] == 1:
                        correct_classes += 1
                i += 1

    return con_mse, (correct_classes / total_classes)

def continous_mse(y_true,y_predict):

    oh_code = []

    if len(y_true) == 480:
        oh_code = one_hot.serum_oh

    if len(y_true) == 759:
        oh_code = one_hot.diva_oh

    if len(y_true) == 327:
        oh_code = one_hot.tyrell_oh

    y_true = one_hot.predict(y_true,oh_code)
    y_true = one_hot.decoded(y_true,oh_code)

    y_predict = one_hot.predict(y_predict,oh_code)
    y_predict = one_hot.decoded(y_predict,oh_code)


    con_mse = 0
    i = 0
    for c in oh_code:
        if c <= 1:
            con_mse += (y_true[i] - y_predict[i])**2
            i += 1
        else:
            for n in range(c):
                i += 1

    return con_mse