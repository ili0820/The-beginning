#problem: https://programmers.co.kr/learn/courses/30/lessons/42576

participant = ["mislav", "stanko", "mislav", "ana"]
completion  = 		["stanko", "ana", "mislav"]

def solution(participant,completion):
     participant.sort()
     completion.sort()
     for i in range(len(completion)):
          if participant[i] !=  completion[i]:
             return participant[i]

print(solution(participant,completion))


################################################################################################
# def solution(participant,completion):
#      for i in range(len(completion)):
#           if completion[i] in participant:
#              del participant[participant.index(completion[i])]
#           else:
#                print("Completion not Found")
#      answer = participant[0]
#      return answer
################################################################################################
# Sort 를 쓰지 않고 그냥 일일이 completion 리스트의 요소들을 participant에서 찾아서 제거 하고 
# answer를 return 하도록 하였다, 그랬더니 효율성 테스트를 통과 하지 못하였다. 하지만 결과는 잘 나왔다.



#################################################################################################
# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
#################################################################################################
#다른 사람들의 코드를 보니 collections 라는 모듈을 사용 하였고 , 그안의 Counter객체를 사용 하였는데 정확하게
#어떤 객체들이 있는지 그 용도가 어떤 지는 모르겠다. 
#찾아보니   
# lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee'] 를 
# collections.Counter(lst)
# Counter({'aa': 2, 'cc': 1, 'dd': 1, 'bb': 1, 'ee': 1})
# 이렇게 딕셔너리 형태로 만들어 세어 주고, 이때 Counter는 산술 집합 연산이 가능 하여
# +,-  & | 을 사용 할 수 있다고 한다.
# 출처: https://excelsior-cjh.tistory.com/94 [EXCELSIOR]
##################################################################################################