class Solution:
    def maxProfit(self, spot: List[int]) -> int:

        spot_len = len(spot)
        index_list = list(range(spot_len))
        spot_index = list(zip(spot, index_list))

        sell_spot = spot_index[-1]
        buy_spot = spot_index[0]

        for i in range(len(spot_index)):
            if spot_index[-i - 1][0] > sell_spot[0] and spot_index[-i - 1][1] > buy_spot[1]:
                sell_spot = spot_index[-i - 1]
            if spot_index[i][0] < buy_spot[0] and spot_index[i][1] < sell_spot[1]:
                buy_spot = spot_index[i]

        return sell_spot[0] - buy_spot[0]