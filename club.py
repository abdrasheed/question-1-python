def sd(s):
    arr1 = []
    arr2 = []
    eq1 = []
    eq2 = []
    for i in s:
        arr1.append(ord(i))
    for i in reversed(arr1):
        arr2.append(i)

    count1 = 0
    while count1 < len(arr1)-1:
        m = arr1[count1] - (arr1[count1+1])
        if m < 0:
            m = m*-1
            eq1.append(m)
        else:
            eq1.append(m)
        count1 +=1

    count2 = 0
    while count2 < len(arr2)-1:
        m = arr2[count2] - (arr2[count2+1])
        if m < 0:
            m = m * -1
            eq2.append(m)
        else:
            eq2.append(m)
        count2 +=1
    print (arr1)
    print (arr2)
    print (eq1)
    print (eq2)
    count = 0
    while count < len(eq1):
        if eq1[count] == eq2[count]:
            if count == len(eq1)-1:
                return 'cool'
        else:
            return 'not cool'
            break
        count += 1
