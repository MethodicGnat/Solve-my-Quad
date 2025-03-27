#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Analeigh Nwokolo 11/27/2023

Solve my Quad was an ambitious project that many have questioned me doing
for it's complexity and size; however, I was still able to code a vision, which
was very exciting for me. This program is designed to solve quadratic equations
like how a student would. Using tkinter wasn't too difficult due to prior 
knowledge and looking through lessons from with Geeks for Geeks,
and I also improved the way I walk through my code. My biggest challenge
throughout the project was to perfect the new sqrt function I made, because
I knew how simplify a radical on paper, but translating that into computer
language took a few tries. What surprised me is it took 3 versions of my
code to get a bug-free program. The first version was a rushed version, for the
second version I started with purpose until I realized the program needs to be more user
friendly and compatible, and the final version is one that respects the
user's experience and tries to enhance the learning of quadratic equations
with increased steps so math content is easier to digest. I learned 
that for functions, if there are functions below a top function and the top 
function is called at the end of the code, the program will run regardless of 
the order. I also expanded my knowledge on dictionaries and list, as for 
this project it was important to have lists of numbers, store them, manipulate, 
and check them. Dictionaries are actually very useful when it comes to looking 
for values within a nested data structure. Boolean values also prove to be 
important in many scenarios, especially when I was creating the Completing the 
Square function as I was making it compatible for fractions. If I had more time to
work on this project, I would have worked on a equation converter that would convert one equation into
the other two quadratic equation formats (vertex form, factored form). I was really proud
of making fractions work for completing the square, and I was really proud of making the box method
work for factoring. Overall, the satisfying creation of this program even taught me how to improve
the way I look at quadratic equations and code.
'''

# keep in mind that program at the moment is only meant for integer input

from tkinter import *
from random import randint
import math, os



def passSys():
    '''
    is a login screen for user. Uses createAccount() and enterAccount() mainly to create windows for user
    
    returns either createAccount or enterAccount, which then sends you to the main window
    '''
    def delAcc():
        '''
        deletes account file
        
        deletes the account file 'pass'
        '''
        return os.remove('pass.txt')
    
        
    def Evaluate():
        '''
        sees if account username and password is appropriate with given requirements
        
        either returns an ErrorMsg to be put on window or creates a file for account info
        '''
        user_name_retrieval = E1.get()
        user_len = len(user_name_retrieval)
        pass_retrieval = E2.get()
        pass_len = len(pass_retrieval)
        if (user_len < 1 or not user_name_retrieval.isalnum()) or (pass_len < 8 or not pass_retrieval.isalnum()):
            ErrorMsg = "Username and password can't contain symbols.\nPassword length must be greater than or equal to 8"
            return ErrorMsg # Error message that will be formatted on to Window in createAccount()
        else:
            with open('pass.txt', 'w') as file:
                # make a file with pass and user on different lines
                file.writelines([f'username:{user_name_retrieval}\n', f'pass:{pass_retrieval}']) 
                
                
    def createAccount():
        '''
        Window for creating an account
        
        creates an account and moves onto sign-in
        '''
        WINDOW = Tk()
        WINDOW.title('Solve my Quad Sign-up')
        WINDOW.geometry('325x200')
        WINDOW.resizable(False, False) # cannot be resized

        Header = Label(WINDOW, font = ('Times', 18), text = "Create Account")
        Header.grid(row=0, column=0)

        user_name = Label(WINDOW, font = ('Helvetica', 14), text = 'Username')
        passcode = Label(WINDOW, font = ('Helvetica', 14), text = 'Passcode')
        global E1 # so it can be used for Evaluate()
        E1 = Entry(WINDOW, width = 13, font = ('Helvetica', 14)) # username
        global E2
        E2 = Entry(WINDOW, width = 13, font = ('Helvetica', 14), show = '*') # password
        
        # if Evaluate returns ErrorMsg, don't continue, else, continue
        ENTER = Button(WINDOW, width = 8, text = 'Enter',
                       command = lambda: [Evaluate(),
                       [[WINDOW.destroy(), enterAccount()] if type(Evaluate()) != str else Label(
                       WINDOW,
                       fg = 'red',
                       font = ('Arial', 7),
                       text = Evaluate(),
                       justify = LEFT).grid(row=3, column = 0, padx = 5, pady = 0, columnspan=2, sticky=W)]])

        user_name.grid(row=1, column=0, padx = 5, pady = 10)
        E1.grid(row=1, column=1, padx = 0, pady = 10)

        passcode.grid(row=2, column=0, padx = 5, pady = 10)
        E2.grid(row=2, column=1, padx = 0, pady = 10)

        ENTER.grid(row=3, column=1, sticky = S + E)

        WINDOW.mainloop() # this is used for all Windows to detect for user initiated events
        
        
    def enterAccount():
        '''
        makes a window for user to enter input
        
        returns either an errormsg telling the user to try again or sends to startUpWin
        '''
        with open('pass.txt', 'r') as file: # looks through file and figures out user and pass
            data = file.read()
            acc_info = data.split('\n')
            user_start = acc_info[0].index(':') + 1 # not including the semicolon, every after is important
            pass_start = acc_info[1].index(':') + 1
            user_info = acc_info[0][user_start:]
            pass_info = acc_info[1][pass_start:]            
            
        WINDOW = Tk()
        WINDOW.title('Solve my Quad Sign-in')
        WINDOW.geometry('275x200')
        WINDOW.resizable(False, False) # cannot be resized

        Header = Label(WINDOW, font = ('Times', 18), text = "Sign-in", justify = LEFT)
        Header.grid(row=0, column=0, sticky = W)

        user_name = Label(WINDOW, font = ('Helvetica', 14), text = 'Username')
        passcode = Label(WINDOW, font = ('Helvetica', 14), text = 'Passcode')
        E1 = Entry(WINDOW, width = 13, font = ('Helvetica', 14)) # username
        E2 = Entry(WINDOW, width = 13, font = ('Helvetica', 14), show = '*') # password
        
        ErrorMsg = 'Username/password is not correct.'
        
        # if user failed to enter account info correctly once, button shows up and if pressed deletes account to make
        # a new one
        newAcc = Button(WINDOW, text = 'Create New Account?', command = lambda: [WINDOW.destroy(), delAcc(), createAccount()])
        
        # if incorrect one, prompt user to create a new account and say information is wrong, else start program
        ENTER = Button(WINDOW, width = 8, text = 'Enter',
                       command = lambda: [[newAcc.grid(row=4, column=1, columnspan=2, sticky=E), Label(
                                 WINDOW,
                                 fg = 'red', font = ('Arial', 8),
                                 text = ErrorMsg,
                                 justify = LEFT).grid(row=3, column=0,
                                 padx=5,
                                 pady=0,
                                 columnspan=2,
                                 sticky = W)] if E1.get() != user_info or E2.get() != pass_info else [WINDOW.destroy(), startUpWin()]])

        user_name.grid(row=1, column=0, padx = 5, pady = 10)
        E1.grid(row=1, column=1, padx = 0, pady = 10)

        passcode.grid(row=2, column=0, padx = 5, pady = 10)
        E2.grid(row=2, column=1, padx = 0, pady = 10)

        ENTER.grid(row=3, column=1, sticky = S + E)
        
        WINDOW.mainloop() 
    
    try: # if there is no account, create one
        open('pass.txt', 'x')
        # create account
        createAccount() # returns a sign-up screen
    except FileExistsError: # if there is an account, sign in
        enterAccount() # returns a sign-in screen
    except Exception as ex: # if there is an error, explain it.
        print(ex) # returns a possible exception.
        
    
def startUpWin():
    '''
    main window, a hub for all other access points 
    
    returns either solutionCalc, infiniteCalc, or signs out based on which button is pressed
    '''
    WINDOW = Tk()
    WINDOW.title("Solve my Quad")
    WINDOW.geometry('500x500')
    WINDOW.resizable(False, False)
    
    # visual properties
    titleText = Label(WINDOW, text = 'Solve my Quad', font = ("Times", 32))
    
    # like a bus stop, destinations that the user can seek by clicking the button, deleting the current window
    button1 = Button(WINDOW, text = 'Solution Calculator', font = ("Helvetica", 22), command = lambda: [WINDOW.destroy(), solutionCalc()])
    button2 = Button(WINDOW, text = 'Infinite Practice Problems', font = ("Helvetica", 22), command = lambda: [WINDOW.destroy(), infinitePractice()])
    button3 = Button(WINDOW, text = 'Sign Out', font = ("Helvetica", 22), command = lambda: [WINDOW.destroy(), passSys()])
    
    titleText.pack()
    button1.pack(padx = 0, pady = 25)
    button2.pack(padx = 0, pady = 25)
    button3.pack(padx = 0, pady = 25)
    WINDOW.mainloop()
    
    
def answerCalc(a,b,c):
    '''
    used for all user-like calculations. a, b, and c will be used for mathematical operations
    
    takes a, b, and c from either solutionCalc or infinitePractice to calculate the solution
    
    returns the process needed to solve the problem and its solution
    '''
    WINDOW = Tk() # creates a window
    WINDOW.attributes('-fullscreen', True) # looks user in fullscreen
    
    # this is so it knows what to title the window
    if where == 'solutionCalc':
        WINDOW.title("Solution Calculator") 
        titleText = Label(WINDOW, text = "Solution Calculator", font = ("Times", 18))
    else:
        WINDOW.title("Infinite Practice")
        titleText = Label(WINDOW, text = "Infinite Practice", font = ("Times", 18))
    WINDOW.geometry('500x500')
    
    # if user wants to go back to startUpWin(), they press this button.
    backButton = Button(WINDOW, text = "Back", font= ("Times", 12), command = lambda: [WINDOW.destroy(), startUpWin()])
    backButton.place(anchor="nw") # it's always in the top left corner
    titleText.pack()
    
    
    def r_sqrt(num):
        '''
        sqrt in radical form
        
        takes an inputted integer
        
        returns the leading coefficient and the radicand
        '''
        
        # finding prime factors
        orig_num = num
        primeList = list()
        if num < 0:
            num = abs(num)
        if num == 0:
            return (0, 1)
                
        i = 2 # starts at 2 because 1 is not a prime factor
        while True:
            if num == 1:
                break
            while num%i == 0:
                num //= i
                primeList.append(i)
            i += 1
        if len(primeList) == 0:
            if orig_num == 0:
                return (0, 1) # returns result as a tuple. If no radical, then equal 1
            elif orig_num == 1:
                return (1, 1)
            
        if len(primeList) == 1:
            return (1, orig_num)
            
        multiplier = list() # factor pairs
        no_pair = list()
            
        i = 0
        while True:
            try:
                if primeList[i] == primeList[i + 1]: # if the first term equals the next term, add to factor pair list
                    multiplier.append(primeList[i])
                    i += 1 # extra step to go past the other number in pair
                else:
                    no_pair.append(primeList[i])
                i += 1 # constant step
            except:
                if i < len(primeList): # if index number is within list and is the last number, add to no_pair
                    no_pair.append(primeList[i])
                break
            
        if len(multiplier) == 1 and len(no_pair) == 0: # if a perfect square, return as perfect square.
            return (multiplier[0], 1)
        if len(multiplier) == 0: # if cannot be simplified, return as radical
            return (1, orig_num)
            
        product = 1
        product1 = 1
        for i in multiplier:
            product *= i
            
        for i in no_pair:
            product1 *= i
            
        return product, product1 # returns coefficient and radicand for sqrt from given num
        
            
    def factorFinder(a, b, c):
        '''
        finds the factors using a, b, and c in a quadratic equation
        
        takes a, b, and c from solutionCalc or infinitePractice
        
        returns the factors for that equation, if any, and says if equation is factorable
        '''
        factorList = list()
        isFactorable = False
        if a != 1:
            if math.gcd(a, b, c) == abs(a):
                c2 = c//a
                b//=a
                a//=a
            else:
                c2 = c * a
        else:
            c2 = c
                
        for i in range(1, abs(c2) + 1):
            if abs(c2) % i == 0:
                if i in dict(factorList).values(): # ends when duplicate in list is found
                    break
                factorList.append([i, abs(c2)//i])
                    
        if b <= 0 and c2 < 0:
            for l in factorList:
                l[1] = -l[1]
                    
        if b > 0 and c2 < 0:
            for l in factorList:
                l[0] = -l[0]
                    
        if b < 0 and c2 > 0:
            for l in factorList:
                for i in range(len(l)):
                    l[i] = -l[i]
            
        for i in factorList:
            if sum(i) == b:
                trueFactors = [i[0], i[1]]
                isFactorable = True
                return trueFactors, isFactorable # states if an equation is factorable and its factors
        return None, isFactorable # equation is not factorable, returns False
        
    # for more complex factorable equations.    
    def factSolvable(a, b, c): # 
        '''
        for the intended output of:
        
          f1 f2
        f3 a  q
        f4 p  c
        
        When a != 1 and gcf != a using current state of a, b, and c, use this to find the content in the boxes
        
        takes a, b, and c from either solutionCalc or infinitePractice
        
        returns the values needed to put numbers in their respective places in the box method.
        '''
        
        p = factorFinder(a, b, c)[0][0]
        q = factorFinder(a, b, c)[0][1]
        f1 = math.gcd(a, p) # column 1
        f2 = math.gcd(c, q) # column 2
        if a < 0 and p < 0:
            f1 = -f1
        elif a > 0 and (q < 0 and p < 0):
            f1 = abs(f1)
            f1 = -f1
            
        if q < 0 and c < 0:
            f2 = -f2
        elif q > 0 and (a < 0 and c < 0):
            f2 = abs(f2)
            f2 = -f2
            
        f3 = a//f1
        f4 = c//f2

        return (f1, f2, f3, f4) # returns factors from equation ax^2+px+qx+c
        
        
    def quad_form(a, b, c):
        '''
        uses the quadratic formula to find the solution using a, b, & c from a quadratic equation
        
        Uses a, b, and c from either solutionCalc or infinitePractice
        
        returns solution using the quadratic formula in either fraction form, int form, or simplified rad form
        '''
        denominator = 2 * a
        b = -b
        if myDiscriminant(a, b, c) == '0':
            if b % (2 * a) == 0:
                solution = [b // denominator]
            else:
                gcf = math.gcd(b, denominator)
                if b < 0 and denominator < 0:
                    gcf = -gcf
                    
                b //= gcf
                denominator //= gcf
                solution = str(b) + '/' + str(denominator)
                    
            return solution # returns one solution
        
        if myDiscriminant(a, b, c) == '2pr':
            pos_form_num = int(b + math.sqrt((b**2) - (4 * a * c)))
            neg_form_num = int(b - math.sqrt((b**2) - (4 * a * c)))
            gcf1 = math.gcd(int(pos_form_num), denominator)
            gcf2 = math.gcd(int(neg_form_num), denominator)
                
            pos_form_num //= gcf1
            neg_form_num //= gcf2
            
            denominator_1 = denominator//gcf1
            denominator_2 = denominator//gcf2
                
            if pos_form_num % denominator_1 == 0:
                pos_solution = pos_form_num // denominator_1
            else:
                if pos_form_num < 0 and denominator_1 < 0:
                    pos_form_num = abs(pos_form_num)
                    denominator_1 = abs(denominator_1)
                    pos_solution = str(pos_form_num) + '/' + str(denominator_1)
                elif denominator_1 < 0:
                    pos_solution = '-' + str(pos_form_num) + '/' + str(abs(denominator_1))
                else:
                    pos_solution = str(pos_form_num) + '/' + str(denominator_1)
                
            if neg_form_num % denominator_2 == 0:
                neg_solution = neg_form_num // denominator_2
            else:
                if neg_form_num < 0 and denominator//gcf2 < 0:
                    neg_form_num = abs(neg_form_num)
                    denominator_2 = abs(denominator_2)
                    neg_solution = str(neg_form_num) + '/' + str(denominator_2)
                elif denominator_2 < 0:
                    neg_solution = '-' + str(neg_form_num) + '/' + str(abs(denominator_2))
                else:
                    neg_solution = str(neg_form_num) + '/' + str(denominator_2)
                    
            return [pos_solution, neg_solution] # returns pos and neg solution in list pair
        
        if myDiscriminant(a, b, c) == '2ir':
            if a < 0:
                denominator = -denominator
                b = -b
                c = -c
                a = -a
            leading_coe, radicand = r_sqrt((b**2) - (4 * a * c))
            gcf = math.gcd(leading_coe, b, denominator)
                
            leading_coe //= gcf
            b //= gcf
            denominator //= gcf
                
            if radicand == 1:
                if b == 0:
                    if denominator == 1:
                        solution = (f'\u00b1{leading_coe}', None)
                    else:
                        solution = (f'\u00b1{leading_coe}', str(denominator))
                else:
                    if denominator == 1:
                        solution = (f'{b}\u00b1{leading_coe}', None)
                    else:
                        solution = (f'{b}\u00b1{leading_coe}', str(denominator))
            elif leading_coe == 1:
                if b == 0:
                    if denominator == 1:
                        solution = (f'\u00b1\u221a{radicand}', None)
                    else:
                        solution = (f'\u00b1\u221a{radicand}', str(denominator))
                else:
                    if denominator == 1:
                        solution = (f'{b}\u00b1\u221a{radicand}', None)
                    else:
                        solution = (f'{b}\u00b1\u221a{radicand}', str(denominator))
            else:
                if b == 0:
                    if denominator == 1:
                        solution = (f'\u00b1{leading_coe}\u221a{radicand}', None)
                    else:
                        solution = (f'\u00b1{leading_coe}\u221a{radicand}', str(denominator))
                else:
                    if denominator == 1:
                        solution = (f'{b}\u00b1{leading_coe}\u221a{radicand}', None)
                    else:
                        solution = (f'{b}\u00b1{leading_coe}\u221a{radicand}', str(denominator))
                
            if solution[1] == None: # if no denominator, return expression
                return solution[0]
            return f'({solution[0]})/{solution[1]}' # if denominator, return solution as fraction
        
        elif myDiscriminant(a, b, c) == 'i':
            if a < 0:
                denominator = -denominator
                b = -b
                c = -c
                a = -a
            discriminant = (b**2) - (4 * a * c)
            leading_coe, radicand = r_sqrt(-discriminant)
            gcf = math.gcd(leading_coe, b, denominator)
                
            leading_coe //= gcf
            b //= gcf
            denominator //= gcf
                
            if radicand == 1:
                if b == 0:
                    if denominator == 1:
                        solution = (f'\u00b1{leading_coe}i', None)
                    else:
                        solution = (f'\u00b1{leading_coe}i', str(denominator))
                else:
                    if denominator == 1:
                        solution = (f'{b}\u00b1{leading_coe}i', None)
                    else:
                        solution = (f'{b}\u00b1{leading_coe}i', str(denominator))
            elif leading_coe == 1:
                if b == 0:
                    if denominator == 1:
                        solution = (f'\u00b1\u221a{radicand}i', None)
                    else:
                        solution = (f'\u00b1\u221a{radicand}i', str(denominator))
                else:
                    if denominator == 1:
                        solution = (f'{b}\u00b1\u221a{radicand}i', None)
                    else:
                        solution = (f'{b}\u00b1\u221a{radicand}i', str(denominator))
            else:
                if b == 0:
                    if denominator == 1:
                        solution = (f'\u00b1{leading_coe}\u221a{radicand}i', None)
                    else:
                        solution = (f'\u00b1{leading_coe}\u221a{radicand}i', str(denominator))
                else:
                    if denominator == 1:
                        solution = (f'{b}\u00b1{leading_coe}\u221a{radicand}i', None)
                    else:
                        solution = (f'{b}\u00b1{leading_coe}\u221a{radicand}i', str(denominator))
                
            if solution[1] == None: # if no denominator, return expression
                return solution[0]
            return f'({solution[0]})/{solution[1]}' # if denominator, return solution as fraction
                
                        
    def myDiscriminant(a, b, c): 
        '''
        finds the discriminant of a quadratic equation using its values a, b, and c
        
        uses a, b, and c input from either infinitePractice or answerCalc
        
        0 means one solution, 2pr means two perfect squares, 2ir means 2 irrational roots, and i means imaginary num
        '''
        discriminant = (b**2) - (4 * a * c)
        if discriminant == 0:
            return '0' # one rational root
        elif discriminant > 0 and r_sqrt(discriminant)[1] == 1:
            return '2pr' # two perfect rational roots
        elif discriminant > 0:
            return '2ir' # two irrational roots
        elif discriminant < 0:
            return 'i' # two unreal solutions
        
              
    def showProcess(a, b, c): 
        '''
        shows a student-like process of solving a problem using a quadratic equation's a b and c
        
        takes the a, b, and c input from either solutionCalc or infinitePractice
        
        returns the process needed to calculate the equation
        '''
        solution = quad_form(a,b,c) # finding the solution first.
        if b == 0: # square rooting
            explanation = Label(WINDOW, font = ('Arial', 15), text = "Best method: SQUARE ROOTING")
            explanation.pack(padx = 0, pady = 15)
                
            for i in range(5):
                debounce = False # if something is a part of a step, add to window
                    
                if i == 0:
                    myText = 'Set equation: {}x\u00b2{}=0'.format(a if a != 1 else '', c if c < 0 else '+' + str(c))
                        
                if i == 1:
                    c = -c
                    myText = 'Separate constant from variable: {}x\u00b2={}'.format(a if a != 1 else '', c)
                    
                if i == 2:
                    if a != 1:
                        myText = 'Remove coefficient from x: ({}x\u00b2)\u00F7{}={}\u00F7{}'.format(
                                                                             a if a != 1 else '', a, c, a)
                    else:
                        debounce = True # if no coefficient to remove, skip step
                            
                if i == 3:
                    if c % a == 0: # if an integer divide
                        c //= a
                    else: # if not, turn number into a fraction
                        c = f'{c}/{a}'
                    myText = f'Square root both sides: \u221a(x\u00b2)=\u00b1\u221a({c})'
                        
                if i == 4: # show solution
                    myText = f'x = {solution}'
                                        
                if debounce == False: # adds step to window unless step is unapplicable
                    equation_text = Label(WINDOW, font = ('Arial', 18), text = myText)  
                    equation_text.pack()
        
        # factorization if equation is factorable.
        elif factorFinder(a, b, c)[1] or c == 0: 
            explanation = Label(WINDOW, font=('Arial', 18), text='Best method: FACTORIZATION')
            explanation.pack()    
            gcf = math.gcd(a, b, c)
            if a < 0:
                gcf = -gcf
            
            # all programs change a, b, and c values as explanation goes along to make it realistic
            if c == 0:
                for i in range(6):
                    if i == 0:
                        # base eqt
                        myText = 'Set equation: {}x\u00b2{}x=0'.format(a if a != 1 else '', b if b < 0 else '+' + str(b))
                    if i == 1:
                        gcf = math.gcd(a, b) 
                        if a < 0:
                            gcf = -gcf
                        b //= gcf
                        a //= gcf
                        myText = 'Remove greatest common factor(gcf): {}x({}x{})=0'.format(gcf if gcf != 1 else '',
                                                       a if a != 1 else '',
                                                       b if b < 0 else '+' + str(b))
                    if i == 2:
                        myText = 'Set both expressions equal to 0: {}x=0, {}x{}=0'.format(gcf if gcf != 1 else '',
                                                             a if a != 1 else '',
                                                             b if b < 0 else '+' + str(b))
                    if i == 3:
                        b = -b
                        myText = 'Make x coefficient equal 1 or move constant to other side: ({}x)\u00F7{}=0\u00F7{}, {}x={}'.format(gcf if gcf != 1 else '', gcf, gcf,
                                                                              a if a != 1 else '', b)
                                                                                                 
                    if i == 4:
                        myText = 'Finish making x coefficient equal 1: x = 0, ({}x)\u00F7{}={}\u00F7{}'.format(a if a != 1 else '', a,
                                                                             b, a)
                    if i == 5:
                        myText = f'x = {solution}'
                            
                    equation_text = Label(WINDOW, font = ('Arial', 18), text = myText)  
                    equation_text.pack()
                       
            elif gcf == a:
                for i in range(8):
                    debounce = False
                    if i == 0:
                        myText = 'Set equation: {}x\u00b2{}x{}=0'.format(a if a != 1 else '',
                                                            b if b < 0 else '+' + str(b),
                                                            c if c < 0 else '+' + str(c))
                    if i == 1:
                        if a != 1:
                            myText = "Make 'a' in equation equal to 1: ({}x\u00b2{}x{})\u00F7{}=0\u00F7{}".format(a if a != 1 else '', 
                                                                                        b if b < 0 else '+' + str(b),
                                                                                        c if c < 0 else '+' + str(c), a, a)
                        else:
                            debounce = True
                    if i == 2:
                        b //= a
                        c //= a
                        a2 = 1
                            
                        p = factorFinder(a2, b, c)[0][0]
                        q = factorFinder(a2, b, c)[0][1]
                        myText = 'Find factors of c that when combined is b: {}\u00D7{} = {} and {}{} = {}'.format(p, q, c, p,
                                                                                                         q if q < 0 else '+' + str(q), b)
                    if i == 3:
                        myText = 'Set factor equation(x+p)(x+q): {}(x{})(x{})=0'.format(a, p if p < 0 else '+' + str(p),
                                                                                       q if q < 0 else '+' + str(q))
                    if i == 4:
                        if len(solution) == 1:
                            myText = 'Since both expressions are the same, set the expression equal to 0: x{}=0'.format(p if p < 0 else '+' + str(p))
                        else:
                            myText = 'Set both expressions equal to 0: x{}=0, x{}=0'.format(p if p < 0 else '+' + str(p),
                                                                                       q if q < 0 else '+' + str(q))
                    if i == 5:
                        if len(solution) == 1:
                            myText = 'Separate constant from variable: x{}{}={}'.format(p if p < 0 else '+' + str(p),
                                                                                       -p if -p < 0 else '+' + str(-p), -p)
                        else:
                            myText = 'Separate constant from variable: x{}{}={}, x{}{}={}'.format(p if p < 0 else '+' + str(p), -p if -p < 0 else '+' + str(-p), -p,
                                                q if q < 0 else '+' + str(q), -q if -q < 0 else '+' + str(-q), -q)
                    if i == 6:
                        if len(solution) == 1:
                            myText = f'Solve: x = {-p}'
                        else:
                            myText = f'Solve: x = {-p}, x = {-q}'
                        
                    if i == 7:
                        myText = f'x = {solution}'
                        
                    if debounce == False:
                        equation_text = Label(WINDOW, font = ('Arial', 18), text = myText)  
                        equation_text.pack()
                            
            else: # if a != 1 and gcf != a
                for i in range(10):
                    debounce = False
                    if i == 0:
                        myText = 'Set equation: {}x\u00b2{}x{}=0'.format(a if a != 1 else '',
                                                            b if b < 0 else '+' + str(b),
                                                            c if c < 0 else '+' + str(c))
                    if i == 1:
                        if gcf != 1:
                            myText = "Get rid of greatest common factor: ({}x\u00b2{}x{})\u00F7{}=0\u00F7{}".format(a if a != 1 else '', 
                                                                                       b if b < 0 else '+' + str(b),
                                                                             c if c < 0 else '+' + str(c), gcf, gcf)
                        else:
                            debounce = True
                    if i == 2:
                        a //= gcf
                        b //= gcf
                        c //= gcf
                            
                        p = factorFinder(a, b, c)[0][0]
                        q = factorFinder(a, b, c)[0][1]
                            
                        myText = 'Find factors of a\u00D7c that when combined is b: {}\u00D7{} = {} and {}{} = {}'.format(p, q, c*a, p,
                                                                               q if q < 0 else '+' + str(q), b)
                    if i == 3:
                        myText = 'Set another equation with factors: {}x\u00b2{}x{}x{}=0'.format(a if a != 1 else '', p if p < 0 else '+' + str(p),
                                                         q if q < 0 else '+' + str(q), c if c < 0 else '+' + str(c))
                    if i == 4:
                        myText = 'Put terms in a box-like form: \n\n{}x\u00b2 {}x\n{}x {}'.format(a if a != 1 else '', p, q, c)
                    if i == 5:
                        f1, f2, f3, f4 = factSolvable(a,b,c) # unpacks values from factSolvable into variables
                        
                        # creates a box like 'silhouette' for user to understand grouping method
                        myText = "Find factors in box so that when multiplied they equal what's inside the box:\n{}x   {}\n{}x {}x\u00b2 {}x\n{} {}x {}".format(
                                                                                               f3 if f3 != 1 else '',
                                                                                               f4, f1 if f1 != 1 else '',
                                                                                               a if a != 1 else '',
                                                                                               p if p != 1 else '',
                                                                                               f2, q if q != 1 else '',
                                                                                                                     c)
                    if i == 6:
                        f3 = a//f1
                        f4 = c//f2
                        myText = 'Set factor equation: ({}x{})({}x{}) = 0'.format(f1 if f1 != 1 else '',
                                                                                      f2 if f2 < 0 else '+' + str(f2),
                                                                                      f3 if f3 != 1 else '',
                                                                                      f4 if f4 < 0 else '+' + str(f4))
                        
                    if i == 7:
                        myText = 'separate constant from variable: {}x{}{}={}, {}x{}{}={}'.format(f1 if f1 != 1 else '',
                                                                           f2 if f2 < 0 else '+' + str(f2),
                                                                           -f2 if -f2 < 0 else '+' + str(-f2),
                                                                           -f2, f3 if f3 != 1 else '',
                                                                           f4 if f4 < 0 else '+' + str(f4),
                                                                           -f4 if -f4 < 0 else '+' + str(-f4), -f4)
                    if i == 8:
                        myText = 'Solve: {}x\u00F7{} = {}\u00F7{}, {}x\u00F7{} = {}\u00F7{}'.format(f1 if f1 != 1 else '', f1, -f2, f1,
                                                                                       f3 if f3 != 1 else '', f3, -f4, f3)
                    if i == 9:
                        myText = f'x = {solution}'
                        
                    if debounce == False:
                        equation_text = Label(WINDOW, font = ('Arial', 18), text = myText)  
                        equation_text.pack()
                        
        # completing the square, if radical coefficients don't go above 15 and if b and c are divisble by a
        elif (r_sqrt(abs(b//2 + c))[0] <= 15) and b % a == 0 and c % a == 0: 
            explanation = Label(WINDOW, font=('Arial', 18), text='Best method: COMPLETING THE SQUARE')
            explanation.pack()
                
            for i in range(10):
                debounce = False
                if i == 0:
                    myText = 'Set equation: {}x\u00b2{}x{}=0'.format(a if a != 1 else '',
                                                                         b if b < 0 else '+' + str(b),
                                                                         c if c < 0 else '+' + str(c))
                if i == 1:
                    if a != 1:
                        myText = 'Make a equal to 1: ({}x\u00b2{}x{})\u00F7{}=0\u00F7{}'.format(a if a != 1 else '',
                                                                                    b if b < 0 else '+' + str(b),
                                                                                    c if c < 0 else '+' + str(c), a, a)
                    else:
                        debounce = True
                            
                if i == 2:
                    b//=a
                    c//=a
                    a//=a
                    c = -c
                    myText = 'Put c on the other side of the equation: {}x\u00b2{}x   ={}'.format(a if a != 1 else '',
                                                                                                     b if b < 0 else '+' + str(b),
                                                                                                     c)
                if i == 3:
                    if b % 2 == 0:
                        quotient = b // 2
                        
                    else:
                        quotient = f'{b}/2'   
                    
                    myText = f'Find b\u00F72: {b}\u00F72 = {quotient}'
                if i == 4:
                    if b % 2 == 0:
                        quotient_2 = quotient**2
                    else:
                        quotient_2 = f'{b**2}/4'
                    myText = 'Do {} squared and add result to both sides: {}x\u00b2{}x{}={}{}'.format(quotient,
                                                                                    a if a != 1 else '',
                                                                                    b if b < 0 else '+' + str(b),
                                                                                    '+' + str(quotient_2),
                                                                                    c, '+' + str(quotient_2))
                if i == 5:
                    if type(quotient_2) == int and b % 2 == 0:
                        c += quotient_2
                    else:
                        if type(quotient_2) == str and math.gcd((c * 4) + (b ** 2)) == 4:
                            c = ((c * 4) + (b**2))//4
                        else:
                            denominator = 4 # will always be this value with the way Complete the Square accepts values
                            gcf = math.gcd((c * 4) + (b**2), denominator)
                            c = (c * 4) + (b ** 2)
                            c //= gcf
                            denominator //= gcf
                            
                            # Set up c this way to easily call numerical values for mathematical operations and concatenate too
                            c = str(c), '/', str(denominator) 
                            
                    factor = quotient # The quotient of b/2 is also the factor in the perfect square
                    if type(factor) == str:
                        # if number is negative, now it's positive
                        # if number was positive, now it's negative
                        if '-' in factor:
                            isNegative = True
                            factor_1 = factor.replace('-', '')
                            isNegative2 = False
                        else:
                            isNegative = False
                            factor_1 = '-' + factor
                            isNegative2 = True
                    else:
                        if factor < 0:
                            isNegative = True
                            factor_1 = str(-factor)
                            factor = str(factor)
                            isNegative2 = False
                        else:
                            isNegative = False
                            factor_1 = str(-factor)
                            factor = str(factor)
                            if '-' in factor_1:
                                isNegative2 = True
                            else:
                                isNegative2 = False
                            
                    myText = 'Set equation as perfect square and combine c and b\u00F72: (x{})\u00b2={}'.format(
                                                                    factor if isNegative else '+' + factor,
                                                                    c[0]+c[1]+c[2] if type(c) == tuple else c)
                    
                if i == 6:
                    myText = 'Square root both sides: \u221a((x{})\u00b2)=\u00b1\u221a({})'.format(factor if isNegative else '+' + factor,
                                                                                              c[0]+c[1]+c[2] if type(c) == tuple else c)
                if i == 7: 
                    myText = 'Separate constant from variable: x{}{}={}\u00b1\u221a({})'.format(
                                                factor if isNegative else '+' + factor,
                                                factor_1 if isNegative2 else '+' + factor_1, 
                                                factor_1, c[0]+c[1]+c[2] if type(c) == tuple else c)
                if i == 8:
                    if type(c) != tuple: # if c is an integer
                        if c < 0:
                            c2 = abs(c)
                        else:
                            c2 = c
                        if r_sqrt(c2)[1] == 1 or r_sqrt(c2)[0] == 1 and c > 0:
                            debounce = True
                        else:
                            if r_sqrt(c2)[1] == 1:
                                mySqrt = f'{r_sqrt(c2)[0]}'
                            elif r_sqrt(c2)[0] == 1:
                                mySqrt = f'\u221a{r_sqrt(c2)[1]}'
                            else:
                                mySqrt = f'{r_sqrt(c2)[0]}\u221a{r_sqrt(c2)[1]}'

                            if c < 0:
                                mySqrt += 'i'

                            myText = 'Simplify the radical: x = {}\u00b1{}'.format(factor_1, mySqrt)
                    else:
                        if int(c[0]) < 0:
                            c2 = abs(int(c[0]))
                        else:
                            c2 = int(c[0])
                        if r_sqrt(c2)[1] == 1 or r_sqrt(c2)[0] == 1 and int(c[0]) > 0:
                            debounce = True
                        else:
                            if r_sqrt(c2)[1] == 1:
                                mySqrt = f'{r_sqrt(c2)[0]}'
                            elif r_sqrt(c2)[0] == 1:
                                mySqrt = f'\u221a{r_sqrt(c2)[1]}'
                            else:
                                mySqrt = f'{r_sqrt(c2)[0]}\u221a{r_sqrt(c2)[1]}'

                            if int(c[0]) < 0:
                                mySqrt += 'i'
                                
                            denominator = int(c[2])
                            if r_sqrt(denominator)[1] == 1:
                                denominator = int(math.sqrt(denominator))
                            else:
                                denominator = f'\u221a{denominator}'

                            myText = 'Simplify the radical: x = {}\u00b1{}/{}'.format(factor_1, mySqrt, denominator)
                if i == 9:
                    myText = f'x = {solution}'
                        
                if debounce == False:
                    equation_text = Label(WINDOW, font = ('Arial', 18), text = myText)  
                    equation_text.pack()
                    
        else: # quadratic formula as a last resort
            explanation = Label(WINDOW, font=('Arial', 18), text='Best method: QUADRATIC FORMULA')
            explanation.pack()
            
            for i in range(7):
                debounce = False
                if i == 0:
                    myText = 'Set equation: {}x\u00b2{}x{}=0'.format(a if a != 1 else '',
                                                                    b if b < 0 else '+' + str(b),
                                                                    c if c < 0 else '+' + str(c))
                if i == 1:
                    myText = 'Plug in values to quadratic formula:\n{}\u00b1\u221a({}\u00b2-4({})({}))\n------------------\n2*{}'.format(-b, b, a, c, a)
                if i == 2:
                    discriminant = (b**2) - (4*a*c)
                    denominator = 2 * a
                    myText = "Evaluate what's inside the square root and denominator:\n{}\u00b1\u221a{}\n------------------\n{}".format(-b, discriminant, denominator)
                if i == 3:
                    leading_coe, radicand = r_sqrt(denominator)
                    if myDiscriminant(a,b,c) == '0' or myDiscriminant(a,b,c) == '2pr':
                        discriminant = int(math.sqrt(discriminant))
                        print(discriminant)
                        debounce = True
                    elif myDiscriminant(a,b,c) == '2ir':
                        if r_sqrt(discriminant)[1] == 1:
                            debounce = True
                            discriminant = int(math.sqrt(discriminant))
                        elif r_sqrt(discriminant)[0] == 1:
                            debounce = True
                            discriminant = f'\u221a{discriminant}'
                        else:
                            myText = f'Simplify radical: \u221a{discriminant} => {r_sqrt(discriminant)[0]}\u221a{r_sqrt(discriminant)[1]}'
                            discriminant = f'{r_sqrt(discriminant)[0]}\u221a{r_sqrt(discriminant)[1]}'
                    elif myDiscriminant(a,b,c) == 'i':
                        if r_sqrt(discriminant)[1] == 1:
                            myText = f'Simplify radical: \u221a{discriminant} => {r_sqrt(-discriminant)[0]}i'
                            discriminant = f'{r_sqrt(-discriminant)[0]}i'
                        elif r_sqrt(discriminant)[0] == 1:
                            myText = f'Simplify radical: \u221a{discriminant} => \u221a{r_sqrt(-discriminant)[1]}i'
                            discriminant = f'\u221a{r_sqrt(-discriminant)[1]}i'
                        else:
                            myText = f'Simplify radical: \u221a{discriminant} => {r_sqrt(-discriminant)[0]}\u221a{r_sqrt(-discriminant)[1]}i'
                            discriminant = f'{r_sqrt(-discriminant)[0]}\u221a{r_sqrt(-discriminant)[1]}i'
                if i == 4:
                    if myDiscriminant(a,b,c) == '0':
                        myText = f'Current equation: {-b}/{denominator}'
                    else:
                        myText = f'Current equation:\n{-b}\u00b1{discriminant}\n------------\n{denominator}'
                if i == 5:
                    if myDiscriminant(a,b,c) == '0':
                        myText = f'x = {solution}'
                    else:
                        if math.gcd(b, leading_coe, denominator) != 1:
                            myText = f'Simplify equation: {solution}'
                        else:
                            debounce = True
                if i == 6:
                    if myDiscriminant(a,b,c) == '0':
                        debounce = True
                    else:
                        myText = f'x =  {solution}'
                
                
                if debounce == False:
                    equation_text = Label(WINDOW, font = ('Arial', 18), text = myText)  
                    equation_text.pack()
        
    showProcess(a, b, c)
    
    if where == 'solutionCalc' : # used to know where to send user back to
        AGAIN = Button(WINDOW, text = 'Again?', font = ('Times', 12), command = lambda: [WINDOW.destroy(), solutionCalc()])
    else:
        AGAIN = Button(WINDOW, text = 'Again?', font = ('Times', 12), command = lambda: [WINDOW.destroy(), infinitePractice()])

    titleText.pack()
    AGAIN.pack(padx = 50, pady = 10)
    WINDOW.mainloop()
    

def solutionCalc():
    '''
    a friendly graphical interface for user to enter quadratic equation values from a, b, and c
    
    returns correct window or processes calculation according to functions
    '''
    # GRAPHICS
    WINDOW = Tk()
    WINDOW.title("Solution Calculator")
    WINDOW.attributes('-fullscreen', True) # locks user in fullscreen
     
    def entryInteract(): 
        '''
        when the enter button gets hit, it takes info from text boxes and transfers that to answerCalc for a solution
        
        sends user to answerCalc for the correct answer
        '''
        try:
            a = int(entry_a.get())
            b = int(entry_b.get())
            c = int(entry_c.get())
            
            1/a # checks if a is equal to 0 through zero division
            
            WINDOW.destroy()
            global where # used so when sent to answerCalc, answerCalc knows where to send user back to
            where = 'solutionCalc'
            answerCalc(a,b,c)
            
        except ZeroDivisionError: # cannot be equal to 0 in a quadratic equation
            errorText = Label(WINDOW, font = ('Arial', 14), fg ='red', text = "a cannot be equal to '0' in a quadratic equation.\nPlease try again.")
            errorText.pack()
        except Exception as ex: # packs exception onto window
            errorText = Label(WINDOW, font = ('Arial', 14), fg = 'red', text = ex)
            errorText.pack()
        
    titleText = Label(WINDOW, text = "Solution Calculator", font = ("Times", 18))
    backButton = Button(WINDOW, text = "Back", font= ("Times", 12), command = lambda: [WINDOW.destroy(), startUpWin()])
    text_prompt = Label(WINDOW, text = "Enter a, b, and c from equation ax\u00b2+bx+c=0", font = ("Helvetica", 16))
    entry_a = Entry(WINDOW, font = ("Arial", 16))
    entry_b = Entry(WINDOW, font = ("Arial", 16))
    entry_c = Entry(WINDOW, font = ("Arial", 16))
    
    
    backButton.place(anchor="nw")
    titleText.pack()
    text_prompt.pack()
    entry_a.pack(padx = 10, pady = 0)
    entry_b.pack(padx = 10, pady = 0)
    entry_c.pack(padx = 10, pady = 0)
    
    #CODE
        
    ENTER = Button(WINDOW, text = 'Enter', font = ('Times', 12), command = entryInteract)
    ENTER.pack(padx = 50, pady = 10)
    WINDOW.mainloop()
    
    
def infinitePractice():
    '''
    graphical interface used to generate equations for practice
    
    either sends back to startUpWin, or sends to find the solution in answerCalc
    '''
    # GRAPHICS
    WINDOW = Tk() # Generates window
    WINDOW.title("Infinite Practice Problems") # if you hover over application, that's the name
    WINDOW.attributes('-fullscreen', True) # locks user in fullscreen.
    
    
    titleText = Label(WINDOW, text = 'Infinite Practice Problems', font = ('Times', 18))
    backButton = Button(WINDOW, text = "Back", font= ("Times", 12), command = lambda: [WINDOW.destroy(), startUpWin()])
    desc = Label(WINDOW, text = "Solve this equation.")
    
    # Functionality
    # have to use both, computer only prints positive: print(sqrt(25), -sqrt(25))
    
    
    #userEntry.bind('<Return>', Evaluate)
    
    titleText.pack()
    desc.pack()
    #userEntry.pack(padx = 0, pady = 10)
    backButton.place(anchor="nw")
    
    # for standard form:
    def generate_rn(): 
        '''
        generates numbers for quadratic equation
        
        returns list of random numbers
        '''
        stackList = list()
        for i in range(3):
            rn = randint(-15, 15)
            stackList.append(rn)
        return stackList 
    
    a, b, c = generate_rn() # unpacks random generated numbers into a, b, and c
    if a == 0: # a cannot be equal to 0, so if rn = 0 it changes 0 to 1
        a = 1
    
    myText = '{}x\u00b2'.format(a if a != 1 else '') # baseline equation
    if b != 0: # if b equals to 0, don't include it in equation
        myText += '{}x'.format(b if b < 0 else '+' + str(b))
    if c != 0: # if c equals to 0, don't include it in equation
        myText += '{}'.format(c if c < 0 else '+' + str(c))
    myText += '=0' # always add =0 at the end to make it a basic quadratic equation
    eqt = Label(WINDOW, font = ('Arial', 15), text = myText)

    def entryInteract():
        '''
        when reveal button is hit, it takes user to the answer
        
        sends user to answerCalc to calculate their answer like how a student would
        '''
        global where # used to say where a user was sent from to determine where to be sent back to later
        where = 'infinitePractice'
        answerCalc(a,b,c)
        
    eqt.pack(padx = 0, pady = 5)
    REVEAL = Button(WINDOW, text = 'Reveal answer?', font = ('Times', 12), command = lambda: [WINDOW.destroy(), entryInteract()])
    REVEAL.pack(padx = 50, pady = 10)
    WINDOW.mainloop()

passSys() # initiation of program, all other functions spring from this


# In[ ]:




