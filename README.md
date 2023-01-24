# passgenpy
Passgen

Used for currently unidentified routers from either Zyxel or D-link\
Found in /usr/bin of the binwalked firmware of the\
Zyxel LTE3301-M209 (LTE3301-M209_V1.00(ABLG.0)C0.zip)\

Mode 1: lower case ASCII\
Mode 2: lower and upper case ASCII\
Mode 3: memorable word\
Mode 4: alphanumeric upper and lower case\
Mode 5: numberic\
Mode 6: hexadecimal\

Usage: python3 passgen.py "hello world" 3 -length 10

Thanks to drsnooker for his Matlab code that this was converted from: https://forum.hashkiller.io/index.php?threads/unpublished-wpa-key-algorithms.19944/post-324060
