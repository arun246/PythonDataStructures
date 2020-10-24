class CaesarCipher:

    def __init__(self,shift):
        encoder=[None]*26
        decoder = [None]*26
        for i in range(26):
            encoder[i] = chr((i+shift)%26 + ord('A'))
            decoder[i] = chr((i-shift)%26  + ord('A'))
        self._enc = ''.join(encoder)
        self._dec = ''.join(decoder)

    def encrypt(self,msg):
        return self._transform(msg,self._enc)

    def decrypt(self,msg):
        return self._transform(msg,self._dec)

    def _transform(self,mssg,mapper):
        msg =list(mssg)
        for i in range(len(msg)):
            if (msg[i].isupper()):
                j= ord(msg[i])-ord('A')
                msg[i] = mapper[j]
        return "".join(msg)


cipher = CaesarCipher(3)
message = "THE EAGLE IS IN PLAY; MEET AT JOE S."

print("Secret:", cipher.encrypt(message))
