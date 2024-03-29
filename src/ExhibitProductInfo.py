from __future__ import annotations


class ExhibitProductCommon():
    """
     @class     出品商品情報(共通設定部)
    """
    __strShippingCharge     : str = '';       # 配送料の負担
    __strShippingMethod     : str = '';       # 配送の方法
    __strShippingArea       : str = '';       # 発送元の地域
    __strShippingDays       : str = '';       # 発送までの日数
    
    
    def __init__(self,
                strShippingCharge,
                strShippingMethod,
                strShippingArea,
                strShippingDays
                ) ->  None:
        """
         @brief         コンストラクタ
         @detail        ProductList.xlsxの商品情報を登録（シート名：master）
         @param[in]     strShippingCharge       配送料の負担
         @param[in]     strShippingMethod       配送の方法
         @param[in]     strShippingArea         配送元の地域
         @param[in]     strShippingDays         発送までの日数
        """
        self.__strShippingCharge  = strShippingCharge;
        self.__strShippingMethod  = strShippingMethod;
        self.__strShippingArea    = strShippingArea;
        self.__strShippingDays    = strShippingDays;
        
        
    def getShippingCharge(self) ->  str:
        """
         @details       配送料の負担の取得
         @return        配送料の負担
        """
        return self.__strShippingCharge;
    
    def getShippingMethod(self) ->  str:
        """
         @details       配送料の方法の取得
         @return        配送料の方法
        """
        return self.__strShippingMethod;
    
    def getShippingArea(self) ->  str:
        """
         @details       配送元の地域取得
         @return        配送元の地域
        """
        return self.__strShippingArea;
    
    def getShippingDays(self) ->  str:
        """
         @details       発送までの日数の取得
         @return        発送までの日数
        """
        return self.__strShippingDays;
    
    
    
class ExhibitProductInfo():
    """
     @class     出品商品情報
    """
    __strProductNo                  : str   = '';       # 商品番号
    __strProductPhotoFlolderPath    : str   = '';       # 商品写真フォルダまでの絶対パス
    
    __strCategory_1                 : str   = '';       # カテゴリー_1      (※ユーザーの自由度を考慮し対象外)
    __strCategory_2                 : str   = '';       # カテゴリー_2      (※ユーザーの自由度を考慮し対象外)
    __strCategory_3                 : str   = '';       # カテゴリー_3      (※ユーザーの自由度を考慮し対象外)
    
    __strBrand_1                    : str   = '';       # ブランド  （商品次第では対象外）
    
    __strProductName                : str   = '';       # 商品名

    __strCommodityCondition         : str   = '';       # 商品の状態
    
    __nStartingPrice                : int   = 0;        # 出品開始額

    __strExplanation                : str   = '';       # 商品説明
    
    
    
    __objExhibitProductCommon: ExhibitProductCommon;
    
    
    def __init__(self,
                                strProductNo                : str,
                                strProductPhotoFlolderPath  : str,
                                strCategory_1               : str,
                                strCategory_2               : str,
                                strCategory_3               : str,
                                strBrand_1                  : str,
                                strProductName              : str,
                                strCommodityCondition       : str,
                                nStartingPrice              : int,
                                strExplanation              : str
                                ) ->  None:
        """
         @brief         コンストラクタ
         @detail        ProductList.xlsxの商品情報を登録（シート名：data）
         @param[in]     strProductNo                    商品ナンバー
         @param[in]     strProductPhotoFlolderPath      商品写真フォルダまでの絶対パス
         @param[in]     strCategory_1                   カテゴリー_1
         @param[in]     strCategory_2                   カテゴリー_2
         @param[in]     strCategory_3                   カテゴリー_3
         @param[in]     strBrand_1                      ブランド_1
         @param[in]     strProductName                  商品名
         @param[in]     strCommodityCondition           商品状態
         @param[in]     nStartingPrice                  出品開始額
         @param[in]     strExplanation                  商品説明
        """
        self.__strProductNo                   = strProductNo
        self.__strProductPhotoFlolderPath     = strProductPhotoFlolderPath
        self.__strCategory_1                  = strCategory_1
        self.__strCategory_2                  = strCategory_2
        self.__strCategory_3                  = strCategory_3
        self.__strBrand_1                     = strBrand_1
        self.__strProductName                 = strProductName
        self.__strCommodityCondition          = strCommodityCondition
        self.__nStartingPrice                 = nStartingPrice
        self.__strExplanation                 = strExplanation
        
        
    #! Setter
    def setExhibitProductCommon(self, objExhibitProductCommon: ExhibitProductCommon) ->  None:
        """
         @details       出品商品情報(共通設定部)の設定
         @param[in]     objExhibitProductCommon     出品商品情報(共通設定部)オブジェクト
        """
        self.__objExhibitProductCommon = objExhibitProductCommon;
        

    #! Getter
    def getProductNo(self):
        """
         @detail    商品ナンバーを取得
         @return    商品ナンバー
        """
        return  self.__strProductNo;
    
    def getProductPhotoFlolderPath(self):
        """
         @detail    商品写真フォルダまでの絶対パスを取得
         @return    self.__strProductPhotoFlolderPath    商品写真フォルダまでの絶対パス
        """
        return self.__strProductPhotoFlolderPath;
    
    
    def getCommodityCondition(self):
        """
         @detail    商品の状態を取得
         @return    self.__strCommodityCondition        商品の状態
        """
        return self.__strCommodityCondition;
    
    def getProductName(self):
        """
         @detail    商品名を取得
         @return    self.__strProductName     商品名
        """
        return self.__strProductName;
    
    def getProductExplanation(self):
        """
         @detail    商品説明を取得
         @return    self.__strExplanation     商品説明
        """
        return self.__strExplanation;
    
    def getStartingPrice(self):
        """
         @detail    出品開始額を取得
         @return    self.__nStartingPrice     出品開始額
        """
        return self.__nStartingPrice;
    
    
    def getExhibitProductCommon(self) ->  ExhibitProductCommon:
        """
         @details       出品商品情報(共通設定部)の取得
        """
        return self.__objExhibitProductCommon;