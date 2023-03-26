from __future__ import annotations
import os
import sys


class Settings:
    """
    @class      Excel
    """
    @classmethod
    def staticSettings(cls) ->  Settings:
        """
         @brief     static関数
         @return    Define
        """
        return cls()



    # 出品商品のファイル名
    FILE_PRODUCT_LIST: str = 'ProductList.xlsx';
    
    
    # 出品商品ファイルのシート名：data
    SHEET_DATA: str = 'data';
    
    
    # 出品商品ファイルのシート名：master
    SHEET_MASTER: str = 'master';
    
    
    # 出品商品ファイルのシート名：setting
    SHEET_SETTING: str = 'setting';
    
    
    # 出品商品ファイルのシート名：template
    SHEET_TEMPLATE: str = 'template';
    
    
    # 出品商品ファイルのシート名：PriceCut
    SHEET_PRICE_CUT: str = 'PriceCut';