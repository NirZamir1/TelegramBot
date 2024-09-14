from scechduler import scechduler
def Update(args):
    #getts called after certain amount of time indefinitely
    print(f"normal:{args}")
    
def FixedUpdate(args):
    #gets called on changes made
    print(f"fixed:{args}")

def main():
    scech = scechduler(Update,FixedUpdate,frenquency=1,activeDuration=(0,24))
    scech.run()

if __name__ == "__main__":
    main()