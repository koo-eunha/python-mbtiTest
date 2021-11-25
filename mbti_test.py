''' Eunha Koo
INF452, Dr. Maher Elshakankiri
Midterm Project: MBTI test
Date created: 2021.10.22 2:25pm
Date last modified: 2021.11.07 9:32pm
'''

# provide instructions to user about the test and prompt user to enter 1 to start the test
start = input("This is the Myers-Briggs Type Indicator test. "
              "\nRead each question carefully and select one of the two choices given, which applies to you,"
              "\nby pressing either 1, 2, or 3, depending on the question."
              "\n\nPress 1 to start the test.\n")
# if user entered something other than 1, keep prompting until they enter 1
while start != '1':
    start = input("Please enter a valid number.\n")
# initialize the variables
if start == '1':
    E = 0
    I = 0
    S = 0
    N = 0
    T = 0
    F = 0
    J = 0
    P = 0
    # provide instructions about part 1
    print("This is part 1 of the test. Choose the option that comes closer"
          "\nto telling how you usually feel or act.\n")
    # store the answer of question 1 into a variable
    q1 = input("Question 1: When you go somewhere for the day, wound you rather"
               "\n\t1) Plan what you will do and when"
               "\n\t2) Just go!!\n")
    # if user entered a number other than 1 or 2, keep prompting until they enter a valid number
    while q1 != '1' and q1 != '2':
        q1 = input("Please enter a valid number.\n")
    # Add the amount of points that should be added to the corresponding variable
    # (points are different for each question and for each variable)
    if q1 == '1':
        J += 2
    elif q1 == '2':
        P += 2

    q2 = input("Question 2: If you were a teacher, would you rather teach"
               "\n\t1) Facts-based courses"
               "\n\t2) Courses involving opinion or theory\n")
    while q2 != '1' and q2 != '2':
        q2 = input("Please enter a valid number.\n")
    if q2 == '1':
        S += 2
    elif q2 == '2':
        N += 2

    q3 = input("Question 3: Are you usually"
               "\n\t1) A \"good mixer\" with groups of people"
               "\n\t2) Rather quiet and reserved\n")
    while q3 != '1' and q3 != '2':
        q3 = input("Please enter a valid number.\n")
    if q3 == '1':
        E += 2
    elif q3 == '2':
        I += 2

    q4 = input("Question 4: Do you more often let"
               "\n\t1) Your heart rule your head"
               "\n\t2) Your head rule your heart\n")
    while q4 != '1' and q4 != '2':
        q4 = input("Please enter a valid number.\n")
    if q4 == '1':
        F += 1
    elif q4 == '2':
        T += 2

    q5 = input("Question 5: In doing something that many other people do, would you rather"
               "\n\t1) Invent a way of your own"
               "\n\t2) Do it in the accepted way\n")
    while q5 != '1' and q5 != '2':
        q5 = input("Please enter a valid number.\n")
    if q5 == '1':
        N += 1
    elif q5 == '2':
        S += 1

    q6 = input("Question 6: Among your friends are you"
               "\n\t1) Full of news about everybody"
               "\n\t2) One of the last to hear what is going on\n")
    while q6 != '1' and q6 != '2':
        q6 = input("Please enter a valid number.\n")
    if q6 == '1':
        E += 2
    elif q6 == '2':
        I += 1

    q7 = input("Question 7: Does the idea of making a list of what you should get done over a weekend"
               "\n\t1) Help you"
               "\n\t2) Stress you"
               "\n\t3) Positively depress you\n")
    while q7 != '1' and q7 != '2' and q7 != '3':
        q7 = input("Please enter a valid number.\n")
    if q7 == '1':
        J += 1
    elif q7 == '2' or q7 == '3':
        P += 1

    q8 = input("Question 8: When you have a special job to do, do you like to"
               "\n\t1) Organize it carefully before you start"
               "\n\t2) Find out what is necessary as you go along\n")
    while q8 != '1' and q8 != '2':
        q8 = input("Please enter a valid number.\n")
    if q8 == '1':
        J += 1
    elif q8 == '2':
        P += 2

    q9 = input("Question 9: Do you tend to have"
               "\n\t1) Broad friendships with many different people"
               "\n\t2) Deep friendship with very few people\n")
    while q9 != '1' and q9 != '2':
        q9 = input("Please enter a valid number.\n")
    if q9 == '1':
        E += 2
    elif q9 == '2':
        I += 1

    q10 = input("Question 10: Do you admire more the people who are"
                "\n\t1) Normal-acting to never make themselves the center of attention"
                "\n\t2) Too original and individual to care whether they are the center of attention or not\n")
    while q10 != '1' and q10 != '2':
        q10 = input("Please enter a valid number.\n")
    if q10 == '1':
        S += 1
    elif q10 == '2':
        N += 2

    q11 = input("Question 11: Do you prefer to"
                "\n\t1) Arrange picnics, parties, etc., well in advance"
                "\n\t2) Be free to do whatever looks like fun when the time comes\n")
    while q11 != '1' and q11 != '2':
        q11 = input("Please enter a valid number.\n")
    if q11 == '1':
        J += 2
    elif q11 == '2':
        P += 1

    q12 = input("Question 12: Do you usually get along better with"
                "\n\t1) Realistic people"
                "\n\t2) Imaginative people\n")
    while q12 != '1' and q12 != '2':
        q12 = input("Please enter a valid number.\n")
    if q12 == '1':
        S += 1
    elif q12 == '2':
        N += 2

    q13 = input("Question 13: When you are with a group of people, would you usually rather"
                "\n\t1) Join in the talk of the group"
                "\n\t2) Stand back and listen first\n")
    while q13 != '1' and q13 != '2':
        q13 = input("Please enter a valid number.\n")
    if q13 == '1':
        E += 1
    elif q13 == '2':
        I += 2

    q14 = input("Question 14: Is it a higher compliment to be called"
                "\n\t1) A person of real feeling"
                "\n\t2) A consistently reasonable person\n")
    while q14 != '1' and q14 != '2':
        q14 = input("Please enter a valid number.\n")
    if q14 == '1':
        F += 1
    elif q14 == '2':
        T += 2

    q15 = input("Question 15: In reading for pleasure, do you"
                "\n\t1) Enjoy odd or original ways of saying things"
                "\n\t2) Like writers to say exactly what they mean\n")
    while q15 != '1' and q15 != '2':
        q15 = input("Please enter a valid number.\n")
    if q15 == '1':
        pass
    elif q15 == '2':
        S += 1

    q16 = input("Question 16: Do you"
                "\n\t1) Talk easily to almost anyone for as long as you have to"
                "\n\t2) Find a lot to say only to certain people or under certain conditions\n")
    while q16 != '1' and q16 != '2':
        q16 = input("Please enter a valid number.\n")
    if q16 == '1':
        E += 2
    elif q16 == '2':
        I += 2

    q17 = input("Question 17: Does following a schedule"
                "\n\t1) Appeal to you"
                "\n\t2) Cramp you\n")
    while q17 != '1' and q17 != '2':
        q17 = input("Please enter a valid number.\n")
    if q17 == '1':
        J += 2
    elif q17 == '2':
        P += 2

    q18 = input("Question 18: When it is settled well in advance that you will do a"
                "\ncertain thing at a certain time, do you find it"
                "\n\t1) Nice to be able to plan accordingly"
                "\n\t2) A little unpleasant to be tied down\n")
    while q18 != '1' and q18 != '2':
        q18 = input("Please enter a valid number.\n")
    if q18 == '1':
        J += 1
    elif q18 == '2':
        P += 1

    q19 = input("Question 19: Are you more successful"
                "\n\t1) At following a carefully worked out plan"
                "\n\t2) At dealing with the unexpected and seeing quickly what should be done\n")
    while q19 != '1' and q19 != '2':
        q19 = input("Please enter a valid number.\n")
    if q19 == '1':
        J += 1
    elif q19 == '2':
        P += 1

    q20 = input("Question 20: Would you rather be considered"
                "\n\t1) A practical person"
                "\n\t2) An out-of-the-box-thinking person\n")
    while q20 != '1' and q20 != '2':
        q20 = input("Please enter a valid number.\n")
    if q20 == '1':
        S += 2
    elif q20 == '2':
        N += 2

    q21 = input("Question 21: In a large group, do you more often"
                "\n\t1) Introduce others"
                "\n\t2) Get introduced\n")
    while q21 != '1' and q21 != '2':
        q21 = input("Please enter a valid number.\n")
    if q21 == '1':
        E += 2
    elif q21 == '2':
        I += 2

    q22 = input("Question 22: Do you usually"
                "\n\t1) Value emotion more than logic"
                "\n\t2) Value logic more than feelings\n")
    while q22 != '1' and q22 != '2':
        q22 = input("Please enter a valid number.\n")
    if q22 == '1':
        F += 2
    elif q22 == '2':
        T += 2

    q23 = input("Question 23: Would you rather have as a friend"
                "\n\t1) Someone who is always coming up with new ideas"
                "\n\t2) Someone who has both feet on the ground\n")
    while q23 != '1' and q23 != '2':
        q23 = input("Please enter a valid number.\n")
    if q23 == '1':
        N += 1
    elif q23 == '2':
        S += 2

    q24 = input("Question 24: Can the new people you meet tell what you are interested in"
                "\n\t1) Right away"
                "\n\t2) Only after they really get to know you\n")
    while q24 != '1' and q24 != '2':
        q24 = input("Please enter a valid number.\n")
    if q24 == '1':
        E += 1
    elif q24 == '2':
        I += 1

    # this question can take multiple answers
    q25 = input("Question 25: (On this question only, if two answers are true,"
                "\nenter both numbers e.g., 12 for 1 and 2, 23 for 2 and 3)"
                "\nIn your daily work, do you"
                "\n\t1) Usually plan your work so you won't need to work under pressure"
                "\n\t2) Rather enjoy an emergency that makes you work against time"
                "\n\t3) Hate to work under pressure\n")
    # this is a list of all possible valid answers
    q25_valid = ['1', '2', '3', '12', '13', '23', '21', '31', '32']
    # if user entered an invalid answer, keep prompting until they enter a valid answer
    while q25 not in q25_valid:
        q25 = input("Please enter a valid number.\n")
    # separate the number from the tens digit and the ones digit
    tens = int(q25) // 10
    ones = int(q25) % 10
    # if the user entered two numbers then tens will not be zero
    # add the points to the corresponding variable
    # some answers do not count as anything, so pass for that one
    if tens != 0:
        if tens == 1:
            J += 1
        elif tens == 2:
            P += 1
        elif tens == 3:
            pass
    # add the points to the corresponding variable
    if ones == 1:
        J += 1
    elif ones == 2:
        P += 1
    elif ones == 3:
        pass

    q26 = input("Question 26: Do you usually"
                "\n\t1) Show your feelings freely"
                "\n\t2) Keep your feelings to yourself\n")
    while q26 != '1' and q26 != '2':
        q26 = input("Please enter a valid number.\n")
    if q26 == '1':
        E += 1
    elif q26 == '2':
        pass

    # provide instructions for the user for part 2
    print("This is part 2 of the test. Choose the word in each pair that appeals to you more."
          "\n(Think what the word means, not how they look or how they sound)\n")
    q27 = input("Question 27:"
                "\n\t1) Scheduled"
                "\n\t2) Unplanned\n")
    while q27 != '1' and q27 != '2':
        q27 = input("Please enter a valid number.\n")
    if q27 == '1':
        J += 2
    elif q27 == '2':
        P += 2

    q28 = input("Question 28:"
                "\n\t1) Facts"
                "\n\t2) Ideas\n")
    while q28 != '1' and q28 != '2':
        q28 = input("Please enter a valid number.\n")
    if q28 == '1':
        S += 2
    elif q28 == '2':
        N += 1

    q29 = input("Question 29:"
                "\n\t1) Quiet"
                "\n\t2) Hearty\n")
    while q29 != '1' and q29 != '2':
        q29 = input("Please enter a valid number.\n")
    if q29 == '1':
        I += 2
    elif q29 == '2':
        E += 2

    q30 = input("Question 30:"
                "\n\t1) Convincing"
                "\n\t2) Touching\n")
    while q30 != '1' and q30 != '2':
        q30 = input("Please enter a valid number.\n")
    if q30 == '1':
        T += 2
    elif q30 == '2':
        F += 1

    q31 = input("Question 31:"
                "\n\t1) Imaginative"
                "\n\t2) Matter-of-fact\n")
    while q31 != '1' and q31 != '2':
        q31 = input("Please enter a valid number.\n")
    if q31 == '1':
        pass
    elif q31 == '2':
        S += 2

    q32 = input("Question 32:"
                "\n\t1) Benefits"
                "\n\t2) Blessings\n")
    while q32 != '1' and q32 != '2':
        q32 = input("Please enter a valid number.\n")
    if q32 == '1':
        T += 1
    elif q32 == '2':
        F += 1

    q33 = input("Question 33:"
                "\n\t1) Peacemaker"
                "\n\t2) Judge\n")
    while q33 != '1' and q33 != '2':
        q33 = input("Please enter a valid number.\n")
    if q33 == '1':
        pass
    elif q33 == '2':
        T += 2

    q34 = input("Question 34:"
                "\n\t1) Systematic"
                "\n\t2) Spontaneous\n")
    while q34 != '1' and q34 != '2':
        q34 = input("Please enter a valid number.\n")
    if q34 == '1':
        J += 2
    elif q34 == '2':
        P += 2

    q35 = input("Question 35:"
                "\n\t1) Statement"
                "\n\t2) Concept\n")
    while q35 != '1' and q35 != '2':
        q35 = input("Please enter a valid number.\n")
    if q35 == '1':
        S += 2
    elif q35 == '2':
        N += 1

    q36 = input("Question 36:"
                "\n\t1) Reserved"
                "\n\t2) Talkative\n")
    while q36 != '1' and q36 != '2':
        q36 = input("Please enter a valid number.\n")
    if q36 == '1':
        I += 1
    elif q36 == '2':
        E += 2

    q37 = input("Question 37:"
                "\n\t1) Analyze"
                "\n\t2) Sympathize\n")
    while q37 != '1' and q37 != '2':
        q37 = input("Please enter a valid number.\n")
    if q37 == '1':
        T += 1
    elif q37 == '2':
        F += 2

    q38 = input("Question 38:"
                "\n\t1) Create"
                "\n\t2) Make\n")
    while q38 != '1' and q38 != '2':
        q38 = input("Please enter a valid number.\n")
    if q38 == '1':
        pass
    elif q38 == '2':
        S += 2

    q39 = input("Question 39:"
                "\n\t1) Determined"
                "\n\t2) Devoted\n")
    while q39 != '1' and q39 != '2':
        q39 = input("Please enter a valid number.\n")
    if q39 == '1':
        T += 1
    elif q39 == '2':
        F += 1

    q40 = input("Question 40:"
                "\n\t1) Gentle"
                "\n\t2) Firm\n")
    while q40 != '1' and q40 != '2':
        q40 = input("Please enter a valid number.\n")
    if q40 == '1':
        F += 1
    elif q40 == '2':
        T += 2

    q41 = input("Question 41:"
                "\n\t1) Systematic"
                "\n\t2) Casual\n")
    while q41 != '1' and q41 != '2':
        q41 = input("Please enter a valid number.\n")
    if q41 == '1':
        J += 2
    elif q41 == '2':
        P += 2

    q42 = input("Question 42:"
                "\n\t1) Certainty"
                "\n\t2) Theory\n")
    while q42 != '1' and q42 != '2':
        q42 = input("Please enter a valid number.\n")
    if q42 == '1':
        S += 1
    elif q42 == '2':
        N += 2

    q43 = input("Question 43:"
                "\n\t1) Calm"
                "\n\t2) Lively\n")
    while q43 != '1' and q43 != '2':
        q43 = input("Please enter a valid number.\n")
    if q43 == '1':
        I += 1
    elif q43 == '2':
        E += 1

    q44 = input("Question 44:"
                "\n\t1) Justice"
                "\n\t2) Mercy\n")
    while q44 != '1' and q44 != '2':
        q44 = input("Please enter a valid number.\n")
    if q44 == '1':
        T += 1
    elif q44 == '2':
        F += 2

    q45 = input("Question 45:"
                "\n\t1) Fascinating"
                "\n\t2) Sensible\n")
    while q45 != '1' and q45 != '2':
        q45 = input("Please enter a valid number.\n")
    if q45 == '1':
        pass
    elif q45 == '2':
        S += 2

    q46 = input("Question 46:"
                "\n\t1) Firm-minded"
                "\n\t2) Warm hearted\n")
    while q46 != '1' and q46 != '2':
        q46 = input("Please enter a valid number.\n")
    if q46 == '1':
        T += 2
    elif q46 == '2':
        pass

    q47 = input("Question 47:"
                "\n\t1) Feeling"
                "\n\t2) Thinking\n")
    while q47 != '1' and q47 != '2':
        q47 = input("Please enter a valid number.\n")
    if q47 == '1':
        F += 1
    elif q47 == '2':
        T += 2

    q48 = input("Question 48:"
                "\n\t1) Literal"
                "\n\t2) Figurative\n")
    while q48 != '1' and q48 != '2':
        q48 = input("Please enter a valid number.\n")
    if q48 == '1':
        S += 1
    elif q48 == '2':
        N += 1

    q49 = input("Question 49:"
                "\n\t1) Anticipation"
                "\n\t2) Compassion\n")
    while q49 != '1' and q49 != '2':
        q49 = input("Please enter a valid number.\n")
    if q49 == '1':
        T += 2
    elif q49 == '2':
        F += 1

    q50 = input("Question 50:"
                "\n\t1) Hard"
                "\n\t2) Soft\n")
    while q50 != '1' and q50 != '2':
        q50 = input("Please enter a valid number.\n")
    if q50 == '1':
        T += 2
    elif q50 == '2':
        pass

    # initialize the result personality
    res = ''
    # compare each of the two variables to find out the dominant traits
    if E > I:
        res += 'E'
    else:
        res += 'I'
    if S > N:
        res += 'S'
    else:
        res += 'N'
    if T > F:
        res += 'T'
    else:
        res += 'F'
    if J > P:
        res += 'J'
    else:
        res += 'P'
    # get the percentage of each of the traits to provide a breakdown for the user
    E_per = round((E / (E + I)) * 100, 2)
    I_per = round((I / (E + I)) * 100, 2)
    S_per = round((S / (S + N)) * 100, 2)
    N_per = round((N / (S + N)) * 100, 2)
    T_per = round((T / (T + F)) * 100, 2)
    F_per = round((F / (T + F)) * 100, 2)
    J_per = round((J / (J + P)) * 100, 2)
    P_per = round((P / (J + P)) * 100, 2)
    # print result and breakdown of each trait percentages, and the source the test is from
    print("Your personality type is", res)
    print("Results Breakdown:\n"
          + str(E_per) + "% Extraverted, " + str(I_per) + "% Introverted\n"
          + str(S_per) + "% Sensing, " + str(N_per) + "% Intuitive\n"
          + str(T_per) + "% Thinking, " + str(F_per) + "% Feeling\n"
          + str(J_per) + "% Judging, " + str(P_per) + "% Perceiving")
    print("\nTest from https://wedgworthleadership.com/wp-content/uploads/2016/08/Myers-Briggs-Personality-Test.pdf")
