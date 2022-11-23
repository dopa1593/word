import csv,os,random

def add_csv(name, b, n):#csv 추가
  
  data = open_csv(name)

  f = open(name + '.csv', 'a',newline='')
  wr = csv.writer(f)
  if n <= 1 and not b in data:
    wr.writerow(b)
  else:
    for i in b:
      if not i in data:
        wr.writerow(i)
  f.close()

def insert_csv(name, b):#csv 수정
  f = open(name + '.csv', 'w',newline='')
  wr = csv.writer(f)
  for i in b:
    wr.writerow(i)
  f.close()

def open_csv(name):#csv 열기
  f = open(name + '.csv', 'r')
  r = csv.reader(f)
  b = list(r)
  f.close()
  return b

def remove_csv(name, b):#csv파일에서 b 요소만 삭제
  data = open_csv(name)
  for a in b:
    data.remove(a)
  insert_csv(name, data)

def day_word(n):#30개씩 암기, 학습
  n = int(n)
  wrong_answer = []

  data = open_csv('origin')
  today_data = data[(n-1)*30 : (n-1)*30 + 30]

  print("-" * 90)
  for i,a in enumerate(today_data):
    print("{:5d} {:20s} {:20s}".format(i+1,a[0],a[1]))
  print("-" * 90)

  ready=''
  while ready != '시작':
    ready = str(input("테스트할 준비가 되면 '시작'을 입력해주세요 : "))

  os.system('cls')
  count = 0
  random.shuffle(today_data)
  for i,a in enumerate(today_data):
    q = "{:d} {:s} : ".format(i+1,a[1])
    answer = str(input(q))
    if answer == a[0]:
      print("정답!")
      count += 1
    else: 
      print("오답...")
      wrong_answer.append(a)
    print()

  add_csv('wrong_answer', wrong_answer, 30-count)
  print("30개중 {:d}개 맞추었습니다.".format(count))
  print("\n하루암기가 완료되었습니다.")
  print("-" * 90)
  return 0

def random_word():#origin에서 랜덤하게 문제 풀이
  count = 0
  wrong_answer = []

  data = open_csv('origin')
  random.shuffle(data)

  print("-" * 90)

  for i,a in enumerate(data): 
    q = "{:d} {:s} : ".format(i+1,a[1])
    answer = str(input(q))
    if answer == '종료':
      break
    elif answer == a[0]:
      print("정답!\n")
    else:
      print("오답...\n")
      wrong_answer.append(a)
      count += 1

  print("무작위 암기가 종료되었습니다.")
  print("-" * 90)

  add_csv('wrong_answer',wrong_answer,count)
  return

def remind():#틀린문제 풀이, 맞추면 틀린문제 삭제
  count = 0
  good_answer = []

  data = open_csv('wrong_answer')
  if data == []:
    print('틀린문제가 없습니다')
    print("-" * 90)
    return
  random.shuffle(data)

  print("-" * 90)

  for i,a in enumerate(data): 
    q = "{:d} {:s} : ".format(i,a[1])
    answer = str(input(q))
    if answer == '종료':
      break
    elif answer == a[0]:
      print("정답!\n")
      count += 1
      good_answer.append(a)
    else:
      print("오답...\n")

  remove_csv('wrong_answer', good_answer)
  print("틀린문제연습이 종료되었습니다.")
  print("-" * 90)
  return 

def clear():
  data = []
  insert_csv('wrong_answer',data)
  print("정보가 초기화 되었습니다")
  print("-" * 90)


while True:

  a = input("입력 : ")
  if a == '종료':
     break
  elif a == '하루암기':
    a = input("몇일차인가요? : ")
    day_word(a)
  elif a == '무작위암기':
    random_word()
  elif a == '틀린문제연습':
    remind()
  elif a == '초기화':
    a = input("정말 초기화 하시겠습니까? (Y/N)")
    if a == 'y' or 'Y':
      clear()
    else:
      print("취소되었습니다")
  else:
    print("존재하기 않는 명령어")



