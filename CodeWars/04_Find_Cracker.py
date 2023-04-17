"""
https://www.codewars.com/kata/59f70440bee845599c000085/train/python

Someone was hacking the score. Each student's record is given as an array The objects in the array are given again as an array of scores for each name and total score. ex

array = [
["name1", 445, ["B", "A", "A", "C", "A", "A"]],
["name2", 140, ["B", "A", "A", "A"]],
["name3", 200, ["B", "A", "A", "C"]]
]
The scores for each grade is:

A: 30 points
B: 20 points
C: 10 points
D: 5 points
Everything else: 0 points
If there are 5 or more courses and all courses has a grade of B or above, additional 20 points are awarded. After all the calculations, the total score should be capped at 200 points.

Returns the name of the hacked name as an array when scoring with this rule.

array = [
["name1", 445, ["B", "A", "A", "C", "A", "A"]], # name1 total point is over 200 => hacked
["name2", 110, ["B", "A", "A", "A"]], #  name2 point is right
["name3", 200, ["B", "A", "A", "C"]] # name3 point is 200 but real point is 90 => hacked
];

return ["name1", "name3"]

"""
array = [
    ["name1", 150, ["B", "A", "A", "C", "A", "A"]],
    ["name2", 120, ["B", "A", "A", "A"]],
    ["name3", 160, ["B", "A", "A", "A","A"]],
    ["name4", 140, ["B", "A", "A", "C", "A"]]
]

#My solution
def find_hack1(arr):
    hacked = []
    for j in range (0, len(arr)):
        count = 0
        for i in range (0, len(arr[j][2])):
            if arr[j][2][i] == "A": count += 30
            elif arr[j][2][i] == "B": count += 20
            elif arr[j][2][i] == "C": count += 10
            elif arr[j][2][i] == "D": count += 5
                
        if len(arr[j][2]) > 4 and all(x in {"A","B"} for x in arr[j][2]):
            count += 20
        if count > 200:
            count = 200
        if count != int(arr[j][1]):
            hacked.append(arr[j][0])
    return hacked

#Best pratices
PTS       = {'A':30, 'B':20, 'C':10, 'D':5}
MAX_PTS   = 200
HAS_BONUS = set('AB')
BONUS_PTS = 20

def find_hack(arr):
    # pegar o nome de [name,pts,card] do arr, se pts forem diferente do minino entre 200 e a soma dos pontos 
    return [name for name,pts,card in arr if pts != min( MAX_PTS, 
    #soma os pontos do dic. PTS get retorna 0 se nao tiver a letra no dic.                                  
            sum(PTS.get(n,0) for n in card) + 
                    #verifica de tem bonus o operador <= é utilizado para verificar* se um conjunto é um subconjunto (ou subconjunto próprio) de outro conjunto.
                    BONUS_PTS * (len(card)>4 and set(card)<=HAS_BONUS) )]

"""
*
Por exemplo, se card for ["A", "B", "C"] e HAS_BONUS for {"A", "B", "C", "D"}, a expressão set(card) <= HAS_BONUS será avaliada como True, já que o conjunto {"A", "B", "C"} é um subconjunto próprio do conjunto {"A", "B", "C", "D}".

Já se card for ["A", "B", "C", "D", "E"] e HAS_BONUS for {"A", "B", "C", "D"}, a expressão set(card) <= HAS_BONUS será avaliada como False, já que o conjunto {"A", "B", "C", "D", "E"} não é um subconjunto (ou subconjunto próprio) do conjunto {"A", "B", "C", "D}".

"""


print(find_hack(array))