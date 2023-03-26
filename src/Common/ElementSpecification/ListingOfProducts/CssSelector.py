from __future__ import annotations
from multiprocessing.managers import DictProxy
import os
import sys
import Log



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
    

    # ログクラス
    LOG: Log.Log = Log.Log();
    

    #! テキストボックス：カテゴリー_1（その他）
    SELECT_CATEGORY1: str = '#main > form > section:nth-child(2) > mer-select:nth-child(2) > div > label > div.mer-select > select > option:nth-child(14)';
    
    
    #! テキストボックス：カテゴリー_2（その他）
    SELECT_CATEGORY2: str = '#main > form > section:nth-child(2) > mer-select:nth-child(3) > div > div.mer-select > select > option:nth-child(10)';
    

    # テキストボックス：商品名
    INPUT_PRODUCT_NAME: str = '#main > form > section:nth-child(3) > mer-text-input > div > label > div.mer-text-input-container > input';
    
    # 商品名の入力文字数制限
    LIMIT_NUM_PRODUCT_NAME: int = 39;
    

    # テキストボックス：商品説明
    INPUT_PRODUCT_EMPLANATION: str = '#main > form > section:nth-child(3) > mer-textarea > div > label > textarea.input-node';

    # 商品説明の入力文字数制限
    LIMIT_NUM_PRODUCT_EMPLANATION: int = 999;


    #! プルダウン：商品の状態
    SELECT_COMMODITY_CONDITION: str = '#main > form > section:nth-child(2) > mer-select.mer-spacing-t-16 > div > label > div.mer-select > select';


    ### 商品の状態
    __PRODUCT_STATUS_1: int = 1;      # 新品、未使用
    __PRODUCT_STATUS_2: int = 2;      # 未使用に近い
    __PRODUCT_STATUS_3: int = 3;      # 目立った傷や汚れなし
    __PRODUCT_STATUS_4: int = 4;      # やや傷や汚れあり
    __PRODUCT_STATUS_5: int = 5;      # 傷や汚れあり
    __PRODUCT_STATUS_6: int = 6;      # 全体的に状態が悪い

    #「商品の状態」種別に応じた HTMLの value値
    __dicProductStatus = {
        '新品、未使用'            : __PRODUCT_STATUS_1,
        '未使用に近い'            : __PRODUCT_STATUS_2,
        '目立った傷や汚れなし'    : __PRODUCT_STATUS_3,
        'やや傷や汚れあり'        : __PRODUCT_STATUS_4,
        '傷や汚れあり'            : __PRODUCT_STATUS_5,
        '全体的に状態が悪い'      : __PRODUCT_STATUS_6
        };

    #! プルダウン：配送料の負担
    SELECT_SHIPPING_CHARGE: str = '#main > form > section:nth-child(4) > div:nth-child(2) > mer-select:nth-child(1) > div > label > div.mer-select > select';


    ### 配送料の負担
    __POSTAGE_INCLUDE : int = 2;      # 送料込み（出品者負担）
    __CASH_ON_DELIVERY: int = 1;      # 着払い（購入者負担）

    #「商品の状態」種別に応じた HTMLの value値
    __dicShippingChange = {
        '送料込み（出品者負担）'           : __POSTAGE_INCLUDE,
        '着払い（購入者負担）'             : __CASH_ON_DELIVERY
        };
    

    #! プルダウン：配送の方法(ver.01)
    SELECT_SHIPPING_METHOD_VER01: str = '#main > form > section:nth-child(4) > div:nth-child(2) > mer-select.mer-spacing-t-24 > div > label > div.mer-select > select'

    ### 着払い（購入者負担）
    __VER1_CASH_ON_DELIVERY                            : str   = '1';      # 着払い（購入者負担）
    __VER1_CASH_ON_DELIVERY__TO_BE_DECIDED             : int   = 1;        # 未定
    __VER1_CASH_ON_DELIVERY__KURONEKO_YAMATO           : int   = 3;        # クロネコヤマト
    __VER1_CASH_ON_DELIVERY__YU_PACK                   : int   = 4;        # ゆうパック
    __VER1_CASH_ON_DELIVERY__YU_NAIL                   : int   = 15;       # ゆうメール

    #「配送料の負担」種別に応じた HTMLの value値
    __dicCathOnDeliveryVer01: dict = {
        '未定'            : __VER1_CASH_ON_DELIVERY__TO_BE_DECIDED, 
        'クロネコヤマト'  : __VER1_CASH_ON_DELIVERY__KURONEKO_YAMATO,
        'ゆうパック'      : __VER1_CASH_ON_DELIVERY__YU_PACK,
        'ゆうメール'      : __VER1_CASH_ON_DELIVERY__YU_NAIL
        };

    ### 送料込み（出品者負担）
    __VER1_POSTAGE_INCLUDED                            : str   = '2';      # 送料込み（出品者負担）
    __VER1_POSTAGE_INCLUDED__TO_BE_DECIDED             : int   = 5;        # 未定
    __VER1_POSTAGE_INCLUDED__EASY_MERCARI_SHIPPING     : int   = 14;       # らくらくメルカリ便
    __VER1_POSTAGE_INCLUDED__YU_YU_MERCARI_SHIPPING    : int   = 17;       # ゆうゆうメルカリ便
    __VER1_POSTAGE_INCLUDED__PACKING_AND_SHIPPING      : int   = 16;       # 梱包・発送たのメル便
    __VER1_POSTAGE_INCLUDED__YU_NAIL                   : int   = 6;        # ゆうメール
    __VER1_POSTAGE_INCLUDED__LETTER_PACK               : int   = 8;        # レターパック
    __VER1_POSTAGE_INCLUDED__REGUAL_MAIL               : int   = 9;        # 普通郵便(定型、定形外)
    __VER1_POSTAGE_INCLUDED__KURONEKO_YAMATO           : int   = 10;       # クロネコヤマト
    __VER1_POSTAGE_INCLUDED__YU_PACK                   : int   = 11;       # ゆうパック
    __VER1_POSTAGE_INCLUDED__CLICK_POST                : int   = 13;       # クリックポスト
    __VER1_POSTAGE_INCLUDED__YU_PACKET                 : int   = 7;        # ゆうパケット

    #「配送料の負担」種別に応じた HTMLの value値
    __dicPostageIncludedVer01: dict = {
        '未定'                    : __VER1_POSTAGE_INCLUDED__TO_BE_DECIDED, 
        'らくらくメルカリ便'      : __VER1_POSTAGE_INCLUDED__EASY_MERCARI_SHIPPING,
        'ゆうゆうメルカリ便'      : __VER1_POSTAGE_INCLUDED__YU_YU_MERCARI_SHIPPING,
        '梱包・発送たのメル便'    : __VER1_POSTAGE_INCLUDED__PACKING_AND_SHIPPING,
        'ゆうメール'              : __VER1_POSTAGE_INCLUDED__YU_NAIL,
        'レターパック'            : __VER1_POSTAGE_INCLUDED__LETTER_PACK,
        '普通郵便(定型、定形外)'  : __VER1_POSTAGE_INCLUDED__REGUAL_MAIL,
        'クロネコヤマト'          : __VER1_POSTAGE_INCLUDED__KURONEKO_YAMATO,
        'ゆうパック'              : __VER1_POSTAGE_INCLUDED__YU_PACK,
        'クリックポスト'          : __VER1_POSTAGE_INCLUDED__CLICK_POST,
        'ゆうパケット'            : __VER1_POSTAGE_INCLUDED__YU_PACKET
        };

    #「配送料の負担」種別に応じた「配送の方法」の value値を保持
    __dicShippingMethodVer01: dict = {__VER1_CASH_ON_DELIVERY : __dicCathOnDeliveryVer01, __VER1_POSTAGE_INCLUDED : __dicPostageIncludedVer01};
    

    #! プルダウン：配送の方法(ver.02)
    # (fix_1 : 2023/03/25) SELECT_SHIPPING_METHOD_VER02    : str = '#main > form > section:nth-child(4) > div:nth-child(2) > div > mer-text-link > a';
    SELECT_SHIPPING_METHOD_VER02    : str = '#main > form > section:nth-child(4) > div:nth-child(2) > div > span > a'

    # 既にいずれか選択されている場合
    # (fix_1 : 2023/03/25) SELECT_ALREDY_SHIPPING_METHOD   : str = '#main > form > section:nth-child(4) > div:nth-child(2) > div > div > mer-text-link > a'
    SELECT_ALREDY_SHIPPING_METHOD   : str = '#main > form > section:nth-child(4) > div:nth-child(2) > div > div > span > a'

    # 配送の方法に変更があった場合の「更新」ボタン
    # (fix_1 : 2023/03/05) BTN_SHIPPING_METHOD_UPDATE      : str = 'body > div.UpdateButton__Container-sc-1fr5w7e-0.gUsjyr > mer-button > button'
    # (fix_2 : 2023/03/11) BTN_SHIPPING_METHOD_UPDATE      : str = 'body > div.sc-d9357a98-0.jTolJt > mer-button > button'
    BTN_SHIPPING_METHOD_UPDATE      : str = 'body > div.sc-829bba56-0.jTVys > mer-button > button'


    ### 着払い（購入者負担）
    __VER2_CASH_ON_DELIVERY                             : str       = '1';                                                                                                          # 着払い（購入者負担）
    __VER2_CASH_ON_DELIVERY__TO_BE_DECIDED              : str       = '#main > form > mer-radio-group > div:nth-child(1) > mer-radio-label > mer-radio > input';                    # 未定
    __VER2_CASH_ON_DELIVERY__KURONEKO_YAMATO            : str       = '#main > form > mer-radio-group > div:nth-child(3) > mer-radio-label > mer-radio > input[type=radio]';        # クロネコヤマト
    __VER2_CASH_ON_DELIVERY__YU_PACK                    : str       = '#main > form > mer-radio-group > div:nth-child(5) > mer-radio-label > mer-radio > input[type=radio]';        # ゆうパック
    __VER2_CASH_ON_DELIVERY__YU_NAIL                    : str       = '#main > form > mer-radio-group > div:nth-child(7) > mer-radio-label > mer-radio > input[type=radio]';        # ゆうメール

    #「配送料の負担」種別に応じた HTMLの value値
    __dicCathOnDeliveryVer02: dict = {
        "未定"            : __VER2_CASH_ON_DELIVERY__TO_BE_DECIDED, 
        "クロネコヤマト"  : __VER2_CASH_ON_DELIVERY__KURONEKO_YAMATO,
        "ゆうパック"      : __VER2_CASH_ON_DELIVERY__YU_PACK,
        "ゆうメール"      : __VER2_CASH_ON_DELIVERY__YU_NAIL
        };
    
    ### 送料込み（出品者負担）
    __VER2_POSTAGE_INCLUDED                             : str       = '2';                                                                                                          # 送料込み（出品者負担）
    __VER2_POSTAGE_INCLUDED__TO_BE_DECIDED              : str       = '#main > form > mer-radio-group > div:nth-child(7) > mer-radio-label > mer-radio > input';                    # 未定
    __VER2_POSTAGE_INCLUDED__EASY_MERCARI_SHIPPING      : str       = '#main > form > mer-radio-group > div:nth-child(1) > mer-radio-label > mer-radio > input[type=radio]';        # らくらくメルカリ便
    __VER2_POSTAGE_INCLUDED__YU_YU_MERCARI_SHIPPING     : str       = '#main > form > mer-radio-group > div:nth-child(3) > mer-radio-label > mer-radio > input[type=radio]';        # ゆうゆうメルカリ便
    __VER2_POSTAGE_INCLUDED__PACKING_AND_SHIPPING       : str       = '#main > form > mer-radio-group > div:nth-child(5) > mer-radio-label > mer-radio > input[type=radio]';        # 梱包・発送たのメル便
    __VER2_POSTAGE_INCLUDED__YU_NAIL                    : str       = '#main > form > mer-radio-group > div:nth-child(9) > mer-radio-label > mer-radio > input[type=radio]';        # ゆうメール
    __VER2_POSTAGE_INCLUDED__LETTER_PACK                : str       = '#main > form > mer-radio-group > div:nth-child(11) > mer-radio-label > mer-radio > input[type=radio]';       # レターパック
    __VER2_POSTAGE_INCLUDED__REGUAL_MAIL                : str       = '#main > form > mer-radio-group > div:nth-child(13) > mer-radio-label > mer-radio > input[type=radio]';       # 普通郵便(定型、定形外)
    __VER2_POSTAGE_INCLUDED__KURONEKO_YAMATO            : str       = '#main > form > mer-radio-group > div:nth-child(15) > mer-radio-label > mer-radio > input[type=radio]';       # クロネコヤマト
    __VER2_POSTAGE_INCLUDED__YU_PACK                    : str       = '#main > form > mer-radio-group > div:nth-child(17) > mer-radio-label > mer-radio > input[type=radio]';       # ゆうパック
    __VER2_POSTAGE_INCLUDED__CLICK_POST                 : str       = '#main > form > mer-radio-group > div:nth-child(19) > mer-radio-label > mer-radio > input[type=radio]';       # クリックポスト
    __VER2_POSTAGE_INCLUDED__YU_PACKET                  : str       = '#main > form > mer-radio-group > div:nth-child(21) > mer-radio-label > mer-radio > input[type=radio]';       # ゆうパケット

    #「配送料の負担」種別に応じた HTMLの value値
    __dicPostageIncludedVer02: dict = {
    '未定'                    : __VER2_POSTAGE_INCLUDED__TO_BE_DECIDED, 
    'らくらくメルカリ便'      : __VER2_POSTAGE_INCLUDED__EASY_MERCARI_SHIPPING,
    'ゆうゆうメルカリ便'      : __VER2_POSTAGE_INCLUDED__YU_YU_MERCARI_SHIPPING,
    '梱包・発送たのメル便'    : __VER2_POSTAGE_INCLUDED__PACKING_AND_SHIPPING,
    'ゆうメール'              : __VER2_POSTAGE_INCLUDED__YU_NAIL,
    'レターパック'            : __VER2_POSTAGE_INCLUDED__LETTER_PACK,
    '普通郵便(定型、定形外)'  : __VER2_POSTAGE_INCLUDED__REGUAL_MAIL,
    'クロネコヤマト'          : __VER2_POSTAGE_INCLUDED__KURONEKO_YAMATO,
    'ゆうパック'              : __VER2_POSTAGE_INCLUDED__YU_PACK,
    'クリックポスト'          : __VER2_POSTAGE_INCLUDED__CLICK_POST,
    'ゆうパケット'            : __VER2_POSTAGE_INCLUDED__YU_PACKET
    };

    #「配送料の負担」種別に応じた「配送の方法」の value値を保持
    __dicShippingMethodVer02: dict = {__VER2_CASH_ON_DELIVERY : __dicCathOnDeliveryVer02, __VER2_POSTAGE_INCLUDED : __dicPostageIncludedVer02};


    #! 発送元の地域
    SELECT_SHIPPING_AREA: str = '#main > form > section:nth-child(4) > mer-select:nth-child(3) > div > label > div.mer-select > select';

    ### 「発送元の地域」種別に応じた HTMLの value値
    __SHIPPING_AREA_VAL01: int   = 1;
    __SHIPPING_AREA_VAL02: int   = 2;
    __SHIPPING_AREA_VAL03: int   = 3;
    __SHIPPING_AREA_VAL04: int   = 4;
    __SHIPPING_AREA_VAL05: int   = 5;
    __SHIPPING_AREA_VAL06: int   = 6;
    __SHIPPING_AREA_VAL07: int   = 7;
    __SHIPPING_AREA_VAL08: int   = 8;
    __SHIPPING_AREA_VAL09: int   = 9;
    __SHIPPING_AREA_VAL10: int   = 10;
    __SHIPPING_AREA_VAL11: int   = 11;
    __SHIPPING_AREA_VAL12: int   = 12;
    __SHIPPING_AREA_VAL13: int   = 13;
    __SHIPPING_AREA_VAL14: int   = 14;
    __SHIPPING_AREA_VAL15: int   = 15;
    __SHIPPING_AREA_VAL16: int   = 16;
    __SHIPPING_AREA_VAL17: int   = 17;
    __SHIPPING_AREA_VAL18: int   = 18;
    __SHIPPING_AREA_VAL19: int   = 19;
    __SHIPPING_AREA_VAL20: int   = 20;
    __SHIPPING_AREA_VAL21: int   = 21;
    __SHIPPING_AREA_VAL22: int   = 22;
    __SHIPPING_AREA_VAL23: int   = 23;
    __SHIPPING_AREA_VAL24: int   = 24;
    __SHIPPING_AREA_VAL25: int   = 25;
    __SHIPPING_AREA_VAL26: int   = 26;
    __SHIPPING_AREA_VAL27: int   = 27;
    __SHIPPING_AREA_VAL28: int   = 28;
    __SHIPPING_AREA_VAL29: int   = 29;
    __SHIPPING_AREA_VAL30: int   = 30;
    __SHIPPING_AREA_VAL31: int   = 31;
    __SHIPPING_AREA_VAL32: int   = 32;
    __SHIPPING_AREA_VAL33: int   = 33;
    __SHIPPING_AREA_VAL34: int   = 34;
    __SHIPPING_AREA_VAL35: int   = 35;
    __SHIPPING_AREA_VAL36: int   = 36;
    __SHIPPING_AREA_VAL37: int   = 37;
    __SHIPPING_AREA_VAL38: int   = 38;
    __SHIPPING_AREA_VAL39: int   = 39;
    __SHIPPING_AREA_VAL40: int   = 40;
    __SHIPPING_AREA_VAL41: int   = 41;
    __SHIPPING_AREA_VAL42: int   = 42;
    __SHIPPING_AREA_VAL43: int   = 43;
    __SHIPPING_AREA_VAL44: int   = 44;
    __SHIPPING_AREA_VAL45: int   = 45;
    __SHIPPING_AREA_VAL46: int   = 46;
    __SHIPPING_AREA_VAL47: int   = 47;
    __SHIPPING_AREA_VAL48: int   = 48;

    #「発送元の地域」種別に応じた「配送の方法」の value値を保持
    __dicShippingArea: dict = {
    '北海道'       : __SHIPPING_AREA_VAL01, 
    '青森県'       : __SHIPPING_AREA_VAL02, 
    '岩手県'       : __SHIPPING_AREA_VAL03, 
    '宮城県'       : __SHIPPING_AREA_VAL04, 
    '秋田県'       : __SHIPPING_AREA_VAL05, 
    '山形県'       : __SHIPPING_AREA_VAL06, 
    '福島県'       : __SHIPPING_AREA_VAL07, 
    '茨城県'       : __SHIPPING_AREA_VAL08, 
    '栃木県'       : __SHIPPING_AREA_VAL09, 
    '群馬県'       : __SHIPPING_AREA_VAL10, 
    '埼玉県'       : __SHIPPING_AREA_VAL11, 
    '千葉県'       : __SHIPPING_AREA_VAL12, 
    '東京都'       : __SHIPPING_AREA_VAL13, 
    '神奈川県'     : __SHIPPING_AREA_VAL14, 
    '新潟県'       : __SHIPPING_AREA_VAL15, 
    '富山県'       : __SHIPPING_AREA_VAL16, 
    '石川県'       : __SHIPPING_AREA_VAL17, 
    '福井県'       : __SHIPPING_AREA_VAL18, 
    '山梨県'       : __SHIPPING_AREA_VAL19, 
    '長野県'       : __SHIPPING_AREA_VAL20, 
    '岐阜県'       : __SHIPPING_AREA_VAL21, 
    '静岡県'       : __SHIPPING_AREA_VAL22, 
    '愛知県'       : __SHIPPING_AREA_VAL23, 
    '三重県'       : __SHIPPING_AREA_VAL24, 
    '滋賀県'       : __SHIPPING_AREA_VAL25, 
    '京都府'       : __SHIPPING_AREA_VAL26, 
    '大阪府'       : __SHIPPING_AREA_VAL27, 
    '兵庫県'       : __SHIPPING_AREA_VAL28, 
    '奈良県'       : __SHIPPING_AREA_VAL29, 
    '和歌山県'     : __SHIPPING_AREA_VAL30, 
    '鳥取県'       : __SHIPPING_AREA_VAL31, 
    '島根県'       : __SHIPPING_AREA_VAL32, 
    '岡山県'       : __SHIPPING_AREA_VAL33, 
    '広島県'       : __SHIPPING_AREA_VAL34, 
    '山口県'       : __SHIPPING_AREA_VAL35, 
    '徳島県'       : __SHIPPING_AREA_VAL36, 
    '香川県'       : __SHIPPING_AREA_VAL37, 
    '愛媛県'       : __SHIPPING_AREA_VAL38, 
    '高知県'       : __SHIPPING_AREA_VAL39, 
    '福岡県'       : __SHIPPING_AREA_VAL40, 
    '佐賀県'       : __SHIPPING_AREA_VAL41, 
    '長崎県'       : __SHIPPING_AREA_VAL42, 
    '熊本県'       : __SHIPPING_AREA_VAL43, 
    '大分県'       : __SHIPPING_AREA_VAL44, 
    '宮城県'       : __SHIPPING_AREA_VAL45, 
    '鹿児島県'     : __SHIPPING_AREA_VAL46, 
    '沖縄県'       : __SHIPPING_AREA_VAL47, 
    '未定'         : __SHIPPING_AREA_VAL48
    };


    #! 発送までの日数
    SELECT_SHIPPING_DAYS: str = '#main > form > section:nth-child(4) > mer-select:nth-child(4) > div > label > div.mer-select > select';

    #「発送までの日数」に応じた HTMLの value値
    __SHIPPING_DAYS_1: int = 1;
    __SHIPPING_DAYS_2: int = 2;
    __SHIPPING_DAYS_3: int = 3;

    #「発送までの日数」に応じた HTMLの value値を保持
    __dicShippingDays: dict = {
    '1~2日で発送'       : __SHIPPING_DAYS_1, 
    '2~3日で発送'       : __SHIPPING_DAYS_2, 
    '4~7日で発送'       : __SHIPPING_DAYS_3, 
    };


    # 変更する
    #（fix_1 : 2022/04/28）BTN_CHANGED = '#main > form > div.layout__FlexWrapper-sc-1lyi7xi-9.eNrnaj > mer-button:nth-child(1) > button'
    #（fix_2 : 2022/08/02）BTN_CHANGED = '#main > form > div.layout__FlexWrapper-sc-1lyi7xi-9.cQBeFq > mer-button:nth-child(1) > button'
    #（fix_3 : 2022/11/19）BTN_CHANGED = '#main > form > div.layout__FlexWrapper-sc-1lyi7xi-9.cFSybX > mer-button:nth-child(1) > button'
    # (fix_4 : 2023/03/05) BTN_CHANGED: str = '#main > form > div.layout__FlexWrapper-sc-1lyi7xi-9.elfNBA > mer-button:nth-child(1) > button';
    BTN_CHANGED: str = '#main > form > div.sc-faba0f76-9.dAsva-D > mer-button:nth-child(1) > button'


    # 販売価格
    INPUT_STARTING_PRICE: str = '#main > form > section:nth-child(5) > div:nth-child(2) > mer-text-input > div > label > div.mer-text-input-container > input';
    

    # 下書きに保存（※ユーザーの要望）出品までは行わない
    # (fix_1 : 2022/11/02 )BTN_SAVE_TO_DRAFT = '#main > form > div.layout__FlexWrapper-sc-1lyi7xi-9.cFSybX > mer-button:nth-child(2) > button'
    # (fix_1 : 2023/03/05) BTN_SAVE_TO_DRAFT: str = '#main > form > div.layout__FlexWrapper-sc-1lyi7xi-9.elfNBA > mer-button:nth-child(2) > button';
    BTN_SAVE_TO_DRAFT: str = '#main > form > div.sc-faba0f76-9.dAsva-D > mer-button:nth-child(2) > button'


    # 出品画面「出品する」ボタン
    # (fix_1 : 2022/11/02) BTN_EXHIBITING = '#main > section:nth-child(2) > div > a.OldSellerHomeContent__ListItemButton-sc-2xo3fq-0.bbGatD.mer-spacing-r-16'
    BTN_EXHIBITING: str = '#main > section:nth-child(3) > div > mer-button:nth-child(1) > a';



    def getCommodityCondition(self, strCommodityCondition: str) ->  str:
        """
         @detail        「商品の状態」に応じた HTML内の value値を取得
         @param[in]     strCommodityCondition       商品の状態
         @return        nCommodityConditionVal      HTML内の value値
        """

        if not strCommodityCondition in self.__dicProductStatus.keys():
            self.LOG.LogError(f'指定された「商品の状態」種別はありません［種別：{strCommodityCondition}］');
            return str(self.__dicProductStatus[self.__PRODUCT_STATUS_1]);

        return str(self.__dicProductStatus[strCommodityCondition]);



    def getShippingChange(self, strShippingChange) ->  str:
        """
         @detail        「配送料の負担」に応じた HTML内の value値を取得
         @param[in]     strShippingChange       配送料の負担
         @return        nShippingChangeVal      HTML内の value値
        """
        
        if not strShippingChange in self.__dicShippingChange.keys():
            self.LOG.LogError(f'指定された「商品の状態」種別はありません［種別：{strShippingChange}］');
            return str(self.__dicShippingChange[self.__POSTAGE_INCLUDE]);

        return str(self.__dicShippingChange[strShippingChange]);


    
    def getShippingMethodVer01(self, strShippingChargeVal: str, strShippingMethod: str) ->  str:
        """
         @detail        「配送料の負担」種別に応じた「配送の方法」の HTML内の value値を取得
         @param[in]     strShippingChargeVal        配送料の負担（1：着払い、2：送料込み）
         @param[in]     strShippingMethod           配送の方法
         @return        str(self.__dicShippingMethodVer01[strShippingMethod][strShippingChargeVal])      「配送料の負担」種別に応じた「配送の方法」HTML内の value値
        """
        
        if not strShippingChargeVal in self.__dicShippingMethodVer01.keys():
            self.LOG.LogError(f'指定された「配送料の負担」種別はありません［種別：{strShippingChargeVal}］');
            return str(999);


        if not strShippingMethod in self.__dicShippingMethodVer01[strShippingChargeVal].keys():
            self.LOG.LogError(f'指定された「配送の方法」種別はありません［種別：{strShippingMethod}］');
            return str(999);

        
        return str(self.__dicShippingMethodVer01[strShippingChargeVal][strShippingMethod]);
    


    def getShippingMethodVer02(self, strShippingChargeVal: str, strShippingMethod: str) ->  str:
        """
         @detail        「配送料の負担」種別に応じた「配送の方法」の CssSelectorを取得
         @param[in]     strShippingChargeVal        配送料の負担（1：着払い、2：送料込み）
         @param[in]     strShippingMethod           配送の方法
         @return        self.__dicShippingMethodVer02[strShippingMethod][strShippingChargeVal]      「配送料の負担」種別に応じた「配送の方法」CssSelectorCssSelector
        """
        if not strShippingChargeVal in self.__dicShippingMethodVer02.keys():
            self.LOG.LogError(f'指定された「配送料の負担」種別はありません［種別：{strShippingChargeVal}］');
            return str(999);


        if not strShippingMethod in self.__dicShippingMethodVer02[strShippingChargeVal].keys():
            self.LOG.LogError(f'指定された「配送の方法」種別はありません［種別：{strShippingMethod}］');
            return str(999);

        
        return self.__dicShippingMethodVer02[strShippingChargeVal][strShippingMethod];



    def getShippingArea(self, strShippingArea: str) ->  str:
        """
         @detail        「発送元の地域」種別に応じた HTML内の value値を取得
         @param[in]     strShippingArea      発送元の地域
         @return        str(self.__dicShippingArea[strShippingArea])    「発送元の地域」種別に応じた「配送の方法」の value値
        """
        
        if not strShippingArea in self.__dicShippingArea.keys():
            self.LOG.LogError(f'指定された「発送元の地域」種別はありません［種別：{strShippingArea}］');
            return str(self.__dicShippingArea[self.__SHIPPING_AREA_VAL13]);

        return str(self.__dicShippingArea[strShippingArea]);



    def getShippingDays(self, strShippingDays: str) ->  str:
        """
         @detail        「発送までの日数」種別に応じた HTML内の value値を取得
         @param[in]     strShippingDays         発送までの日数
         @return        str(self.__dicShippingDays[strShippingDays])      「発送までの日数」種別に応じた HTML内の value値
        """
        
        if not strShippingDays in self.__dicShippingDays.keys():
            self.LOG.LogError(f'指定された「発送までの日数」種別はありません［種別：{strShippingDays}］');
            return str(self.__dicShippingDays[self.__SHIPPING_DAYS_1]);

        return str(self.__dicShippingDays[strShippingDays]);