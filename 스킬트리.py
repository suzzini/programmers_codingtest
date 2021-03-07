def solution(skill, skill_trees):
    for i in range(len(skill_trees)):
        for j in skill_trees[i]:
            if j not in skill:
                skill_trees[i] = skill_trees[i].replace(j, "")

    answer = 0
    for i in range(len(skill_trees)):  # i=0,1,2,3
        count = 0
        for j in range(len(skill_trees[i])):  # i=0, j=0,1,2
            if skill_trees[i][j] == skill[j]:
                count += 1
        if count == len(skill_trees[i]):
            answer += 1

    return answer