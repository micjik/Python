
#def main():
##    print (f"This is the first module's name:{(__name__)}")

#if __name__ == '__main__': ## It means am running this on the python script directly, am not importing
 #     main()

#if __name__ == '__main__':
 #   print("Run directly")
#else:
#    print("Run From import")

print("This will always be run")

def main():
    print("First Module's main Method")

if __name__ == '__main__':
    main()