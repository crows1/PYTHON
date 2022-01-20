import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import* #tkinter의 모든걸 쓰겟다
from tkinter import filedialog

root = Tk() 
root.title("물품 검색")  #타이틀
root.geometry("640x480")

def create_new_file():
    print("새 파일을 만듭니다") #File에 new file 눌렀을시
    
menu = Menu(root)
#File메뉴

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="새 파일",command = create_new_file)   #File 눌렀을시 안에 속성값
menu_file.add_command(label="새 Window")                           #File 눌렀을시 안에 속성값
menu_file.add_separator()                                           #줄자,구분자
menu_file.add_command(label="파일 열기...")                         #File 눌렀을시 안에 속성값
menu_file.add_command(label="폴더 열기") 

menu_file.add_separator()
menu_file.add_command(label="저장")
menu_file.add_command(label="모두 저장",state="disable") #disable 속성이있슴 비활성화뜻 
menu_file.add_command(label="다른 이름으로 저장하기")
                      
menu_file.add_separator()
menu_file.add_command(label="종료후 저장",command=root.quit)
menu_file.add_command(label="종료(Exit)",command=root.quit)

menu.add_cascade(label= "파일",menu=menu_file)  #최상단 File메뉴창

#Edit
 
menu_Edit = Menu(menu, tearoff=0)

menu_Edit.add_command(label="실행 취소")
menu_Edit.add_command(label="다시 실행")
menu_Edit.add_separator()

menu_Edit.add_command(label="복사")
menu_Edit.add_command(label="붙여넣기")
menu_Edit.add_command(label="잘라내기")

menu_Edit.add_separator()
menu_Edit.add_command(label="찾기")
menu_Edit.add_command(label="바꾸기")

menu.add_cascade(label="편집",menu=menu_Edit)

#보기

menu_view = Menu(menu, tearoff=0)
menu_view.add_command(label="화면 글꼴")
menu_view.add_command(label="프린트 글꼴")
menu_view.add_separator()
menu_view.add_command(label="JAVA")
menu_view.add_command(label="PYHOTN")
menu_view.add_separator()
menu_view.add_command(label="기본값")
menu.add_cascade(label="보기",menu=menu_view) 
#윈도우메뉴
                          
menu_win = Menu(menu, tearoff=0)

menu_win.add_command(label="화면색 설정")
menu_win.add_command(label="화면 비율설정")
menu_win.add_separator()
menu_win.add_command(label="전체 화면")
menu_win.add_command(label="창모드")
menu_win.add_separator()
menu_win.add_command(label="우측 반 화면")
menu_win.add_command(label="좌측 반 화면")

menu.add_cascade(label="Window",menu=menu_win)

#도구
menu_pck = Menu(menu,tearoff=0)
menu_pck.add_checkbutton(label="도구 설정 체크") #쇼미니맵 선택시 체크댐
menu_pck.add_separator()
menu_pck.add_command(label="기본 설정")
menu_pck.add_command(label="설정 초기화")
menu_pck.add_separator()
menu_pck.add_command(label="사용자 도구")
menu_pck.add_command(label="사용자 도구 그룹")
menu.add_cascade(label="도구",menu=menu_pck)

#도움말
menu_help = Menu(menu,tearoff=0)
menu_help.add_command(label="설명서")
menu_help.add_command(label="모든 단축키")
menu_help.add_separator()
menu_help.add_command(label="도움말")
menu_help.add_command(label="키보드 맵")
menu_help.add_separator()
menu_help.add_command(label="등록 코드변경")
menu_help.add_command(label="제품지원")
menu_help.add_command(label="최신 버전 확인")
menu_help.add_separator()
menu_help.add_command(label="정보")
menu.add_cascade(label="도움말",menu=menu_help)
#인쇄

menu_pr = Menu(menu,tearoff=0)
menu_pr.add_command(label="인쇄하기")
menu_pr.add_command(label="인쇄 미리보기")
menu_pr.add_command(label="모두 인쇄하기")
menu_pr.add_separator()
menu_pr.add_command(label="인쇄 기타")
menu_pr.add_command(label="인쇄 설정")

menu.add_cascade(label="인쇄",menu=menu_pr)

# frame을 왼쪽에 한줄 얇게 넣고 이미지 라벨버튼하려는데 안대서 이건 찾아도 안보인다...
# 설정 지정이 안대나?
# lf = LabelFrame(root, text="음료")
# lf.grid(row=1,column=1)
# lf(side = "right",fill="both",expand=True) 
#create left Right


#list프레임
    
list_frame = Frame(root)
list_frame.pack(fill="both",padx=7,pady=7)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right",fill="y")

list_file = Listbox(list_frame,selectmode="extended",height=24,yscrollcomman=scrollbar.set)
list_file.pack(side="left",fill="both",expand=True)
scrollbar.config(command=list_file.yview)

#저장경로Frame
path_frame= LabelFrame(root,text="물품검색창")
path_frame.pack(fill="x",padx=7,pady=7,ipady=7)

txt_dest_path= Entry(path_frame)#저장경로르 text쳐서찾기
txt_dest_path.pack(side="left",fill="x",expand=True,padx=5,pady=5,ipady=4)#높이변경

btn_dest_path = Button(path_frame,text="찾아보기",width=10)
btn_dest_path.pack(side="right",padx=5,pady=5)

root.config(menu=menu,bg="skyblue")
root.resizable(False,False)#창크기 변경 불가
root.mainloop()

