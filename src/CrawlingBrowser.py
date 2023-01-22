import sys
from tkinter import messagebox
from typing import List
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from telnetlib import EC
from bs4 import BeautifulSoup
import lxml
import re
import time
import random
import os
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import Const
import ProductInfo
import Log
import glob
import UserInfo
import ExhibitProductInfo


class CrawlingBrowser():
    """
     @class     ブラウザのクロールクラス
    """
    # ログクラス
    m_objLog: Log.Log = Log.Log();

    
    # 固定値設定クラス
    m_objSettingFile: Const.SettingFile = Const.SettingFile.staticSettingFile();
    
    # Webクローリング時のタグパス
    m_objCssSelector    : Const.CssSelector     = Const.CssSelector.staticCssSelector();
    m_objXpath          : Const.Xpath           = Const.Xpath.staticXpath();
    m_objClassName      : Const.ClassName       = Const.ClassName.staticClassName();

    
    # WebDriver
    m_objWebDriver: WebDriver;

    
    
    def __init__(self, objWebDriver: WebDriver):
        """
         @brief     コンストラクタ
         @details   WebDriverのインスタンス保持
        """
        self.m_objWebDriver = objWebDriver;
    
    
        
    
    def loginMercari(self, objUserInfo: UserInfo.UserInfo):
        """
         @detaila       メルカリログイン
         @param[in]     objUserInfo     ユーザー情報
        """
        self.m_objLog.LogDebug('メルカリログイン実行');
        
        
        # 要素が表示されるまでの待機処理 (最大待ち時間の設定)
        wait: WebDriverWait = WebDriverWait(self.m_objWebDriver, 10);
        # ランダムな秒数処理を停止（自動化を誤魔化す処理）
        waitsec: int = random.randint(1,3);
        
        try:
            # メルカリを開く
            self.m_objWebDriver.get(self.m_objSettingFile.MERCARI_HOME);
            time.sleep(waitsec);
            
            # 要素が全て検出できるまで待機
            wait.until(EC.presence_of_all_elements_located);
            self.m_objLog.LogDebug(f'HTML全ての要素が検出できるまで待機中...');
            
            # ログインキャッシュの有無
            if not objUserInfo.getExistCache():
                
                # ログイン
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.BTN_LOGIN)));
                self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_LOGIN).click();
                self.m_objLog.LogDebug('【ログイン】：「ログイン」ボタンを押下');
                
                # メールアドレスでログイン
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.BTN_MAIL_ADDRESS_LOGIN)));
                self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_MAIL_ADDRESS_LOGIN).click();
                self.m_objLog.LogDebug('【ログイン】：「メールアドレスでログイン」ボタンを押下');
                
                time.sleep(waitsec);
                
                # ユーザー情報入力
                wait.until(EC.visibility_of_element_located((By.NAME, 'emailOrPhone')));
                elmEmail = self.m_objWebDriver.find_element_by_name('emailOrPhone');
                elmEmail.send_keys(objUserInfo.getEmail());
                self.m_objLog.LogDebug('【ログイン】：「メールアドレス」を入力');
                
                wait.until(EC.visibility_of_element_located((By.NAME, 'password')));
                elmPass = self.m_objWebDriver.find_element_by_name('password');
                elmPass.send_keys(objUserInfo.getPass());
                self.m_objLog.LogDebug('【ログイン】：「パスワード」を入力');
                
                # ログイン実行
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.BTN_LOGIN_EXECUTION)));
                self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_LOGIN_EXECUTION).click();
                self.m_objLog.LogDebug('【ログイン】：「ログイン実行」ボタンを押下');
                
                # 初回2段階認証は手動対応
                strCurrentURL: str = self.m_objWebDriver.current_url;
                self.m_objLog.LogDebug('【ログイン】：2段階認証対応');
                
                # 現在のURLを取得し、変更されたら突破したと解釈しループを抜ける
                nWaitCount = 0;
                while strCurrentURL != self.m_objSettingFile.MERCARI_HOME:
                    time.sleep(waitsec);
                    strCurrentURL = self.m_objWebDriver.current_url;
                    
                    # 1分間、2段階認証が突破される事を待つ
                    nWaitCount += 1;
                    if nWaitCount == 30:
                        self.m_objLog.LogCritical('timeout：2段階認証コードの入力が確認できませんでした');
                        raise;
                    
                # ログインキャッシュの有無を「有」へ変更
                objUserInfo.setExistCache(True);
                
                
            # 初回ログイン時のポップアップ確認    
            try:
                # ポップアップが表示されているかの確認
                WebDriverWait(self.m_objWebDriver, waitsec).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.IMG_POPUP_SHOW)));
                
                # 閉じるボタンの押下
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.BTN_POPUP_HIDE)));
                self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_POPUP_HIDE).click();
            except:
                pass
            finally:
                self.m_objWebDriver.get(self.m_objSettingFile.MERCARI_HOME);
                
                    
        except Exception as e:
            self.m_objLog.LogCritical('ログインに失敗しました');
            sys.exit();
    
    
    
    
    def returnMercariHome(self):
        """
         @details       メルカリ ホーム画面に戻る
        """
        # メルカリ ホーム画面に戻る
        self.m_objWebDriver.get(self.m_objSettingFile.MERCARI_HOME);
        
        
    
    
    def getExhibitingList(self) ->  List[ProductInfo.ExhibitingProduct]:
        """
         @details       出品中の商品を取得
         @return        lstExhibitingProduct        出品商品のリスト
        """
        self.m_objLog.LogInfo('出品商品の取得');
        
        # 要素が表示されるまでの待機処理 (最大待ち時間の設定)
        wait: WebDriverWait = WebDriverWait(self.m_objWebDriver, 10);
        # ランダムな秒数処理を停止（自動化を誤魔化す処理）
        waitsec: int = random.randint(1,5);
        
        # 出品中の商品情報リスト
        lstExhibitingProduct: List[ProductInfo.ExhibitingProduct] = [];
        
        try:
            # アカウント
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.BTN_ACCOUNT)));
            self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_ACCOUNT).click();
            time.sleep(waitsec);
            
            # 出品した商品
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.BTN_LISTED_ITEM)));
            self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_LISTED_ITEM).click();
            time.sleep(waitsec);
            
            # 要素が全て検出できるまで待機
            wait.until(EC.presence_of_all_elements_located);
            self.m_objLog.LogDebug(f'HTML全ての要素が検出できるまで待機中...');
            
            # Web情報の取得（商品ページ）
            html = self.m_objWebDriver.page_source.encode('utf-8');
            soup = BeautifulSoup(html, 'lxml');
            
            # 出品中の商品情報が 1つもなければ終了
            if len(soup.find_all(text=re.compile("出品中の商品がありません"))) > 0:
                self.m_objLog.LogWarning(f'出品中の商品がありません');
                return lstExhibitingProduct;
            
            
            # もっと見る
            blChecl: bool = True;
            while blChecl:
                try:
                    WebDriverWait(self.m_objWebDriver, waitsec).until(EC.visibility_of_element_located((By.XPATH, self.m_objXpath.BTN_SEE_MORE)));
                    self.m_objWebDriver.find_element_by_xpath(self.m_objXpath.BTN_SEE_MORE).click();
                    time.sleep(waitsec);
                except:
                    #「もっと見る」要素がなくなるまでループ
                    blChecl = False;
                    pass;
            
            
            lstProductInfo: List = [];      # 出品されている商品名のリスト
            lstProductUrls: List = [];      # 出品されている商品URLのリスト
            
            # 商品名の取得
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.LST_PRODUCT)));
            lstProductInfo = self.m_objWebDriver.find_elements_by_css_selector(self.m_objCssSelector.LST_PRODUCT);
            self.m_objLog.LogInfo('全ての商品名を取得しました');

            # 商品URLの取得
            html = self.m_objWebDriver.page_source.encode('utf-8');
            soup = BeautifulSoup(html, 'lxml');
            lstProductUrls = soup.find_all(href=re.compile('/item/m'));
            self.m_objLog.LogInfo('全ての商品URLを取得しました');
            
            
        except Exception as ex:
            self.m_objLog.LogCritical('商品情報の取得中にエラーが発生しました。');
            print(f'ExceptionLog : {ex}');
            raise;
                

        for count in range(len(lstProductInfo)):
            # 商品名の整形
            strProductName  : str   = (lstProductInfo[count].text).split('\n')[0];
            # 商品IDの整形
            strProductId    : str   = (lstProductUrls[count].get('href')).split('/')[-1];
            # 商品URLの整形
            strProductUrl   : str   = self.m_objSettingFile.EXE_BASE_FILE_PATH + lstProductUrls[count].get('href');
                
            if strProductName != '' and strProductId != '' and strProductUrl != '':
                # 出品中の所品情報クラス
                objExhibitingProduct: ProductInfo.ExhibitingProduct = ProductInfo.ExhibitingProduct(strProductName, strProductId, strProductUrl);
                lstExhibitingProduct.append(objExhibitingProduct);
            else:
                self.m_objLog.LogError(f'{count}目の出品商品情報の取得に失敗しました。');
                pass;
            
        return lstExhibitingProduct;
    
    
    
    def exePriceCut(self, objPriceCutProduct: ProductInfo.PriceCutProduct) ->  ProductInfo.ExhibitingProduct:
        """
         @details       商品の値下げ実行
         @param[in]     objPriceCutProduct          値下げ商品情報
         @return        objExhibitingProduct        出品中の商品情報
        """
        self.m_objLog.LogInfo('商品の値下げ実行');

        # 要素が表示されるまでの待機処理 (最大待ち時間の設定)
        wait = WebDriverWait(self.m_objWebDriver, 10);
        # ランダムな秒数処理を停止（自動化を誤魔化す処理）
        waitsec: int = random.randint(2,7);
        
        
        # 値下げ商品情報
        strProductName  : str   = objPriceCutProduct.getProductName();
        strProductId    : str   = objPriceCutProduct.getProductId();
        strProductUrl   : str   = f'https://jp.mercari.com/item/{strProductId}';
        
        # 出品中の商品情報
        objExhibitingProduct: ProductInfo.ExhibitingProduct = ProductInfo.ExhibitingProduct(strProductName, strProductId, strProductUrl);
        
        
        self.m_objLog.LogInfo(f'商品ID［{strProductId}］の値下げを実行します\n［商品URL：{strProductUrl}］');
        try:
            # 商品ページへアクセス
            self.m_objWebDriver.get(strProductUrl);
            
            # 要素が全て検出できるまで待機
            # wait.until(EC.presence_of_all_elements_located)
            # self.m_objLog.LogDebug(f'HTML全ての要素が検出できるまで待機中...')
            time.sleep(waitsec);
            self.m_objLog.LogDebug(f'商品ページの HTMLが表示されるまでの待機処理中..');
            
            try:
                # 商品ページの HTML取得 (xml形式)
                html = self.m_objWebDriver.page_source.encode('utf-8');
                soup = BeautifulSoup(html, 'lxml');
                
            except Exception as ex:
                self.m_objLog.LogError(f'商品情報の HTMLを取得中にエラーが発生しました。商品ID［{strProductId}］');
                self.m_objLog.LogError(f'正しい判断ができないため、商品ID［{strProductId}］の操作はスキップします');
                print(f'ExceptionLog : {ex}');
                time.sleep(waitsec);
                raise;  #Exception(objExhibitingProduct)
            
            # 正常終了時の処理 (finally ≠ 終了時必ず)
            else:
                self.m_objLog.LogDebug(f'商品情報の HTMLを取得しました。商品ID［{strProductId}］');
                
        
            time.sleep(waitsec);
            
            # 商品情報の要素に「公開停止」状態の要素が含まれていたら終了
            lstStopPublishing: List = soup.find_all(text=re.compile("公開停止中"));
            if len(lstStopPublishing) > 0:
                objExhibitingProduct.setProductStopPublishing(True);
                
                self.m_objLog.LogWarning(f'商品状態が「公開停止」です。商品ID［{strProductId}］');
                return objExhibitingProduct;
            
            # 商品情報の要素に「削除」状態の要素が含まれていたら終了
            #（fix_1 : 2022/08/04）lstProductDelete = soup.find_all(text=re.compile("ページが見つかりませんでした"))
            lstProductDelete: List = soup.find_all(text=re.compile("この商品は削除されました"));
            if len(lstProductDelete) > 0:
                objExhibitingProduct.setProductDelete(True);
                
                self.m_objLog.LogWarning(f'商品が削除されている可能性があります。商品ID［{strProductId}］');
                return objExhibitingProduct;
            
            # 商品情報の要素に「売り切れ」状態の要素が含まれていたら終了
            lstSoldOut: List = soup.find_all(text=re.compile("売り切れ"));
            if len(lstSoldOut) > 0:
                objExhibitingProduct.setProductSoldOut(True);
                
                self.m_objLog.LogWarning(f'商品は既に売り切れています。商品ID［{strProductId}］');
                return objExhibitingProduct;
            
            
            # 出品価格取得
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.ELEM_PRICE)));
            strPrice: str = self.m_objWebDriver.find_elements_by_css_selector(self.m_objCssSelector.ELEM_PRICE)[0].text;
            lstNumber: List = strPrice.split(',');
            
            # 出品価格の値が文字列なので数値に変換後'¥'を削除
            strSubPrice: str = '';
            for strNumber in lstNumber:
                strSubPrice += strNumber;
            strSubPrice = strSubPrice.lstrip('¥');
            nCurrentPrice = int(strSubPrice);
            self.m_objLog.LogDebug(f'【商品画面】：現在の「出品価格」を取得 ->  商品価格［{nCurrentPrice}円］');
            
            # 予め設定された最安値価格より現在の出品価格が低ければ値下げを行わない
            nSettingCheapestPrice: int = objPriceCutProduct.getCheapestPrice();
            if nCurrentPrice <= nSettingCheapestPrice:
                self.m_objLog.LogInfo('設定された価格より現在の価格が下回るのでパスしました。');
                self.m_objLog.LogDebug(f'商品ID［{strProductId}］：現在の出品価格［{nCurrentPrice}円］< 最安値設定価格［{nSettingCheapestPrice}円］');
                time.sleep(waitsec);
                
                return objExhibitingProduct;
            
            try:
                # 商品の編集
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.BTN_PRODUCT_EDIT)));
                self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_PRODUCT_EDIT).click();
                self.m_objLog.LogDebug(f'【編集画面】：「商品の編集」ボタンを押下');
                
                # 販売価格の要素を取得
                wait.until(EC.visibility_of_element_located((By.CLASS_NAME, self.m_objClassName.INPUT_SELL_PRICE)));
                self.m_objWebDriver.find_element_by_class_name(self.m_objClassName.INPUT_SELL_PRICE).click();
                self.m_objLog.LogDebug(f'【編集画面】：「販売価格」の要素を取得');
                
                # 現在設定されている販売価格をクリア    #! ↓ ※clear関数が使用できない時の対処法
                # Windows
                if os.name == 'nt':
                    self.m_objWebDriver.find_element_by_class_name(self.m_objClassName.INPUT_SELL_PRICE).send_keys(Keys.CONTROL + "a");
                # Mac
                elif os.name == 'posix':
                    self.m_objWebDriver.find_element_by_class_name(self.m_objClassName.INPUT_SELL_PRICE).send_keys(Keys.COMMAND + "a");
                
                self.m_objWebDriver.find_element_by_class_name(self.m_objClassName.INPUT_SELL_PRICE).send_keys(Keys.DELETE);
                self.m_objWebDriver.find_element_by_class_name(self.m_objClassName.INPUT_SELL_PRICE).clear();
                self.m_objLog.LogDebug(f'【編集画面】：現値のクリア');
                
                # 現在の販売価格から値下げ価格を減算
                nSettingPriceCut: int = objPriceCutProduct.getPriceCut();
                nSettingPrice = nCurrentPrice - nSettingPriceCut;
                # 設定された値下げ価格へ変更
                self.m_objWebDriver.find_element_by_class_name(self.m_objClassName.INPUT_SELL_PRICE).send_keys(nSettingPrice);
                self.m_objLog.LogDebug(f'【編集画面】：現値={nCurrentPrice} から 値引額={nSettingPriceCut} を減算');
                
                time.sleep(waitsec);
                
                # 変更を適応して終了
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.BTN_CHANGED)));
                self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_CHANGED).click();
                self.m_objLog.LogDebug(f'【編集画面】：変更を適応');
                
                time.sleep(waitsec);
                self.m_objLog.LogInfo(f'商品ID［{strProductId}］を（{nSettingPriceCut}円）値下げしました');
                
                return objExhibitingProduct;
            
            except Exception as ex:
                self.m_objLog.LogError(f'商品価格の編集中にエラーが発生しました。商品ID［{strProductId}］');
                print(f'ExceptionLog : {ex}');
                time.sleep(waitsec);
                raise;  #Exception(objExhibitingProduct)
            
        except Exception as ex:
            self.m_objLog.LogError(f'商品ページに入る途中でエラーが発生しました。商品URL［https://jp.mercari.com/item/{strProductId}］');
            print(f'ExceptionLog : {ex}');
            time.sleep(waitsec);
            raise;  #Exception(objExhibitingProduct)
        
        
        
    def exeExhibitionProduct(self, objExhibitionProduct: ExhibitProductInfo.ExhibitProductInfo):
        """
         @detaila       商品出品
         @param[in]     objExhibitionProduct    出品商品情報
        """
        self.m_objLog.LogInfo('商品の出品実行');
        
        
        # 要素が表示されるまでの待機処理 (最大待ち時間の設定)
        wait = WebDriverWait(self.m_objWebDriver, 10);
        # ランダムな秒数処理を停止（自動化を誤魔化す処理）
        waitsec: int = random.randint(2,4);
        
        try:
            #!「出品」ボタンを押下
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.BTN_EXHIBIT)));
            self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_EXHIBIT).click();
            self.m_objLog.LogDebug(f'【操作】：ホーム画面「出品」ボタンを押下');
            time.sleep(waitsec);
            
            
            #!「出品する」ボタンを押下
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.BTN_EXHIBITING)));
            self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_EXHIBITING).click();
            self.m_objLog.LogDebug(f'【操作】：出品画面「出品する」ボタンを押下');
            time.sleep(waitsec);
            
            
            #! 出品画像（最大10枚）
            # wait.until(EC.visibility_of_element_located((By.XPATH, self.m_objXpath.INPUR_PICTURE)))
            objInputPicuture = self.m_objWebDriver.find_element_by_xpath(self.m_objXpath.INPUR_PICTURE);
            
            #? 以下の方法で画像をアップロードすると重複するので使用しない
            # for objToProductPhotoFileName in objExhibitionProduct.getToProductPhotoFileName():
            #     objInputPicuture.send_keys(objToProductPhotoFileName)
            
            # フォルダ内の拡張子が *.jpgのファイルを全て取得しリストで保持
            lstProductPhoto = glob.glob(f'{objExhibitionProduct.getProductPhotoFlolderPath()}/*.jpg');
            
            # 商品写真フォルダ内に写真が 1枚も存在しない場合はパス
            if len(lstProductPhoto) == 0:
                self.m_objLog.LogWarning(f'商品画像が 0枚なため挿入されません')
                pass

            else:
                # 制限枚数の 11枚目以上存在する場合はランダムで 10枚を選択 (※重複なし)
                if len(lstProductPhoto) >= 10:
                    lstProductPhoto = random.sample(lstProductPhoto, k=10)

                # リストで保持した各商品画像のファイル名(絶対パス)を '\n'で区切りで 1つの文字列へ変換
                strAllProductPhoto: str = '\n'.join(lstProductPhoto);
            
                # 商品画像を一括で挿入
                objInputPicuture.send_keys(strAllProductPhoto);
            
            self.m_objLog.LogDebug(f'【操作】：出品画面「出品画像」を挿入');
            
            
            #! カテゴリー
            # ユーザーの自由度を高めるため実装なし
            
            
            #! 商品の状態
            ## 取得した「商品の状態」から HTML内の value値に変更し取得
            strCommodityConditionVal = self.m_objCssSelector.selectCommodityCondition(objExhibitionProduct.getCommodityCondition());
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.SELECT_COMMODITY_CONDITION)));
            objSelectCommodityCondition = Select(self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.SELECT_COMMODITY_CONDITION));
            objSelectCommodityCondition.select_by_value(strCommodityConditionVal);
            self.m_objLog.LogDebug(f'【操作】：出品画面「商品の状態」を選択');
            
            
            #! 商品名
            strProductName = objExhibitionProduct.getProductName();
            strProductName = strProductName[:39];              # 文字数制限(40文字以内)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.INPUT_PRODUCT_NAME)));
            self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.INPUT_PRODUCT_NAME).send_keys(strProductName);
            self.m_objLog.LogDebug(f'【操作】：出品画面「商品名」を入力');
            
            
            #! 商品の説明
            strProductExplanation = objExhibitionProduct.getProductExplanation();
            strProductExplanation = strProductExplanation[:999];    # 文字数制限(1,000文字以内)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.INPUT_PRODUCT_EMPLANATION)));
            self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.INPUT_PRODUCT_EMPLANATION).send_keys(strProductExplanation);
            self.m_objLog.LogDebug(f'【操作】：出品画面「商品の説明」を入力');
                        
            
            ## 出品商品情報(共通設定部)を取得 シート名：master
            objExhibitProductCommon: ExhibitProductInfo.ExhibitProductCommon = objExhibitionProduct.getExhibitProductCommon();
            
            #! 配送料の負担
            strShippingChargeVal = self.m_objCssSelector.selectShippingChange(objExhibitProductCommon.getShippingCharge());
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.SELECT_SHIPPING_CHARGE)));
            objSelectShippingCharge = Select(self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.SELECT_SHIPPING_CHARGE));
            objSelectShippingCharge.select_by_value(strShippingChargeVal);
            self.m_objLog.LogDebug(f'【操作】：出品画面「配送料の負担」を選択');
            
            
            #! 配送の方法
            
            #? Ver.01  #####################################################################################################################################################
            # # 取得した「配送の方法」から HTML内の value値に変更し取得
            # strShippingMethod: str = self.m_objCssSelector.selectShippingMethodVer01(objExhibitProductCommon.getShippingMethod(), strShippingChargeVal);
            # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.SELECT_SHIPPING_METHOD_VER01)))
            # objSelectShippingMethod = Select(self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.SELECT_SHIPPING_METHOD_VER01))
            # objSelectShippingMethod.select_by_value(strShippingMethod)
            
            #? Ver.02  #####################################################################################################################################################
            # 配送の方法が既に選択されている場合、ボタンIDが異なるので対応
            try:
                ## 取得した「配送の方法」から HTML内の value値に変更し取得
                strShippingMethod: str = self.m_objCssSelector.selectShippingMethodVer02(objExhibitProductCommon.getShippingMethod(), strShippingChargeVal);
                try:
                    WebDriverWait(self.m_objWebDriver, waitsec).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.SELECT_ALREDY_SHIPPING_METHOD)))
                    self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.SELECT_ALREDY_SHIPPING_METHOD).click();
                except:
                    WebDriverWait(self.m_objWebDriver, waitsec).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.SELECT_SHIPPING_METHOD_VER02)))
                    self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.SELECT_SHIPPING_METHOD_VER02).click();
                finally:
                    time.sleep(waitsec);
                    
                self.m_objWebDriver.find_element_by_css_selector(strShippingMethod).click();
                time.sleep(waitsec);
                self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_SHIPPING_METHOD_UPDATE).click();
                self.m_objLog.LogDebug(f'【操作】：出品画面「配送の方法」を選択');
            except:
                self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_SHIPPING_METHOD_UPDATE).click();
                pass;
            #? #############################################################################################################################################################
            
            #! 発送元の地域
            ## 取得した「発送元の地域」から HTML内の value値に変更し取得
            strShippingAreaVal = self.m_objCssSelector.selectShippingArea(objExhibitProductCommon.getShippingArea());
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.SELECT_SHIPPING_AREA)));
            objSelectShippingArea = Select(self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.SELECT_SHIPPING_AREA));
            objSelectShippingArea.select_by_value(strShippingAreaVal);
            self.m_objLog.LogDebug(f'【操作】：出品画面「発送元の地域」を選択');
            
            
            #! 発送までの日数
            ## 取得した「発送までの日数」から HTML内の value値に変更し取得
            strShippingDaysVal = self.m_objCssSelector.selectShippingDays(objExhibitProductCommon.getShippingDays());
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.SELECT_SHIPPING_DAYS)));
            objSelectShippingDays = Select(self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.SELECT_SHIPPING_DAYS));
            objSelectShippingDays.select_by_value(strShippingDaysVal);
            self.m_objLog.LogDebug(f'【操作】：出品画面「発送までの日数」を選択');
            
            
            #! 販売価格    
            nStartingPrice = objExhibitionProduct.getStartingPrice();
            if nStartingPrice > 9999999:        # 販売金額が上限金額(9,999,999円)を上回る場合、最高額上限内で設定
                nStartingPrice = 9999999;
                self.m_objLog.LogWarning(f'販売価格の設定値が上限金額を超えて設定されているため、最高額の 9,999,999円で設定し直しました');
            elif nStartingPrice < 300:
                nStartingPrice = 300;
                self.m_objLog.LogWarning(f'販売価格の設定値が下限金額を超えて設定されているため、最低額の 300円で設定し直しました');
            strStartingPrice = str(nStartingPrice);
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.INPUT_STARTING_PRICE)));
            self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.INPUT_STARTING_PRICE).send_keys(strStartingPrice);
            self.m_objLog.LogDebug(f'【操作】：出品画面「販売価格」を入力 / 販売額={strStartingPrice}円');
            
            
            #!「下書きに保存」ボタンを押下
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.BTN_SAVE_TO_DRAFT)));
            self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_SAVE_TO_DRAFT).click();
            self.m_objLog.LogDebug(f'【操作】：出品画面「下書きに保存する」ボタンを押下');
            time.sleep(waitsec);
            

        except Exception as ex:
            self.m_objLog.LogError(f'商品を出品中にエラーが発生しました');
            print(f'ExceptionLog : {ex}');
            
            #!「下書きに保存」ボタンを押下
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.m_objCssSelector.BTN_SAVE_TO_DRAFT)));
            self.m_objWebDriver.find_element_by_css_selector(self.m_objCssSelector.BTN_SAVE_TO_DRAFT).click();
            self.m_objLog.LogInfo(f'出品途中にエラーが発生したので成功段階までを保存します［商品名：{objExhibitionProduct.getProductName()}］');
            time.sleep(waitsec);
            
            raise;