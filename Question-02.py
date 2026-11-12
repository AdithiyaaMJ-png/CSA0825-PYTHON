correct_otp = "4821"
attempts = 0

while attempts < 3:
    entered = input("Enter OTP: ").strip()

    if entered == "":
        print("Blank entry. Please try again.")
        continue

    attempts += 1

    if entered == correct_otp:
        print("OTP verified")
        break
    else:
        print("Wrong OTP")

else:
    print("Account locked for 30 minutes")


correct_otp = "4821"
attempts = 0

for i in range(3):
    entered = input("Enter OTP: ").strip()

    while entered == "":
        print("Blank entry does not count.")
        entered = input("Enter OTP: ").strip()

    attempts += 1

    if entered == correct_otp:
        print("OTP verified")
        break
    print("Wrong OTP")
else:
    print("Account locked for 30 minutes")


max_attempts = 3
if input("Answer security question correctly? (yes/no): ").lower() == "yes":
    max_attempts += 2

attempts = 0
while attempts < max_attempts:
    entered = input("Enter OTP: ").strip()
    if not entered:
        print("Blank entry does not count.")
        continue
    attempts += 1
    if entered == "4821":
        print("OTP verified")
        break
    print("Wrong OTP")
else:
    print("Account locked for 30 minutes")


def verify_otp(attempts_left):
    if attempts_left == 0:
        print("Account locked for 30 minutes")
        return

    entered = input("Enter OTP: ").strip()
    if not entered:
        print("Blank entry does not count.")
        return verify_otp(attempts_left)

    if entered == "4821":
        print("OTP verified")
    else:
        print("Wrong OTP")
        verify_otp(attempts_left - 1)

verify_otp(3)
