from __future__ import annotations
import os
import sys



class ClassName:
    """
     @class     「商品の情報を編集」の ClassName定義クラス
    """
    @classmethod
    def staticClassName(cls) ->  ClassName:
        """
         @brief     static関数
         @return    ClassName
        """
        return cls()
    
    

    # テキストボックス：販売価格
    INPUT_SELL_PRICE: str = 'input-node.no-spin-button.with-prefix-label';