# 深度合并dict
"""
注意
1. 考虑嵌套的情况，检查各种异常、冲突、特殊值，并抛出合适异常
2. 当值为 list 时，直接使用新值替换旧值，不必连接两个 list
"""


def merge_dict(x: dict, y: dict):
    """

    :param x: 来源参数被替换的字典
    :param y: 替换数据
    :return:
    """
    for key, value in x.items():
        # 循环找出字典中需要被替换的key值
        if key in y.keys():
            if type(x[key]) != type(y[key]):
                # 无法匹配数据类型不一致的参数
                raise TypeError
            else:
                if isinstance(x[key], dict):
                    # 当hash结构出现时，递归处理
                    x[key] = merge_dict(x[key], y[key])
                else:
                    x[key] = y[key]

    return x


source_dict = {'key0': 'a', 'key1': 'b', 'key2': {'inner_key0': 'c', 'inner_key1': 'd'}}
update_dict = {'key1': 'x', 'key2': {'inner_key0': {}}}
result = merge_dict(source_dict, update_dict)
print(result)
