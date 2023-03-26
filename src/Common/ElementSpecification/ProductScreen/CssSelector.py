from __future__ import annotations
import os
import sys



class CssSelector:
    """
     @class     「商品画面」の CSSSelector定義クラス
    """
    @classmethod
    def staticCssSelector(cls) ->  CssSelector:
        """
         @brief     static関数
         @return    CssSelector
        """
        return cls()
    

    # 出品価格
    # (fix_1 : 2022/04/28) ELEM_PRICE = '#item-info > section:nth-child(1) > section:nth-child(2) > mer-text > mer-price'
    # (fix_2 : 2022/11/19) ELEM_PRICE = '#item-info > section:nth-child(1) > section:nth-child(2) > div > mer-price'
    # (fix_3 : 2022/12/11) ELEM_PRICE: str = '#item-info > section:nth-child(1) > section:nth-child(2) > div > div';
    # (fix_4 : 2023/01/19)ELEM_PRICE = '#item-info > section:nth-child(1) > section:nth-child(2) > div > mer-price'
    ELEM_PRICE: str = '#item-info > section:nth-child(1) > section:nth-child(2) > div > div'


    # 商品の編集
    BTN_PRODUCT_EDIT: str = '#item-info > section:nth-child(1) > div:nth-child(5) > mer-button > a';