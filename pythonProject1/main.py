# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if__name__ == '__main__':
    print

    s = "abc"
    s[1]

    type (5)
    print (3.0 -1)



    usa_gold = 46
    uk_gold = 27
    romania_gold = 1

    total_gold = usa_gold + uk_gold + romania_gold
    print(total_gold)

    romania_gold += 1
    print(total_gold)



    pset_time = 15
    sleep_time = 8
    print(sleep_time > pset_time)
    derive = true
    drink = false
    both = drink and derive
    print(both)



    type (5)


    hi = "hello"
    name = "sumana"
    greet = (hi + " " + name + " ")*3
    print (greet)

    x = 1
    print (x)

    x= float (input("Enter a number for x:"))
    y= float(input("enter a number for y:"))
    if x==y:
        print ("x and y are equal")
        if y!=0:
            print ("therefore, x/y is", x/y )
    elif x<y:
            print ("x is smaller")

    else:
            print ("y is smaller ")

    for n in range (5,11,2) :
        print (n)

    mysum = 0
    for i in range (7,10) :
        mysum +=i
    print (mysum)


    s="abs"
    print (s [2])

    s = "abcdefgh"
    for index in range (len(s)) :
        if s[index] == "a" or s[index] == 'b' :
            print (" there is an a or b")

    s = "abcdefgh"
    for var in s:
         if var == "d" or var == "b" :
             print ("there is an i or u")
    an_letters ="aeiouAEIOU"
    word= input("i will cheer for u! enter a word: ")
    times= int(float(input("enthusiasm level :")))

    for char in word:
        if char in an_letters:
            print("Give me an " + char + "!")
        else :
            print( "give me a " + char + "!")
    print ("what does that spell?")
    for i in range (times) :
        print (word, "!!!")

    cube = 8
    for guess in range (cube +1):
            if guess**3 == cube :
                print ("cube root of ", cube, "is", guess)


    def f(x):
        x=x+1
        print ("in f(x) : x-",x)
        return x

    x =3
    z = f(3)













# See PyCharm help at https://www.jetbrains.com/help/pycharm/
