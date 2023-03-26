from __future__ import annotations
import os
import sys



class XPath:
    """
    @class     「出品した商品」の XPath定義クラス
    """
    @classmethod
    def staticXpath(cls) ->  XPath:
        """
         @brief     static関数
         @return    Xpath
        """
        return cls()
    
    
    
    # もっと見る
    BTN_SEE_MORE: str = '//*[@id="currentListing"]/div/mer-button/button';