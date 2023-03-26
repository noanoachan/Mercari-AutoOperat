from __future__ import annotations
import os
import sys



class CssSelector:
    """
     @class     「出品画面」の CSSSelector定義クラス
    """
    @classmethod
    def staticCssSelector(cls) ->  CssSelector:
        """
         @brief     static関数
         @return    CssSelector
        """
        return cls()
    
    

    # ボタン：出品する
    # (fix_1 : 2022/11/02) BTN_EXHIBITING = '#main > section:nth-child(2) > div > a.OldSellerHomeContent__ListItemButton-sc-2xo3fq-0.bbGatD.mer-spacing-r-16'
    BTN_EXHIBITING: str = '#main > section:nth-child(3) > div > mer-button:nth-child(1) > a';