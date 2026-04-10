import oracledb
from person import Person

# 데이터베이스 접속 정보 설정
dsn = oracledb.makedsn("localhost", 1521, service_name="XE")
conn = oracledb.connect(user="c##mbc", password="green1234", dsn=dsn)

# 쿼리 실행을 위한 커서 생성
cursor = conn.cursor()
        
list=[]

def show_menu():  # 메뉴 보여주는 함수
    print('-- 임직원 관리 시스템 --')
    print('-     1. 직원 추가     - ')
    print('-     2. 직원 삭제     - ')
    print('-     3. 직원 조회     - ')
    print('-     4. 직원 수정     - ')
    print('-   5. 프로그램 종료   - ')
    menu_num=input('메뉴를 선택해주세요. ') 
    print(menu_num)
    return menu_num

def insert_emp(): # 직원 추가 함수  empno, ename, job, mgr, hiredate, sal, comm, deptno   
    print('새로운 직원의 사번, 이름을 입력하세요...')
    empno, ename = input().split()
    print(empno,ename)

    if empno.isdigit():  # 사업 입력 시 숫자인지 문자열인지 확인하여 True일 시 INSERT, False일 시 오류 메시지 출력
        # INSERT 예제
        try:
            cursor.execute("INSERT INTO emp (empno, ename) VALUES (:1, :2)", [empno, ename.upper()])
            conn.commit()
            print("Data inserted successfully")
            list.clear()  # 인서트 후 리스트를 클리어 
        except oracledb.DatabaseError as e:
            print(f"Error inserting data {e}")    
    else:
        print('INSERT ERROR. 숫자만 입력 가능합니다.')
    

def del_emp():  # 직원 삭제 함수
    print('삭제할 직원의 사번을 입력하세요...')
    empno=input()
    print(empno)

    if len(list) > 0:
        eq=False
        for i in list:
            # i.print_person()
            if str(i.empno)==empno:
                eq=True
                list.remove(i) #list에서 삭제
        if eq == True:      # 실제 DB에서 데이터 삭제
            print('해당 사번이 존재합니다.')
            try:
                # DELETE FROM EMP WHERE EMPNO='4769'
                cursor.execute("DELETE FROM EMP WHERE EMPNO=:1", [empno])
                conn.commit()

                print("Data deleted successfully")
            except oracledb.DatabaseError as e:
                print(f"Error deleted data: {e}")
        else:
            print('해당 사번이 존재 하지 않습니다.')
    else:
       search_emp()

def search_emp():   # 직원 조회  함수
    #print('FUNCTION CALL, search_emp()')
# SELECT 예제
    try:
        cursor.execute('''
        SELECT EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO
        FROM emp
        ORDER BY EMPNO''')
        for row in cursor:
            p=Person(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        #     p.print_person()
            list.append(p)

        for i in list:
            i.print_person()

    except oracledb.DatabaseError as e:
        print(f"Error fetching data {e}")

def search_emp2():   # 직원 조회  함수
    #print('FUNCTION CALL, search_emp2()')
    for i in list:
        i.print_person()

def update_emp():   # 직원 수정 함수
    print('수정할 직원의 사번을 입력하세요...')
    empno = input().strip()

    print('변경할 이름을 입력하세요...')
    ename = input().strip()

    try:
        cursor.execute("UPDATE emp SET ename = :1 WHERE empno = :2", [ename.upper(), empno])

        conn.commit()

        if cursor.rowcount == 0:
            print("해당 사번이 존재하지 않습니다.")
        else:
            print("Data updated successfully")

    except oracledb.DatabaseError as e:
        print(f"Error updating data {e}")

# 사용자 행동 반복문 
while True:
    select =int(show_menu())
    if select == 1:
        print('1. 직원 추가 메뉴')
        insert_emp()
    elif select == 2:
        print('2. 직원 삭제 메뉴')
        del_emp()
    elif select == 3:
        print('3. 직원 조회 메뉴')
        print('--- LIST SIZE ---',len(list))
        if len(list) == 0:
            search_emp()
        else:
            search_emp2()
    elif select == 4:
        print('4. 직원 수정 메뉴')
        update_emp()
    else:
        print('***프로그램이 종료 됩니다.***')
        break

# 커서 및 커넥션 닫기
cursor.close()
conn.close()