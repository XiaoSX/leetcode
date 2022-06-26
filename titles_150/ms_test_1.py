#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/17
'''
#


def dense():
    pass


def softmax():
    pass


def forward(x, model):
    """
    model: str
            假设有效玩罗
            参数的格式指定为key:value
            当前层调用 "layer_name#aram1:value1#param2:value2\nlayer_name2#param2:value2 "
            网络结构形式: "S_layer_ith#layer_jth#Operation"
    :param x:
    :param model:
    :return:
    """

    layers = model.split('\n')
    ans = []
    for layer in layers:
        if layer.startswith('S_'):
            i, j, op = layers[2:].split('#')
            i = int(i)
            j = int(j)
            ans.append(eval(op)(ans[i], ans[j]))
        else:
            layer = layer.split('#')
            layer_name, params = layer[0], layer[1:]
            _p = {}
            for item in params:
                k, v = item.split(':')
                _p[k] = int(v)
            f = eval(layer_name)(**_p)
            ans.append(f(ans[-1]))
    return ans[-1]

import json
model = {"layer1": {"name": "Input"},
         "layer2": {"name": "Dense", "param": {"unit": 10}},
         "layer3": {"name": "Softmax"},
         "struct": [("layer1", []), ("layer2", ["layer1"]), ("layer3", ["layer1", "layer2"])]}
model = json.dumps(model)

def forward_v2(x, model):
    model = json.loads(model)
    output = {}
    for i in range(len(model['struct'])):
        layer = model['struct'][i]
        layer_name, layer_input = layer
        layer_class = model['layer_name']['name']
        param = {}
        if 'param' in model['layer_name']:
            param = model['layer_name']['param']
        f = eval(layer_class)(**param)
        if i == 0:
            layer_input.append(x)
        else:
            layer_input = [output[name] for name in layer_input]

        output[layer_name] = f(*layer_input)

    return output[model['struct'][-1][0]]