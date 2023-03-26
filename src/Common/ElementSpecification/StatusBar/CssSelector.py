from __future__ import annotations
import os
import sys



class CssSelector:
    """
     @class     「ステータスバー」の CSSSelector定義クラス
    """
    @classmethod
    def staticCssSelector(cls) ->  CssSelector:
        """
         @brief     static関数
         @return    CssSelector
        """
        return cls()
    
    
    # ログイン
    # (fix_1 : 2023/03/07) BTN_LOGIN: str = '#gatsby-focus-wrapper > div > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-navigation-top-menu-item:nth-child(2) > span';
    BTN_LOGIN: str = '#__next > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-navigation-top-menu-item:nth-child(2) > span';


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


    # アカウント
    # (fix_1 : 2023/03/05) BTN_ACCOUNT: str = '#gatsby-focus-wrapper > div > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-menu > mer-navigation-top-menu-item > span';
    BTN_ACCOUNT: str = '#__next > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-menu > mer-navigation-top-menu-item > span';
    
    
    # 出品した商品
    # (fix_1 : 2023/03/05) BTN_LISTED_ITEM: str = '#gatsby-focus-wrapper > div > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-menu > div > mer-list > mer-list-item:nth-child(4) > a';
    # (fix_2 : 2023/03/25) BTN_LISTED_ITEM: str = '#__next > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-menu > div > mer-list > mer-list-item:nth-child(4) > a';
    BTN_LISTED_ITEM: str = '#__next > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-menu > div > div > mer-list-item:nth-child(4) > a';


    # 出品
    # (fix_1 : 2023/03/05) BTN_EXHIBIT: str = '#gatsby-focus-wrapper > div > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-button > a';
    BTN_EXHIBIT: str = '#__next > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-button > a';