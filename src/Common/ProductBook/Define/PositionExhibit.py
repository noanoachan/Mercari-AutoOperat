from __future__ import annotations
import os
import sys



class PositionExhibit:
    """
    @class      出品商品のセル位置 
    @detail     セル情報をリストとして取得し取り出し時に使用するため以下の値
    @note       ファイル名      ProductList.xlsx
    """
    @classmethod
    def staticPositionExhibit(cls) ->  PositionExhibit:
        """
         @brief     static関数
         @return    PositionExhibit
        """
        return cls()
    
    # data
    GET_DATA_FIRST_ROW          : int   = 6;    # 商品情報が記載されている最初の行

    PRODUCT_NO                  : int   = 1;    # 商品ナンバー
    PRODUCT_PHOTO_FOLDER_PATH   : int   = 2;    # 商品写真のフォルダパス
    CATEGORY_1                  : int   = 3;    # カテゴリー_1
    CATEGORY_2                  : int   = 4;    # カテゴリー_2
    CATEGORY_3                  : int   = 5;    # カテゴリー_3
    BRAND_1                     : int   = 6;    # ブランド_1
    PRODUCT_NAME                : int   = 7;    # 商品名
    COMMODITY_CONDITION         : int   = 8;    # 商品状態
    STARTING_PRICE              : int   = 9;    # 出品開始額
    ALREADY_PRODUCT             : int   = 10;   # 出品(出品済みか否かの判定セル)
    PRODUCT_DETAILS_A           : int   = 11;   # 商品詳細_A
    PRODUCT_DETAILS_B           : int   = 12;   # 商品詳細_B
    PRODUCT_DETAILS_C           : int   = 13;   # 商品詳細_C
    PRODUCT_DETAILS_D           : int   = 14;   # 商品詳細_D
    PRODUCT_DETAILS_E           : int   = 15;   # 商品詳細_E
    PRODUCT_DETAILS_F           : int   = 16;   # 商品詳細_F
    PRODUCT_DETAILS_G           : int   = 17;   # 商品詳細_G
    PRODUCT_DETAILS_H           : int   = 18;   # 商品詳細_H
    PRODUCT_DETAILS_I           : int   = 19;   # 商品詳細_I
    PRODUCT_DETAILS_J           : int   = 20;   # 商品詳細_J
    PRODUCT_DETAILS_K           : int   = 21;   # 商品詳細_K
    PRODUCT_DETAILS_L           : int   = 22;   # 商品詳細_L
    
    
    
    # master
    SHUPPING_CHARGE : str   = 'B6';     # 配送料の負担
    SHUPPING_METHOD : str   = 'D6';     # 配送の方法
    SHUPPING_AREA   : str   = 'F6';     # 配送元の地域
    SHUPPING_DAYS   : str   = 'H6';     # 発送までの日数