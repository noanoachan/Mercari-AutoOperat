class Product():
    """
     @class     商品情報
    """
    __m_strProductName = '';        # 商品名
    __m_strProductId   = '';        # 商品ID
    __m_strProductUrl  = '';        # 商品URL
    
    def __init__(self, strProductName, strProductId, strProductUrl: str = '') ->  None:
        """
         @detail        コンストラクタ
         @param[in]     strProductName      商品名
         @param[in]     strProductId        商品ID
         @param[in]     strProductUrl       商品Url
        """
        self.__m_strProductName   = strProductName;
        self.__m_strProductId     = strProductId;
        self.__m_strProductUrl     = strProductUrl;

    #! Getter
    def getProductName(self) ->  str:
        """
         @detail        商品名の取得
         @return        strProductName      商品名
        """
        return self.__m_strProductName;

    def getProductId(self) ->  str:
        """
         @detail        商品IDの取得
         @return        strProductID        商品ID
        """
        return self.__m_strProductId;
    
    def getProductUrl(self) ->  str:
        """
         @detail        商品URLの取得
         @return        strProductURL       商品URL
        """
        return self.__m_strProductUrl;
    
    
class ExhibitingProduct(Product):
    """
     @class     出品中の商品情報
    """
    m_blProductStopPublishing   = False;    # 公開停止
    m_blProductDelete           = False;    # 削除
    m_blProductSoldOut          = False;    # 売り切れ  
    
    
    #! Getter
    def getProductStopPublishing(self):
        """
         @detail        公開停止ステータスの取得
        """
        return self.m_blProductStopPublishing;
    
    def getProductDelete(self):
        """
         @detail        削除ステータスの取得
        """
        return self.m_blProductDelete;
    
    def getProductSoldOut(self):
        """
         @detail        売り切れ状態の取得
        """
        return self.m_blProductSoldOut;
    
    
    #! Setter
    def setProductStopPublishing(self, blProductStopPublishing):
        """
         @detail        公開停止状態の設定
         @param[in]     blProductStopPublishing     公開停止状態
        """
        self.m_blProductStopPublishing = blProductStopPublishing;
    
    def setProductDelete(self, blProductDelete):
        """
         @detail        削除状態の設定
         @param[in]     blProductDelete             削除状態
        """
        self.m_blProductDelete = blProductDelete;
        
    def setProductSoldOut(self, blProductSoldOut):
        """
         @detail        売り切れ状態の設定
         @param[in]     blProductSoldOut            売り切れ状態
        """
        self.m_blProductSoldOut = blProductSoldOut;
    
    
    
    
class PriceCutProduct(Product):
    """
     @class     値下げ商品情報
    """
    DISCOUNTED_PRICE    : int       = 100;                      # 値下げ価格（固定値：100円）
    
    __m_nPriceCut       : int       = DISCOUNTED_PRICE;         # 値下げ価格
    __m_nCheapestPrice  : int       = 0;                        # 最安値の設定値
    
    
    #! Getter
    def getPriceCut(self) ->  int:
        """
         @detail        値下げ価格の取得
        """
        return self.__m_nPriceCut;
    
    def getCheapestPrice(self) ->  int:
        """
         @detail        最安値の取得
        """
        return self.__m_nCheapestPrice;
    
    
    #! Setter
    def setCheapestPrice(self, nCheapestPrice) ->  bool:
        """
         @detail        最安値の設定
         @param[in]     nCheapestPrice      最安値
         @return        blRet               True:成功/False:失敗
        """
        blRet = True
        
        if nCheapestPrice != 0:
            self.m_nCheapestPrice = nCheapestPrice;
        else:
            blRet = False;
            
        return blRet;