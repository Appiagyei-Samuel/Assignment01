correctPassword="secret"
userAttempt=""
attemptLeft=3
while(attemptLeft>0)and(userAttempt!=correctPassword):
    userAttempt=input(f"Enter password{attemptLeft}")
    attemptLeft-=1
if(userAttempt==correctPassword):
    {
        print("Access Granted")
    }
else:
    {
        print("Access denied")
    }
        