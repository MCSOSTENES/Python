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

def find_hack(arr):
    
    hacked = []
    for j in range (0, len(arr)):
        count = 0
        countAB = 0
        countCD = 0
        for i in range (0, len(arr[j][2])):
            if arr[j][2][i] == "A":
                count += 30
                countAB += 1
            elif arr[j][2][i] == "B":
                count += 20
                countAB += 1
            elif arr[j][2][i] == "C":
                count += 10
                countCD += 1
            elif arr[j][2][i] == "D":
                count += 5
                countCD += 1
            if countAB >= 5 and countCD == 0:
                count += 20
            if count > 200:
                count = 200
        if count != arr[j][1]:
            hacked.append(arr[j][0])
    return hacked


print(find_hack(array))