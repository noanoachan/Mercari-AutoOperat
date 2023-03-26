from __future__ import annotations
import os
import sys



class PositionPriceCut:
    """
    @class      値下げ商品のセル位置
    @detail     セル情報をリストとして取得し取り出し時に使用するため以下の値
    @note       ファイル名      ProductList.xlsx    (シート名：PriceCut)
    """
    @classmethod
    def staticPositionPriceCut(cls) ->  PositionPriceCut:
        """
         @brief     static関数
         @return    CellPositionPriceCut
        """
        return cls()
    
    
    PRODUCT_NAME    : int   = 0;        # 商品名
    PRODUCT_ID      : int   = 1;        # 商品ID
    CHEAPES_PRICE   : int   = 2;        # 最安値
    REMARKS         : int   = 3;        # 備考