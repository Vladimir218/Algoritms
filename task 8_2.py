# 2.	Закодировать любую строку по алгоритму Хаффмана.

from collections import Counter


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node[{self.value}]'


def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Node(None)
        if len(string_count) == 1:
            node.left = [key for key in string_count]
            node.right = Node(None)
        string_count = {node: 1}
    while len(string_count) != 1:
        node = Node(None)
        simv = string_count.most_common()[:-3:-1]
        if isinstance(simv[0][0], str):
            node.left = Node(simv[0][0])
        else:
            node.left = simv[0][0]
        if isinstance(simv[1][0], str):
            node.right = Node(simv[1][0])
        else:
            node.right = simv[1][0]
        del string_count[simv[0][0]]
        del string_count[simv[1][0]]
        string_count[node] = simv[0][1] + simv[1][1]
    return [key for key in string_count][0]


def code_dic(root, codes=dict(), code=''):
    if root is None:
        return
    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    code_dic(root.left, codes, code + '0')
    code_dic(root.right, codes, code + '1')

    return codes


def coding(s, codes):
    coding_string = ''
    for i in s:
        coding_string += codes[i]
    return coding_string


def decoding(string, codes):
    decod = ''
    i = 0

    while i < len(string):

        for simb in codes:
            rez = string[i:].find(codes[simb])
            if string[i:].find(codes[simb]) == 0:
                decod += simb
                i += len(codes[simb])
    return decod


s = input('Введите строку для кодирования: ')
hafman_tree = get_tree(s)
codes = code_dic(hafman_tree)
print(f'Словарь для кодирования: {codes}')
coding_string = coding(s, codes)
print(f'Закодированная строка - {coding_string}')
decoding_string = decoding(coding_string, codes)
print('Декодированная строка: ', decoding_string)
