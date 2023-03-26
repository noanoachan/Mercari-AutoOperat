from __future__ import annotations
import os
import sys



class CssSelector:
    """
     @class     「出品した商品」の CSSSelector定義クラス
    """
    @classmethod
    def staticCssSelector(cls) ->  CssSelector:
        """
         @brief     static関数
         @return    CssSelector
        """
        return cls()
    

    # 商品リスト
    LST_PRODUCT: str = '#currentListing > div > mer-list-item';