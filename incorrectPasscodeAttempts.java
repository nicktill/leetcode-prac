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