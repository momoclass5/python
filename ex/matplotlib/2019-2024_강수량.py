'''
2019-12,108,22.6
    그래프만들고 축 초기화
2020-12,108,4.6
    그래프 만들고 축 초기화
2021-12,108,7.9
    그래프 만들고 축 초기화
2022-12,108,13.6
    그래프 만들고 축 초기화
2023-12,108,85.9
    그래프 만들고 축 초기화
'''
'''
    1. 파일의 내용을 csv파일에 담아 오기
'''
try : 
    f = open('ex/matplotlib/2019-2024_강수량.csv', 'r', encoding='utf-8')
except FileNotFoundError:
    print('No such file or directory')
else :    
    import csv
    csvfile = csv.reader(f, delimiter=',') # 한줄씩 읽어서 ,로 구분하여 리스트로 저장
    header = next(csvfile) # 제목 읽어오기

    # ================================================
    # 그래프를 출력 하기 위해 임포트및 한글 처리
    # 한글깨짐 해결
    # 맷플롭에서 사용하는 폰트를 한글폰트로 변경
    from matplotlib import font_manager, rc, pyplot as plt
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
    import csv
    # ================================================

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    # 축의 데이터를 리스트로 생성
    x=[]
    y=[]
    years=[]
    for line in csvfile :
        yyyy, mm = line[0].split('-')
        
        # 한줄씩 읽어서 x, y 리스트에 값을 추가
        x.append(mm)
        y.append(float(line[2]))
        
        # 년도별로 새로운 선 그래프를 만들고 싶어
        # 만약 월이 12라면
        # '2023-08'
        
        if mm == '12' : 
            # 콘솔에 축 데이터(x, y)를 출력 -> 그래프를 출력하고
            # 축 데이터를 초기화
            print(yyyy, "="*20)
            print(x)
            print(y)
            
            years.append(yyyy)  # 그래프 하나에 범례 하나
            plt.plot(x, y, marker='x', color=colors.pop())   # 그래프 추가

            # 그래프를 출력 하면 축의 데이터를 초기화 하여 새로운 그래프를 만들수 있도록 한다
            x=[]
            y=[]
        
    plt.title('선그래프')     # 타이틀
    plt.xlabel('x축')    # x축 이름
    plt.ylabel('y축')    # y축 이름
    plt.legend(years)    # 범례

    plt.show()
finally : 
    # f라는 이름의 지역변수가 존재 하는지 확인
    if 'f' in locals() and not f.closed :
        f.close()
        print('파일닫음')

print('프로그램 종료')