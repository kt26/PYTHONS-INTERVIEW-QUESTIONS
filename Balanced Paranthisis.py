def is_paranthisis_balanced(s):
    count_c = 0
    count_s = 0
    count_r = 0

    for i in range(len(s)):
        if (count_c<0 or count_s<0 or count_r<0):
            return "NO"
        if s[i] == "(":
            count_r +=1
            try:
                if s[i+1]== "]" or s[i+1]  == "}":
                    return "NO"
            except:
                pass
        elif s[i] == "{":
            count_c +=1
            try:
                if s[i+1]== "]" or s[i+1]  == ")":
                    return "NO"
            except:
                pass
        elif s[i] == "[":
            count_s +=1
            try:
                if s[i+1]== "}" or s[i+1]  == ")":
                    return "NO"
            except:
                pass
        elif s[i] == "]":
            count_s -=1
        elif s[i] == "}":
            count_c -=1
        elif s[i] == ")":
            count_r -=1

    if (count_c==0 and count_s==0 and count_r==0):
        return "YES"

    return "NO"


s = "[{{[]}()}()[]{()}]"
print(is_paranthisis_balanced(s))
