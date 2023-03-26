import logging
import os
import datetime
import Common.Common;

class Log:
    """
     @class     ログクラス
    """
    # 自身のクラスインスタンス
    objLog = None;


    # ロガークラス
    __m_objLogger: logging.Logger;
    

    # ログ出力：呼び出し元のネストの深さ
    NESTING_DEPTH: int = 2;
    
    

    def __new__(cls):
        """
         @details   シングルトン
         @return    Logクラス
        """
        # newされていなければインスタンス生成
        if cls.objLog is None:
            cls.objLog = super().__new__(cls);
        
            ## 固定値設定クラス
            #objSettingFile: Const.SettingFile = Const.SettingFile();

            # 共通設定クラス
            COMMON: Common.Common.Common = Common.Common.Common.staticCommon();
            
            # ログの出力先
            strDateTime = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S');
            strFilePath = os.path.normpath(os.path.join(COMMON.EXE_BASE_FILE_PATH, f'../log/{strDateTime}.log'));

            # ロガーの設定
            cls.__m_objLogger = logging.getLogger(__name__);
            cls.__m_objLogger.setLevel(logging.DEBUG);

            Handler = logging.FileHandler(strFilePath, encoding='utf-8');
            Handler.setLevel(logging.DEBUG);

            Fomatter = logging.Formatter('%(asctime)s - [%(levelname)s] : %(message)s [ファイル名=%(filename)s / 関数名=%(funcName)s 行=%(lineno)s]');
            Handler.setFormatter(Fomatter);

            cls.__m_objLogger.addHandler(Handler);
            
        return cls.objLog;
    

    
    @classmethod
    def LogDebug(cls, strLog: str)      ->  None:
        """
         @details       ログ出力 (#!debug)
         @param[in]     strLog      出力ログ情報
        """
        cls.__m_objLogger.debug(f'{strLog}', stacklevel=cls.NESTING_DEPTH);
        print(f'[debug]：{strLog}');
    
        
    @classmethod
    def LogInfo(cls, strLog: str)       ->  None:
        """
         @details       ログ出力 (#!info)
         @param[in]     strLog      出力ログ情報
        """
        cls.__m_objLogger.info(f'{strLog}', stacklevel=cls.NESTING_DEPTH);
        print(f'[info]：{strLog}');
        

    @classmethod
    def LogWarning(cls, strLog: str)    ->  None:
        """
         @details       ログ出力 (#!warning)
         @param[in]     strLog      出力ログ情報
        """
        cls.__m_objLogger.warning(f'{strLog}', stacklevel=cls.NESTING_DEPTH);
        print(f'[warning]：{strLog}');
        

    @classmethod
    def LogError(cls, strLog: str)      ->  None:
        """
         @details       ログ出力 (#!error)
         @param[in]     strLog      出力ログ情報
        """
        cls.__m_objLogger.error(f'{strLog}', stacklevel=cls.NESTING_DEPTH);
        print(f'[error]：{strLog}');
        

    @classmethod
    def LogCritical(cls, strLog: str)   ->  None:
        """
         @details       ログ出力 (#!critical)
         @param[in]     strLog      出力ログ情報
        """
        cls.__m_objLogger.critical(f'{strLog}', stacklevel=cls.NESTING_DEPTH);
        print(f'[critical]：{strLog}');
        
    

    #! __new__の return cls.objLogの際に都度コールされるので、インスタンス生成時の 1度のみ実行する __new__の中に移動
    # def __init__(self):
    #     """
    #      @details   コンストラクタ
    #     """
    #     # ログの出力先
    #     strDateTime = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S');
    #     strFilePath = os.path.normpath(os.path.join(self.baseFilePath, f'../log/{strDateTime}.log'));

    #     # ロギングクラスの設定
    #     self.objLogger = logging.getLogger(__name__);
    #     self.objLogger.setLevel(logging.DEBUG);

    #     Handler = logging.FileHandler(strFilePath);
    #     Handler.setLevel(logging.DEBUG);

    #     Fomatter = logging.Formatter('%(asctime)s - [%(levelname)s] : %(message)s [ファイル名=%(filename)s / 関数名=%(funcName)s 行=%(lineno)s]');
    #     Handler.setFormatter(Fomatter);

    #     self.objLogger.addHandler(Handler);