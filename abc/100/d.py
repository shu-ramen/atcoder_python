# -*- coding: utf-8 -*-
# IMPORT ###############################################################################################################
import sys                                                      # システム
sys.setrecursionlimit(10**6)                                    # 再帰処理の上限変更
from collections import deque, Counter                          # キュー・個数カウント
from itertools   import accumulate, permutations, combinations  # 累積和・順列・組み合わせ
from operator    import itemgetter                              # ソート補助
from bisect      import bisect_left, bisect_right, bisect       # 二分探索
from heapq       import heappop, heappush                       # プライオリティキュー
from fractions   import gcd                                     # 最大公約数
from math        import ceil, floor, sqrt, cos, sin, tan, pi    # 数学処理
from copy        import deepcopy                                # オブジェクトコピー
import numpy         as np                                      # 数値計算

# MAIN #################################################################################################################
def main():
    # Init #############################################################################################################
    im = InputManager()
    # Input ############################################################################################################
    n, m = im.inputMultiple()
    xyz = im.input2D(h=n)
    # Logic ############################################################################################################
    scores = []
    for kx in [1, -1]:
        for ky in [1, -1]:
            for kz in [1, -1]:
                tmpScores = []
                for i in range(n):
                    tmpScores.append(kx * xyz[i][0] + ky * xyz[i][1] + kz * xyz[i][2])
                tmpScores.sort(reverse=True)
                scores.append(sum(tmpScores[0:m]))
    # Output ###########################################################################################################
    print(max(scores))
    # Return ###########################################################################################################
    return

# INPUT MANAGER ########################################################################################################
class InputManager(object):
    def __init__(self):
        pass

    @staticmethod
    def inputSingle(dtype=int):
        return dtype(input())
    
    @staticmethod
    def inputMultiple(dtype=int, aslist=False):
        if aslist:
            return list(map(dtype, input().split()))
        else:
            return map(dtype, input().split())

    @staticmethod
    def input2D(h, dtype=int):
        return [list(map(dtype, input().split())) for i in range(h)]

# CALL MAIN ############################################################################################################
main()