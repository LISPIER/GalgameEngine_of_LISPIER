# 提供一个DataReader函数：读取一个存档文件，并返回一个运行时环境


from Define_Character import Character
from Define_Scene import Scene
from Define_Runtime_Env import Runtime_Env


def DataReader(Path):
    DataFile_Line_List=DataReader_Read(Path)
    Current_Runtime_Env=DataReader_Load(DataFile_Line_List)

    return Current_Runtime_Env


def DataReader_Read(Path):  # 和EventParser_Read几乎一样
    DataFile=open(Path,"r")
    DataFile_Line_List=[]
    while True:
        CurrentLine=DataFile.readline()

        if (CurrentLine==""):  # 文件末尾（什么都读不到）处退出
            break
        elif (CurrentLine=="\n"):  # 空行（一个换行符）跳过
            continue

        CurrentLine=CurrentLine.replace("\n","")
        DataFile_Line_List.append(CurrentLine)

    DataFile.close()

    return DataFile_Line_List


def DataReader_Load(Current_Runtime_Env):
    # 这里请谨慎考虑后动笔

    return Current_Runtime_Env  # 存档加载完毕后，返回一个完整的运行时环境，之后转入事件解析之类的东西（主要看main.py怎么写）

