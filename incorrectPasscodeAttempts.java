//Opening the Dropbox mobile app on the VIU's tablet requires a four-digit passcode. To ensure the confidentiality of the stored information, the device is locked out of Dropbox after 10 consecutive failed passcode attempts. We need to implement a function that, given an array of attempts made throughout the day and the correct passcode, checks to see if the device should be locked, i.e. 10 or more consecutive failed passcode attempts were made.

//Nicohlas Tillmann, CodeSignal Solution, 

boolean incorrectPasscodeAttempts(String passcode, String[] attempts) {
    int wrongAttempts = 0;
    for (int i = 0; i < attempts.length; i++) {
        if (passcode.equals(attempts[i])) 
            wrongAttempts = 0;
         else {
            wrongAttempts++;
            if (wrongAttempts >= 10) {
                return true;
            }
        }
    }
    return false;
}