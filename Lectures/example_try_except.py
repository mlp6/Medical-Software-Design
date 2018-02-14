def print_example():
    # comment out this next line
    #print(testdict)

    # note that none of this will run if the line above is in play
    try:
        print(testdict)
    # try changing this to IOError or do not specify error
    #except NameError:
    except IOError:
        print("You are out of space.")
    except:
        print("You are trying to print something that doesn't exist.")

    testdict = {'name': 'Kathy', 'grade': 100}

    print(testdict)


def div_example():
    import logging
    logging.basicConfig(filename='divlog.txt', level=logging.DEBUG) 

    for x in [3, 5, 7, 0, 9]:
        # comment out this next line
        #y = 10/x
    
        try:
            y = 10/x
        except ZeroDivisionError:
            logging.error("div by 0, skipping this iteration")
            #y = None
            continue 
            #break

        print(y)

if __name__ == "__main__":
    #print_example()
    div_example()
