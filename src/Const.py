from __future__ import annotations
import os
import sys


    

class SettingFile:
    """
     @class     固定値設定クラス
    """
    @classmethod
    def staticSettingFile(cls) ->  SettingFile:
        """
         @brief     static関数
         @return    SettingFile
        """
        return cls()
    
    # メルカリの URL
    MERCARI_HOME: str = 'https://jp.mercari.com/';
    
    # 実行環境までの絶対パス
    EXE_BASE_FILE_PATH: str = os.path.dirname(os.path.abspath(sys.argv[0]));   # ×：__file__  / ○：sys.argv[0]
    
    # ログインキャッシュが格納されているフォルダ名
    FOLDER_LOGIN_CACHE: str = 'LoginCache';
    
    # ユーザー情報が記載されているファイル名
    FILE_USER_INFO: str = 'UserInfo.xml';
    
    
    # 値下げ商品のファイル名
    # FILE_LISTING_LIST: str = 'ListingList.xlsx';
    
    
    # 出品商品のファイル名
    FILE_PRODUCT_LIST: str = 'ProductList.xlsx';
    # 出品商品ファイルのシート名：data
    SHEET_DATA: str = 'data';
    # 出品商品ファイルのシート名：master
    SHEET_MASTER: str = 'master';
    # 出品商品ファイルのシート名：setting
    SHEET_SETTING: str = 'setting';
    # 出品商品ファイルのシート名：template
    SHEET_TEMPLATE: str = 'template';
    # 出品商品ファイルのシート名：PriceCut
    SHEET_PRICE_CUT: str = 'PriceCut';
    
    # 出品商品の写真が格納されているフォルダ名
    FOLDER_PRODUCT_PHOTO: str = 'ProductPhoto';
    
    
    

class CssSelector:
    """
     @class     クローリング時の css_selector
    """
    @classmethod
    def staticCssSelector(cls) ->  CssSelector:
        """
         @brief     static関数
         @return    CssSelector
        """
        return cls()
    
    
    # ログイン
    BTN_LOGIN: str = '#gatsby-focus-wrapper > div > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-navigation-top-menu-item:nth-child(2) > span';
    # メールアドレスでログイン
    # (fix_1 : 2022/06/06) BTN_MAIL_ADDRESS_LOGIN = '#root > div > div > div > main > div > div > div > div > mer-button.style_loginButton__1-1k6.mer-spacing-b-24.style_email__1PIYq > a'
    # (fix_2 : 2022/08/04) BTN_MAIL_ADDRESS_LOGIN = '#root > div > div > div > main > div > div > div > div > mer-button.style_loginButton__nsWU0.mer-spacing-b-24.style_email__T3Zi1 > a'
    BTN_MAIL_ADDRESS_LOGIN: str = '#root > div > div > div > main > div > div > div > mer-button.style_loginButton__nsWU0.mer-spacing-b-24.style_email__T3Zi1 > a';
    # ログイン実行
    BTN_LOGIN_EXECUTION: str = '#root > div > div > div > main > div > div > form > mer-button > button';
    # 認証して完了する
    #（fix_1 : 2022/08/02）BTN_TWO_STEP_VERIFICATION = '#root > div > div > div > main > div > div > div > div.sc-hHEiqL.YzGzU > form > mer-button > button'
    BTN_TWO_STEP_VERIFICATION: str = '#root > div > div > div > main > div > div > div > div.sc-kEqXSa.NEeOg > form > mer-button > button';
    
    # 初回ログイン時のポップアップ確認
    IMG_POPUP_SHOW: str = '#modal > div.inner > div.header > picture > img';
    # 閉じる (ポップアップ)
    BTN_POPUP_HIDE: str = 'body > mer-information-popup > div > mer-button:nth-child(1) > button';
    
    
    ###########################################################
    # 値下げ
    ###########################################################
    # アカウント
    BTN_ACCOUNT: str = '#gatsby-focus-wrapper > div > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-menu > mer-navigation-top-menu-item > span';
    # 出品した商品
    BTN_LISTED_ITEM: str = '#gatsby-focus-wrapper > div > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-menu > div > mer-list > mer-list-item:nth-child(4) > a';
    
    # 商品リスト
    LST_PRODUCT: str = '#currentListing > mer-list mer-list-item';
    
    # 出品価格
    # (fix_1 : 2022/04/28) ELEM_PRICE = '#item-info > section:nth-child(1) > section:nth-child(2) > mer-text > mer-price'
    # (fix_2 : 2022/11/19) ELEM_PRICE = '#item-info > section:nth-child(1) > section:nth-child(2) > div > mer-price'
    # (fix_3 : 2022/12/11) ELEM_PRICE: str = '#item-info > section:nth-child(1) > section:nth-child(2) > div > div';
    ELEM_PRICE = '#item-info > section:nth-child(1) > section:nth-child(2) > div > mer-price'
    
    
    # 商品の編集
    BTN_PRODUCT_EDIT: str = '#item-info > section:nth-child(1) > div:nth-child(5) > mer-button > a';
    
    # 変更する
    #（fix_1 : 2022/04/28）BTN_CHANGED = '#main > form > div.layout__FlexWrapper-sc-1lyi7xi-9.eNrnaj > mer-button:nth-child(1) > button'
    #（fix_2 : 2022/08/02）BTN_CHANGED = '#main > form > div.layout__FlexWrapper-sc-1lyi7xi-9.cQBeFq > mer-button:nth-child(1) > button'
    #（fix_3 : 2022/11/19）BTN_CHANGED = '#main > form > div.layout__FlexWrapper-sc-1lyi7xi-9.cFSybX > mer-button:nth-child(1) > button'
    BTN_CHANGED: str = '#main > form > div.layout__FlexWrapper-sc-1lyi7xi-9.elfNBA > mer-button:nth-child(1) > button';
    
    
    ###########################################################
    # 出品
    ###########################################################
    # ホーム画面「出品」ボタン
    BTN_EXHIBIT: str = '#gatsby-focus-wrapper > div > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-button > a';
    
    # 出品画面「出品する」ボタン
    # (fix_1 : 2022/11/02) BTN_EXHIBITING = '#main > section:nth-child(2) > div > a.OldSellerHomeContent__ListItemButton-sc-2xo3fq-0.bbGatD.mer-spacing-r-16'
    BTN_EXHIBITING: str = '#main > section:nth-child(3) > div > mer-button:nth-child(1) > a';
    
    #! 出品画像
    # Xpathに登録
    
    #! 商品の出品画面「カテゴリー_1」
    # その他
    SELECT_CATEGORY_Val10: str = '#main > form > section:nth-child(2) > mer-select:nth-child(2) > div > label > div.mer-select > select > option:nth-child(14)';
    #! 商品の出品画面「カテゴリー_2」
    # その他
    SELECT_CATEGORY_Val10: str = '#main > form > section:nth-child(2) > mer-select:nth-child(3) > div > div.mer-select > select > option:nth-child(10)';
    
    # 出品画面「商品名」挿入
    INPUT_PRODUCT_NAME: str = '#main > form > section:nth-child(3) > mer-text-input > div > label > div.mer-text-input-container > input';
    
    # 出品画面「商品説明」挿入項目
    INPUT_PRODUCT_EMPLANATION: str = '#main > form > section:nth-child(3) > mer-textarea > div > label > textarea.input-node';
    
    
    #! 出品画面「商品の状態」選択項目
    SELECT_COMMODITY_CONDITION: str = '#main > form > section:nth-child(2) > mer-select.mer-spacing-t-16 > div > label > div.mer-select > select';
    def selectCommodityCondition(self, strCommodityCondition: str) ->  str:
        """
         @detail        取得した「商品の状態」から適切な valueを返す
         @param[in]     strCommodityCondition       商品の状態
         @return        nCommodityConditionVal      HTML内の value値
        """
        ### 商品状態
        PRODUCT_STATUS_1: int = 1;      # 新品、未使用
        PRODUCT_STATUS_2: int = 2;      # 未使用に近い
        PRODUCT_STATUS_3: int = 3;      # 目立った傷や汚れなし
        PRODUCT_STATUS_4: int = 4;      # やや傷や汚れあり
        PRODUCT_STATUS_5: int = 5;      # 傷や汚れあり
        PRODUCT_STATUS_6: int = 6;      # 全体的に状態が悪い
        
        
        # return
        nCommodityConditionVal: int;
        
        if strCommodityCondition ==     '新品、未使用':
            nCommodityConditionVal = PRODUCT_STATUS_1;
        elif strCommodityCondition ==   '未使用に近い':
            nCommodityConditionVal = PRODUCT_STATUS_2;
        elif strCommodityCondition ==   '目立った傷や汚れなし':
            nCommodityConditionVal = PRODUCT_STATUS_3;
        elif strCommodityCondition ==   'やや傷や汚れあり':
            nCommodityConditionVal = PRODUCT_STATUS_4;
        elif strCommodityCondition ==   '傷や汚れあり':
            nCommodityConditionVal = PRODUCT_STATUS_5;
        elif strCommodityCondition ==   '全体的に状態が悪い':
            nCommodityConditionVal = PRODUCT_STATUS_6;
        else:
            nCommodityConditionVal = PRODUCT_STATUS_2;
            
        return str(nCommodityConditionVal);

    
    #! 出品画面「配送料の負担」選択項目
    SELECT_SHIPPING_CHARGE: str = '#main > form > section:nth-child(4) > div:nth-child(2) > mer-select:nth-child(1) > div > label > div.mer-select > select';
    def selectShippingChange(self, strShippingChange) ->  str:
        """
         @detail        取得した「配送料の負担」から IDを整形
         @param[in]     strShippingChange       配送料の負担
         @return        nShippingChangeVal      HTML内の value値
        """
        ### 配送料の負担
        POSTAGE_INCLUDE : int = 2;      # 送料込み（出品者負担）
        CASH_ON_DELIVERY: int = 1;      # 着払い（購入者負担）
        
        
        # return
        nShippingChangeVal: int;
        
        if strShippingChange    == '送料込み（出品者負担）':
            nShippingChangeVal  = POSTAGE_INCLUDE;
        elif strShippingChange  == '着払い（購入者負担）':
            nShippingChangeVal  = CASH_ON_DELIVERY;
            
        else:                   # 送料込み（出品者負担）
            nShippingChangeVal  = POSTAGE_INCLUDE;
            
        return str(nShippingChangeVal);
    
    
    #! 配送の方法(ver.01)
    SELECT_SHIPPING_METHOD_VER01: str = '#main > form > section:nth-child(4) > div:nth-child(2) > mer-select.mer-spacing-t-24 > div > label > div.mer-select > select'
    def selectShippingMethodVer01(self, strShippingMethod: str, strShippingChargeVal: str) ->  str:
        """
         @detail         取得した「配送の方法」から IDを整形
         @param[in]     strShippingMethod       配送の方法
         @param[in]     strShippingCharge       配送料の負担
         @return        nShippingMethodVal      HTML内の value値
        """
        ### 着払い（購入者負担）
        CASH_ON_DELIVERY                    : str   = '1';              # 着払い（購入者負担）
        CASH_ON_DELIVERY__TO_BE_DECIDED     : int   = 1;                # 未定
        CASH_ON_DELIVERY__KURONEKO_YAMATO   : int   = 3;                # クロネコヤマト
        CASH_ON_DELIVERY__YU_PACK           : int   = 4;                # ゆうパック
        CASH_ON_DELIVERY__YU_NAIL           : int   = 15;               # ゆうメール
        
        ### 送料込み（出品者負担）
        POSTAGE_INCLUDED                            : str   = '2';      # 送料込み（出品者負担）
        POSTAGE_INCLUDED__TO_BE_DECIDED             : int   = 5;        # 未定
        POSTAGE_INCLUDED__EASY_MERCARI_SHIPPING     : int   = 14;       # らくらくメルカリ便
        POSTAGE_INCLUDED__YU_YU_MERCARI_SHIPPING    : int   = 17;       # ゆうゆうメルカリ便
        POSTAGE_INCLUDED__PACKING_AND_SHIPPING      : int   = 16;       # 梱包・発送たのメル便
        POSTAGE_INCLUDED__YU_NAIL                   : int   = 6;        # ゆうメール
        POSTAGE_INCLUDED__LETTER_PACK               : int   = 8;        # レターパック
        POSTAGE_INCLUDED__REGUAL_MAIL               : int   = 9;        # 普通郵便(定型、定形外)
        POSTAGE_INCLUDED__KURONEKO_YAMATO           : int   = 10;       # クロネコヤマト
        POSTAGE_INCLUDED__YU_PACK                   : int   = 11;       # ゆうパック
        POSTAGE_INCLUDED__CLICK_POST                : int   = 13;       # クリックポスト
        POSTAGE_INCLUDED__YU_PACKET                 : int   = 7;        # ゆうパケット
        
        
        # return
        nShippingMethodVal: int;
        
        ################################################################################
        # 着払い（購入者負担）
        if strShippingChargeVal     == CASH_ON_DELIVERY:
            
            if strShippingMethod    == '未定':
                nShippingMethodVal  = CASH_ON_DELIVERY__TO_BE_DECIDED;
                
            elif strShippingMethod  == 'クロネコヤマト':
                nShippingMethodVal  = CASH_ON_DELIVERY__KURONEKO_YAMATO;
                
            elif strShippingMethod  == 'ゆうパック':
                nShippingMethodVal  = CASH_ON_DELIVERY__YU_PACK;
                
            elif strShippingMethod  == 'ゆうメール':
                nShippingMethodVal  = CASH_ON_DELIVERY__YU_NAIL;
                
            else:                   # 未定
                nShippingMethodVal  = CASH_ON_DELIVERY__TO_BE_DECIDED;
                
        
        ################################################################################
        # 送料込み（出品者負担）
        elif strShippingChargeVal   == POSTAGE_INCLUDED:
            
            if strShippingMethod    == '未定':
                nShippingMethodVal  = POSTAGE_INCLUDED__TO_BE_DECIDED;
                
            elif strShippingMethod  == 'らくらくメルカリ便':
                nShippingMethodVal  = POSTAGE_INCLUDED__EASY_MERCARI_SHIPPING;
                
            elif strShippingMethod  == 'ゆうゆうメルカリ便':
                nShippingMethodVal  = POSTAGE_INCLUDED__YU_YU_MERCARI_SHIPPING;
                
            elif strShippingMethod  == '梱包・発送たのメル便':
                nShippingMethodVal  = POSTAGE_INCLUDED__PACKING_AND_SHIPPING;
                
            elif strShippingMethod  == 'ゆうメール':
                nShippingMethodVal  = POSTAGE_INCLUDED__YU_NAIL;
                
            elif strShippingMethod  == 'レターパック':
                nShippingMethodVal  = POSTAGE_INCLUDED__LETTER_PACK;
                
            elif strShippingMethod  == '普通郵便(定型、定形外)':
                nShippingMethodVal  = POSTAGE_INCLUDED__REGUAL_MAIL;
                
            elif strShippingMethod  == 'クロネコヤマト':
                nShippingMethodVal  = POSTAGE_INCLUDED__KURONEKO_YAMATO;
                
            elif strShippingMethod  == 'ゆうパック':
                nShippingMethodVal  = POSTAGE_INCLUDED__YU_PACK;
                
            elif strShippingMethod  == 'クリックポスト':
                nShippingMethodVal  = POSTAGE_INCLUDED__CLICK_POST;
                
            elif strShippingMethod  == 'ゆうパケット':
                nShippingMethodVal  = POSTAGE_INCLUDED__YU_PACKET;
                
            else:                   # 未定
                nShippingMethodVal  = POSTAGE_INCLUDED__TO_BE_DECIDED;
        else:
            nShippingMethodVal  = 99999;
            
            
        return str(nShippingMethodVal);
    
    
    #! 配送の方法(ver.02)
    SELECT_SHIPPING_METHOD_VER02    : str = '#main > form > section:nth-child(4) > div:nth-child(2) > div > mer-text-link > a';
    SELECT_ALREDY_SHIPPING_METHOD   : str = '#main > form > section:nth-child(4) > div:nth-child(2) > div > div > mer-text-link > a'        # 既にいずれか選択されている場合
    BTN_SHIPPING_METHOD_UPDATE      : str = 'body > div.UpdateButton__Container-sc-1fr5w7e-0.gUsjyr > mer-button > button'                  # 配送の方法に変更があった場合の「更新」ボタン
    def selectShippingMethodVer02(self, strShippingMethod: str, strShippingChargeVal: str) ->  str:
        """
         @detail         取得した「配送の方法」から IDを整形
         @param[in]     strShippingMethod       配送の方法
         @param[in]     strShippingCharge       配送料の負担
         @return        nShippingMethodVal      HTML内の各配送方法の CssSelector
        """
        ### 着払い（購入者負担）
        CASH_ON_DELIVERY                    : str       = '1';                                                                                                          # 着払い（購入者負担）
        CASH_ON_DELIVERY__TO_BE_DECIDED     : str       = '#main > form > mer-radio-group > div:nth-child(1) > mer-radio-label > mer-radio > input';                    # 未定
        CASH_ON_DELIVERY__KURONEKO_YAMATO   : str       = '#main > form > mer-radio-group > div:nth-child(3) > mer-radio-label > mer-radio > input[type=radio]';        # クロネコヤマト
        CASH_ON_DELIVERY__YU_PACK           : str       = '#main > form > mer-radio-group > div:nth-child(5) > mer-radio-label > mer-radio > input[type=radio]';        # ゆうパック
        CASH_ON_DELIVERY__YU_NAIL           : str       = '#main > form > mer-radio-group > div:nth-child(7) > mer-radio-label > mer-radio > input[type=radio]';        # ゆうメール
        
        ### 送料込み（出品者負担）
        POSTAGE_INCLUDED                            : str   = '2';                                                                                                      # 送料込み（出品者負担）
        POSTAGE_INCLUDED__TO_BE_DECIDED             : str   = '#main > form > mer-radio-group > div:nth-child(7) > mer-radio-label > mer-radio > input';                # 未定
        POSTAGE_INCLUDED__EASY_MERCARI_SHIPPING     : str   = '#main > form > mer-radio-group > div:nth-child(1) > mer-radio-label > mer-radio > input[type=radio]';    # らくらくメルカリ便
        POSTAGE_INCLUDED__YU_YU_MERCARI_SHIPPING    : str   = '#main > form > mer-radio-group > div:nth-child(3) > mer-radio-label > mer-radio > input[type=radio]';    # ゆうゆうメルカリ便
        POSTAGE_INCLUDED__PACKING_AND_SHIPPING      : str   = '#main > form > mer-radio-group > div:nth-child(5) > mer-radio-label > mer-radio > input[type=radio]';    # 梱包・発送たのメル便
        POSTAGE_INCLUDED__YU_NAIL                   : str   = '#main > form > mer-radio-group > div:nth-child(9) > mer-radio-label > mer-radio > input[type=radio]';    # ゆうメール
        POSTAGE_INCLUDED__LETTER_PACK               : str   = '#main > form > mer-radio-group > div:nth-child(11) > mer-radio-label > mer-radio > input[type=radio]';   # レターパック
        POSTAGE_INCLUDED__REGUAL_MAIL               : str   = '#main > form > mer-radio-group > div:nth-child(13) > mer-radio-label > mer-radio > input[type=radio]';   # 普通郵便(定型、定形外)
        POSTAGE_INCLUDED__KURONEKO_YAMATO           : str   = '#main > form > mer-radio-group > div:nth-child(15) > mer-radio-label > mer-radio > input[type=radio]';   # クロネコヤマト
        POSTAGE_INCLUDED__YU_PACK                   : str   = '#main > form > mer-radio-group > div:nth-child(17) > mer-radio-label > mer-radio > input[type=radio]';   # ゆうパック
        POSTAGE_INCLUDED__CLICK_POST                : str   = '#main > form > mer-radio-group > div:nth-child(19) > mer-radio-label > mer-radio > input[type=radio]';   # クリックポスト
        POSTAGE_INCLUDED__YU_PACKET                 : str   = '#main > form > mer-radio-group > div:nth-child(21) > mer-radio-label > mer-radio > input[type=radio]';   # ゆうパケット
        

        # return
        strShippingMethodVal : str;
        
        ################################################################################
        # 着払い（購入者負担）
        if strShippingChargeVal         == CASH_ON_DELIVERY:
            strShippingMethodVal        = CASH_ON_DELIVERY__TO_BE_DECIDED;
            
            if strShippingMethod        == '未定':
                strShippingMethodVal    = CASH_ON_DELIVERY__TO_BE_DECIDED;
                
            elif strShippingMethod      == 'クロネコヤマト':
                strShippingMethodVal    = CASH_ON_DELIVERY__KURONEKO_YAMATO;
                
            elif strShippingMethod      == 'ゆうパック':
                strShippingMethodVal    = CASH_ON_DELIVERY__YU_PACK;
                
            elif strShippingMethod      == 'ゆうメール':
                strShippingMethodVal    = CASH_ON_DELIVERY__YU_NAIL;
                
            else:                       # 未定
                strShippingMethodVal    = CASH_ON_DELIVERY__TO_BE_DECIDED;
                
        
        ################################################################################
        # 送料込み（出品者負担）
        elif strShippingChargeVal       == POSTAGE_INCLUDED:
            strShippingMethodVal        = POSTAGE_INCLUDED__TO_BE_DECIDED;
            
            if strShippingMethod        == '未定':
                strShippingMethodVal    = POSTAGE_INCLUDED__TO_BE_DECIDED;
                
            elif strShippingMethod      == 'らくらくメルカリ便':
                strShippingMethodVal    = POSTAGE_INCLUDED__EASY_MERCARI_SHIPPING;
                
            elif strShippingMethod      == 'ゆうゆうメルカリ便':
                strShippingMethodVal    = POSTAGE_INCLUDED__YU_YU_MERCARI_SHIPPING;
                
            elif strShippingMethod      == '梱包・発送たのメル便':
                strShippingMethodVal    = POSTAGE_INCLUDED__PACKING_AND_SHIPPING;
                
            elif strShippingMethod      == 'ゆうメール':
                strShippingMethodVal    = POSTAGE_INCLUDED__YU_NAIL;
                
            elif strShippingMethod      == 'レターパック':
                strShippingMethodVal    = POSTAGE_INCLUDED__LETTER_PACK;
                
            elif strShippingMethod      == '普通郵便(定型、定形外)':
                strShippingMethodVal    = POSTAGE_INCLUDED__REGUAL_MAIL;
                
            elif strShippingMethod      == 'クロネコヤマト':
                strShippingMethodVal    = POSTAGE_INCLUDED__KURONEKO_YAMATO;
                
            elif strShippingMethod      == 'ゆうパック':
                strShippingMethodVal    = POSTAGE_INCLUDED__YU_PACK;
                
            elif strShippingMethod      == 'クリックポスト':
                strShippingMethodVal    = POSTAGE_INCLUDED__CLICK_POST;
                
            elif strShippingMethod      == 'ゆうパケット':
                strShippingMethodVal    = POSTAGE_INCLUDED__YU_PACKET;
                
            else:                       # 未定
                strShippingMethodVal    = POSTAGE_INCLUDED__TO_BE_DECIDED;
                
        else: 
            strShippingMethodVal    = ' ';
            
        return strShippingMethodVal;
    

    #! 発送元の地域
    SELECT_SHIPPING_AREA: str = '#main > form > section:nth-child(4) > mer-select:nth-child(3) > div > label > div.mer-select > select';
    def selectShippingArea(self, strShippingArea: str) ->  str:
        """
         @detail         取得した「都道府県名」から IDを整形
         @param[in]     strShippingArea      都道府県名
         @return        nShippingAreaVal     HTML内の value値
        """
        
        # return
        nShippingAreaVal: int;
        
        if strShippingArea == '北海道':
            nShippingAreaVal = 1;
        elif strShippingArea == '青森県':
            nShippingAreaVal = 2;
        elif strShippingArea == '岩手県':
            nShippingAreaVal = 3;
        elif strShippingArea == '宮城県':
            nShippingAreaVal = 4;
        elif strShippingArea == '秋田県':
            nShippingAreaVal = 5;
        elif strShippingArea == '山形県':
            nShippingAreaVal = 6;
        elif strShippingArea == '福島県':
            nShippingAreaVal = 7;
        elif strShippingArea == '茨城県':
            nShippingAreaVal = 8;
        elif strShippingArea == '栃木県':
            nShippingAreaVal = 9;
        elif strShippingArea == '群馬県':
            nShippingAreaVal = 10;
        elif strShippingArea == '埼玉県':
            nShippingAreaVal = 11;
        elif strShippingArea == '千葉県':
            nShippingAreaVal = 12;
        elif strShippingArea == '東京都':
            nShippingAreaVal = 13;
        elif strShippingArea == '神奈川県':
            nShippingAreaVal = 14;
        elif strShippingArea == '新潟県':
            nShippingAreaVal = 15;
        elif strShippingArea == '富山県':
            nShippingAreaVal = 16;
        elif strShippingArea == '石川県':
            nShippingAreaVal = 17;
        elif strShippingArea == '福井県':
            nShippingAreaVal = 18;
        elif strShippingArea == '山梨県':
            nShippingAreaVal = 19;
        elif strShippingArea == '長野県':
            nShippingAreaVal = 20;
        elif strShippingArea == '岐阜県':
            nShippingAreaVal = 21;
        elif strShippingArea == '静岡県':
            nShippingAreaVal = 22;
        elif strShippingArea == '愛知県':
            nShippingAreaVal = 23;
        elif strShippingArea == '三重県':
            nShippingAreaVal = 24;
        elif strShippingArea == '滋賀県':
            nShippingAreaVal = 25;
        elif strShippingArea == '京都府':
            nShippingAreaVal = 26;
        elif strShippingArea == '大阪府':
            nShippingAreaVal = 27;
        elif strShippingArea == '兵庫県':
            nShippingAreaVal = 28;
        elif strShippingArea == '奈良県':
            nShippingAreaVal = 29;
        elif strShippingArea == '和歌山県':
            nShippingAreaVal = 30;
        elif strShippingArea == '鳥取県':
            nShippingAreaVal = 31;
        elif strShippingArea == '島根県':
            nShippingAreaVal = 32;
        elif strShippingArea == '岡山県':
            nShippingAreaVal = 33;
        elif strShippingArea == '広島県':
            nShippingAreaVal = 34;
        elif strShippingArea == '山口県':
            nShippingAreaVal = 35;
        elif strShippingArea == '徳島県':
            nShippingAreaVal = 36;
        elif strShippingArea == '香川県':
            nShippingAreaVal = 37;
        elif strShippingArea == '愛媛県':
            nShippingAreaVal = 38;
        elif strShippingArea == '高知県':
            nShippingAreaVal = 39;
        elif strShippingArea == '福岡県':
            nShippingAreaVal = 40;
        elif strShippingArea == '佐賀県':
            nShippingAreaVal = 41;
        elif strShippingArea == '長崎県':
            nShippingAreaVal = 42;
        elif strShippingArea == '熊本県':
            nShippingAreaVal = 43;
        elif strShippingArea == '大分県':
            nShippingAreaVal = 44;
        elif strShippingArea == '宮城県':
            nShippingAreaVal = 45;
        elif strShippingArea == '鹿児島県':
            nShippingAreaVal = 46;
        elif strShippingArea == '沖縄県':
            nShippingAreaVal = 47;
        elif strShippingArea == '未定':
            nShippingAreaVal = 99;
        else:                   # 未定
            nShippingAreaVal = 99;
    
        return str(nShippingAreaVal);
    
    
    #! 発送までの日数
    SELECT_SHIPPING_DAYS: str = '#main > form > section:nth-child(4) > mer-select:nth-child(4) > div > label > div.mer-select > select';
    def selectShippingDays(self, strShippingDays: str) ->  str:
        """
         @detail        取得した「発送までの日数」から IDを整形
         @param[in]     strShippingDays         発送までの日数
         @return        strShippingDaysVal      HTML内の value値
        """
        # 発送までの日数
        SHIPPING_DAYS_1: int = 1;
        SHIPPING_DAYS_2: int = 2;
        SHIPPING_DAYS_3: int = 3;
        
        
        # return
        nShippingDaysVal: int;
        
        if strShippingDays      == '1~2日で発送':
            nShippingDaysVal    = SHIPPING_DAYS_1;
        elif strShippingDays    == '2~3日で発送':
            nShippingDaysVal    = SHIPPING_DAYS_2;
        elif strShippingDays    == '4~7日で発送':
            nShippingDaysVal    = SHIPPING_DAYS_3;
        else:                   # 1~2日で発送
            nShippingDaysVal    = SHIPPING_DAYS_1;
            
        return str(nShippingDaysVal);
    
    
    # 販売価格
    INPUT_STARTING_PRICE: str = '#main > form > section:nth-child(5) > div:nth-child(2) > mer-text-input > div > label > div.mer-text-input-container > input';
    
    # 下書きに保存（※ユーザーの要望）出品までは行わない
    #(fix_1 : 2022/11/02 )BTN_SAVE_TO_DRAFT = '#main > form > div.layout__FlexWrapper-sc-1lyi7xi-9.cFSybX > mer-button:nth-child(2) > button'
    BTN_SAVE_TO_DRAFT: str = '#main > form > div.layout__FlexWrapper-sc-1lyi7xi-9.elfNBA > mer-button:nth-child(2) > button';
    
class ClassName:
    """
     @class     クローリング時の class_name
    """
    @classmethod
    def staticClassName(cls) ->  ClassName:
        """
         @brief     static関数
         @return    ClassName
        """
        return cls()
    
    
    # 販売価格
    INPUT_SELL_PRICE: str = 'input-node.no-spin-button.with-prefix-label';
    
    
    
class Xpath:
    """
    @class     クローリング時の Xpath
    """
    @classmethod
    def staticXpath(cls) ->  Xpath:
        """
         @brief     static関数
         @return    Xpath
        """
        return cls()
    
    
    ###########################################################
    # データ取得
    ###########################################################
    # もっと見る
    BTN_SEE_MORE: str = '//*[@id="currentListing"]/div/mer-button/button';
    
    # 商品リスト中の価格
    ELEM_LIST_ON_PRICE: str = '//*[@id="currentListing"]/mer-list/mer-list-item[1]/a/mer-item-object//div/div/div[1]/mer-text/mer-price//span[2]';
    
    
    ###########################################################
    # 出品
    ###########################################################
    #! 出品画像
    #INPUR_PICTURE: str = '//*[@id="main"]/form/section[1]/div/div[3]/input';
    INPUR_PICTURE: str = '//*[@id="main"]/form/section[1]/div/div[5]/input'
    
    
    
class CellPositionPriceCut:
    """
    @class      値下げ商品のセル位置
    @detail     セル情報をリストとして取得し取り出し時に使用するため以下の値
    @note       ファイル名      ProductList.xlsx    (シート名：PriceCut)
    """
    @classmethod
    def staticCellPositionPriceCut(cls) ->  CellPositionPriceCut:
        """
         @brief     static関数
         @return    CellPositionPriceCut
        """
        return cls()
    
    
    PRODUCT_NAME    : int   = 0;        # 商品名
    PRODUCT_ID      : int   = 1;        # 商品ID
    CHEAPES_PRICE   : int   = 2;        # 最安値
    REMARKS         : int   = 3;        # 備考
    
    
    
class CellPositionExhibit:
    """
    @class      出品商品のセル位置 
    @detail     セル情報をリストとして取得し取り出し時に使用するため以下の値
    @note       ファイル名      ProductList.xlsx
    """
    @classmethod
    def staticCellPositionExhibit(cls) ->  CellPositionExhibit:
        """
         @brief     static関数
         @return    CellPositionExhibit
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