from typing import List
from selenium.webdriver.edge.webdriver import WebDriver
import CrawlingBrowser
import Log
import Const
import ProductDataFile
import UserInfo
import ProductInfo
import ExhibitProductInfo


class ExecuteFunction:
    """
     @class     各機能実行クラス
    """

    # ログクラス
    m_objLog: Log.Log = Log.Log();
    

    # 固定値設定クラス
    m_objSettingFile: Const.SettingFile = Const.SettingFile.staticSettingFile();
    
    
    # ブラウザークローリングクラス
    __m_objCrawlingBrowser: CrawlingBrowser.CrawlingBrowser;
    
    
    # 商品ファイルの読み込みクラス
    __m_objReadData: ProductDataFile.ReadData = ProductDataFile.ReadData();
    
    # 商品ファイルの書き込みクラス
    __m_objWriteData: ProductDataFile.WriteData = ProductDataFile.WriteData();
        
    
    
    def __init__(self, objWebDriver: WebDriver) ->  None:
        """
         @details       コンストラクタ
         @paramp[in]    objWebDriver       WebDriver
        """
        self.__m_objCrawlingBrowser = CrawlingBrowser.CrawlingBrowser(objWebDriver);
    
    
    
    def loginMercari(self, objUserInfo: UserInfo.UserInfo) ->  None:
        """
         @details       メルカリログイン
         @param[in]     objUserInfo     ユーザー情報
        """
        self.__m_objCrawlingBrowser.loginMercari(objUserInfo)
    
    
    
    def getExhibitingList(self) ->  None:
        """
         @details       メルカリ上で既に出品中の商品を取得
        """
        try:
            ################################################################################################
            ### データ取得
            ################################################################################################
            # 出品中の商品情報の取得（商品名、商品ID、商品URL）
            lstExhibitingProduct: List[ProductInfo.ExhibitingProduct] = [];
            lstExhibitingProduct = self.__m_objCrawlingBrowser.getExhibitingList();
            self.m_objLog.LogInfo('メルカリ上の出品中である全ての商品情報の取得が完了しました');
            
            # 値下げ商品情報の取得（商品名、商品ID、最安値）
            lstPriceCutProduct: List[ProductInfo.PriceCutProduct] = [];
            lstPriceCutProduct = self.__m_objReadData.readPriceCutProduct();
            self.m_objLog.LogInfo(f'{self.m_objSettingFile.FILE_PRODUCT_LIST}［シート名：{self.m_objSettingFile.SHEET_PRICE_CUT}］に登録されてある商品情報の取得が完了しました');
            
            # 記録対象の出品中商品情報
            lstWriteProductInfo: List[ProductInfo.ExhibitingProduct] = [];

            # 商品情報ファイルに商品が1つも登録されていなければ全て追加
            if  len(lstPriceCutProduct) == 0:
                for objExhibitingProduct in lstExhibitingProduct:
                    lstWriteProductInfo.append(objExhibitingProduct);
                    self.m_objLog.LogInfo(f'登録商品情報にデータがないので新規追加します。商品ID：{objExhibitingProduct.getProductId()}');
            
            else:
                # メルカリ上の出品中の商品リスト
                for objExhibitingProduct in lstExhibitingProduct:
                    # 値下げ商品シートに登録されてある商品リスト
                    for objPriceCutProduct in lstPriceCutProduct:
                        
                        # 一致すれば次の出品中の商品情報へ
                        if objExhibitingProduct.getProductId() == objPriceCutProduct.getProductId():
                            break;
                        
                        # 最後の商品情報に到達すれば追加
                        elif objPriceCutProduct.getProductId() == lstPriceCutProduct[-1].getProductId():
                            lstWriteProductInfo.append(objExhibitingProduct);
                            self.m_objLog.LogInfo(f'登録商品情報にデータがないので新規追加します。商品ID：{objExhibitingProduct.getProductId()}');
                            
                        # 一致しなければ次の商品情報へ
                        elif objExhibitingProduct.getProductId() != objPriceCutProduct.getProductId():
                            continue;
                        
            # データファイルへ書き込み
            self.__m_objWriteData.writeGetProductInfo(lstWriteProductInfo);
            # 重複商品を「再出品商品」とし「最安値」を設定
            self.__m_objWriteData.writeResetLowestPrice();
            
            # メルカリ ホーム画面に戻る
            self.__m_objCrawlingBrowser.returnMercariHome();
                
        except Exception as ex:
            # メルカリ ホーム画面に戻る
            self.__m_objCrawlingBrowser.returnMercariHome();
            raise ex;
        
        
    def exePriceCut(self) -> None:
        """
         @details       メルカリ上で既に出品中の商品を値下げ
        """
        ################################################################################################
        ### 値下げ
        ################################################################################################
        try:
            # 値下げ商品情報の取得（商品名、商品ID、最安値）
            lstPriceCutProduct: List[ProductInfo.PriceCutProduct] = [];
            lstPriceCutProduct = self.__m_objReadData.readPriceCutProduct();
            self.m_objLog.LogInfo(f'{self.m_objSettingFile.FILE_PRODUCT_LIST}［シート名：{self.m_objSettingFile.SHEET_PRICE_CUT}］に登録されてある商品情報の取得が完了しました');
            
            # 抽出した商品情報を元に値下げを実行
            lstSuccessProduct   : List[ProductInfo.ExhibitingProduct]   = [];       # 成功した商品のリスト
            lstFailedProduct    : List[ProductInfo.PriceCutProduct]     = [];       # 失敗した商品のリスト
            for objPriceCutProduct in lstPriceCutProduct:
                try:
                    # 値下げ時に取得した商品情報を取得
                    objExhibitingProduct: ProductInfo.ExhibitingProduct = self.__m_objCrawlingBrowser.exePriceCut(objPriceCutProduct);
                    lstSuccessProduct.append(objExhibitingProduct);
                except:
                    lstFailedProduct.append(objPriceCutProduct);
                    pass;
            
            # 通信環境などによって実行されなかった商品を再度「値下げ」実行
            self.m_objLog.LogInfo(f'通信状況等で「値下げ」が行われなかった商品{len(lstFailedProduct)}個を再値下げを実行します');
            MAX_FAILED_LOOP: int = 5;       # 再値下げ実行回数制限
            nFailedLoopCount: int = 1;
            while len(lstFailedProduct) > 0:
                # 再値下げ回数制限 5回目以内
                if(nFailedLoopCount <= MAX_FAILED_LOOP):
                    for i in range(len(lstFailedProduct)):
                        try:
                            objExhibitingProduct: ProductInfo.ExhibitingProduct = self.__m_objCrawlingBrowser.exePriceCut(lstFailedProduct[i]);
                            lstSuccessProduct.append(objExhibitingProduct);
                            lstFailedProduct.pop(i);
                            break;
                        except:
                            pass;
                        finally:
                            self.m_objLog.LogInfo(f'再値下げ実行回数：{nFailedLoopCount}回目');
                            # 再値下げ回数制限インクリメント
                            nFailedLoopCount += 1;
                else:
                    break;
            
            # データファイルへ書き込み
            self.m_objLog.LogDebug(f'商品数={len(lstSuccessProduct)}個を書き込みます');
            self.__m_objWriteData.writePriceCutProductStatus(lstSuccessProduct);
            
            # メルカリ ホーム画面に戻る
            self.__m_objCrawlingBrowser.returnMercariHome();
            
        except Exception as ex:
            # メルカリ ホーム画面に戻る
            self.__m_objCrawlingBrowser.returnMercariHome();
            raise ex;
        
    
    def exeExhibit(self) ->  None:
        """
         @details       設定ファイルに登録されている商品を出品
        """
        ################################################################################################
        ### 出品
        ################################################################################################
        try:
            lstExhibitProductInfo: List[ExhibitProductInfo.ExhibitProductInfo] = [];
            lstExhibitProductInfo = self.__m_objReadData.readExhibitProduct();
            
            if len(lstExhibitProductInfo) < 1:
                self.m_objLog.LogError('登録されている商品は全て出品されています');
                return;
            
            self.m_objLog.LogInfo('登録されている商品情報の取得が【完了】しました');
            
            
            # 抽出した商品情報を元に出品を実行
            lstSuccessProduct: List[ExhibitProductInfo.ExhibitProductInfo] = [];            # 成功した商品のリスト
            lstErrorProduct: List[ExhibitProductInfo.ExhibitProductInfo] = [];              # 失敗した商品のリスト
            self.m_objLog.LogInfo(f'{len(lstExhibitProductInfo)}個の商品を出品します');
            
            for objExhibitProductInfo in lstExhibitProductInfo:
                try:
                    self.m_objLog.LogInfo(f'商品No.「{objExhibitProductInfo.getProductNo()}」を出品します');
                    self.__m_objCrawlingBrowser.exeExhibitionProduct(objExhibitProductInfo);
                    lstSuccessProduct.append(objExhibitProductInfo);    # 成功
                except:
                    lstErrorProduct.append(objExhibitProductInfo);      # 失敗
                    pass
                
                # メルカリ ホーム画面に戻る
                self.__m_objCrawlingBrowser.returnMercariHome();
                
            self.m_objLog.LogInfo(f'商品全体数：{len(lstExhibitProductInfo)}  成功：{len(lstSuccessProduct)}  失敗：{len(lstErrorProduct)}');
            
            
            # データファイルへ書き込み
            self.m_objLog.LogDebug(f'商品数={len(lstSuccessProduct)}個を書き込みます');
            self.__m_objWriteData.writeExhibitProductStatus(lstSuccessProduct);
            
            # メルカリ ホーム画面に戻る
            self.__m_objCrawlingBrowser.returnMercariHome();
            
        except Exception as ex:
            # メルカリ ホーム画面に戻る
            self.__m_objCrawlingBrowser.returnMercariHome();
            raise ex;