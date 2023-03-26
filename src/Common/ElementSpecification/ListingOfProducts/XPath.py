from __future__ import annotations
import os
import sys



class XPath:
    """
    @class     「出品画面」の XPath定義クラス
    """
    @classmethod
    def staticXpath(cls) ->  XPath:
        """
         @brief     static関数
         @return    Xpath
        """
        return cls()
    
    
    
    #! 出品画像（最大10枚）
    #INPUR_PICTURE: str = '//*[@id="main"]/form/section[1]/div/div[3]/input';
    INPUR_PICTURE: str = '//*[@id="main"]/form/section[1]/div/div[5]/input'