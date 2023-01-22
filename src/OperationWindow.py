from typing import List
import tkinter
import tkinter.ttk as ttk
from selenium.webdriver.edge.webdriver import WebDriver
from enum import Enum
import Log
import Const
import ExecuteFunction
import UserInfo



class OperatKind(Enum):
    """
     @details       操作項目
    """
    GetGata     = 'データ取得';     # データ取得
    PriceCut    = '値下げ';         # 値下げ
    Exhibit     = '出品';           # 出品
    Other       = 'その他';         # その他
    
    

class OperationWindow:
    """
     @class     機能選択画面(GUI) 
    """ 
    # ログクラス
    m_objLog: Log.Log = Log.Log();

    
    # 設定ファイル名
    objSettingFile: Const.SettingFile = Const.SettingFile();
    
    # 各機能実行関数群
    objExecuteFunction: ExecuteFunction.ExecuteFunction;
    
    
    # ウィンドウオブジェクト
    guiWindow           : tkinter.Tk            = tkinter.Tk();
    # プルダウンリスト
    strOpeartElement    : tkinter.StringVar     = tkinter.StringVar();
    # ラベルオブジェクト
    label               : tkinter.Label         = tkinter.Label();
    # ラベルテキスト
    strLabelText        : tkinter.StringVar     = tkinter.StringVar();
    
    
    
    def __init__(self, objWebDriver: WebDriver, objUserInfo: UserInfo.UserInfo):
        """
         @details       コンストラクタ
         @param[in]     WebDriver               WebDriver
         @param[in]     objUserInfo             ユーザー情報
        """
        self.objExecuteFunction = ExecuteFunction.ExecuteFunction(objWebDriver);        # 各機能実行クラスのインスタンス生成
        self.objExecuteFunction.loginMercari(objUserInfo)                               # メルカリログイン
                
    
    
    
    # """""""""""""""""""""""""""""""""""GUI更新 bind関数"""""""""""""""""""""""""""""""""""
    
    def ExeOperatKind(self, event):
        """
        @details        選択項目の実行
        @param[in]      event   イベント
        """
        # 選択された機能項目
        strOpeartElement: str = self.strOpeartElement.get();
        
        self.m_objLog.LogInfo('/////////////////////////////////////////////');
        self.m_objLog.LogInfo(f'【{strOpeartElement}】の操作を開始します');
        self.m_objLog.LogInfo('/////////////////////////////////////////////');
        
        # ラベル更新
        self.strLabelText.set(f'【{strOpeartElement}】 実行中...');
        self.label.update();
        
        try:
            # データ取得
            if strOpeartElement == OperatKind.GetGata.value:
                self.objExecuteFunction.getExhibitingList();
                
            # 値下げ
            elif strOpeartElement == OperatKind.PriceCut.value:
                self.objExecuteFunction.exePriceCut();
                
            # 出品
            elif strOpeartElement == OperatKind.Exhibit.value:
                self.objExecuteFunction.exeExhibit();
                
                
            # 選択項目の完了表示（ラベル）
            self.strLabelText.set(f'{strOpeartElement}が完了しました')
            
            self.m_objLog.LogInfo('==========================================');
            self.m_objLog.LogInfo(f'【{strOpeartElement}】の操作が完了しました');
            self.m_objLog.LogInfo('==========================================');
                
                
        except Exception as e:
            self.m_objLog.LogError(f'【{strOpeartElement}】の処理中にエラーが発生しました');    
            self.strLabelText.set(f'エラーが発生しました。再度実行して下さい。');
            self.label.update();
            


    def SelectComboBox(self, event):
        """
        @details        操作項目の選択値をラベルへ反映
        @param[in]      event   イベント
        """
        # 選択された機能項目
        strOpeartElement: str = self.strOpeartElement.get();
        
        # 選択項目の表示（ラベル）
        self.strLabelText.set(f'選択項目：{strOpeartElement}');
        self.label.update();
            
    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    
        
    def guiOperatKind(self) ->  None:
        """
        @details        GUIウィンドウの表示
        """    
        # 操作画面表示
        lstOpeartElement: List = []
        lstOpeartElement.append(OperatKind.GetGata.value);      # データ取得
        lstOpeartElement.append(OperatKind.PriceCut.value);     # 値下げ
        lstOpeartElement.append(OperatKind.Exhibit.value);      # 出品
        
        # GUIウィンドウの作成
        self.guiWindow.title('コントロール画面');
        #（横 × 高さ + x座標 + y座標）
        self.guiWindow.geometry('600x400+500+500');
        
        # フレームの作成
        nFrameWidth = 550;
        nFrameHeight = 375;
        guiFrame = tkinter.Frame(self.guiWindow, width=nFrameWidth, height=nFrameHeight, background='#808080');
        guiFrame.place(x=(600-nFrameWidth)/2, y=(400-nFrameHeight)/2);
        
        # コンボボックス
        nComboBoxWidth = 200;
        combobox = ttk.Combobox(guiFrame, width=20, height=2, state="readonly", textvariable=self.strOpeartElement, values=lstOpeartElement);
        combobox.place(width=nComboBoxWidth, x=(nFrameWidth-nComboBoxWidth)/2, rely=0.1);
        
        # 選択ボタン
        nButtonWidth = 200;
        selectButton = tkinter.Button(guiFrame, text='選択', width=20, height=4);
        selectButton.bind('<ButtonPress>', self.SelectComboBox);
        selectButton.place(width=nButtonWidth, x=(nFrameWidth-nButtonWidth)/2, rely=0.3);
        
        # ラベル
        self.strLabelText.set('項目を選択してください');
        self.label = tkinter.Label(guiFrame, text=self.strLabelText.get(), textvariable=self.strLabelText, background='#000', foreground='#FFF');
        self.label.place(width=nButtonWidth, x=(nFrameWidth-nButtonWidth)/2, rely=0.55);
        
        # 実行ボタン
        executeButton = tkinter.Button(guiFrame, text='実行', width=20, height=4);
        executeButton.bind('<ButtonPress>', self.ExeOperatKind);
        executeButton.place(width=nButtonWidth, x=(nFrameWidth-nButtonWidth)/2, rely=0.65);
            
        self.guiWindow.mainloop();