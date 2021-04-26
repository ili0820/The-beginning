participant = ["mislav", "stanko", "mislav", "ana"]
completion  = 		["stanko", "ana", "mislav"]

def solution(participant,completion):
     participant.sort()
     completion.sort()
     for i in range(len(completion)):
          if participant[i] !=  completion[i]:
             return participant[i]

print(solution(participant,completion))

# def solution(participant,completion):
#      for i in range(len(completion)):
#           if completion[i] in participant:
#              del participant[participant.index(completion[i])]
#           else:
#                print("Completion not Found")
#      answer = participant[0]
#      return answer

# import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]