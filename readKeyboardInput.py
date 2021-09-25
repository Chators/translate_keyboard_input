import struct
import sys

if sys.argv == '':
        print('Need a filename')
        exit

filename = sys.argv[1]

azerty_keys = {
    2: "&", 3: "~", 4: '"', 5: "'", 6: "(", 7: "-", 8: "è", 9: "_", 10: "ç",
    11: "@", 12: ")", 13: "=", 14: "[BACKSPACE]", 15: "\t", 16: "a", 17: "z",
    18: "e", 19: "r", 20: "t", 21: "y", 22: "u", 23: "i", 24: "o", 25: "p", 26: "^",
    27: "$", 28: "[ENTER]\n", 29: "[CTRL]", 30: "q", 31: "s", 32: "d", 33: "f", 34: "g",
    35: "h", 36: "j", 37: "k", 38: "l", 39: "m", 40: "ù", 41: "*", 42: "[SHIFT]",
    43: "*", 44: "w", 45: "x", 46: "c", 47: "v", 48: "b", 49: "n", 50: ",",
    51: ";", 52: ":", 53: "!", 54: "[SHIFT]", 55: "[FN]", 56: "[ALT]", 57: " ", 58: "[CAPSLOCK]",
    60: '[F2]', 74: '-', 71: '7', 100: '[ALT]', 82: '0', 83: '.', 80: '2', 96: '[ENTER]\n', 88: '[F12]',
    86: '<', 103: '[ARROWUP]', 78: '+', 73: '9', 75: '4', 79: '1', 76: '5', 1: '[ESC]'
}

azerty_keys_maj = {
    2: "1", 3: "2", 4: "3", 5: "4", 6: "5", 7: "6", 8: "7", 9: "8", 10: "9",
    11: "0", 12: "°", 13: "+", 14: "[BACKSPACE]", 15: "\t", 16: "A", 17: "Z",
    18: "E", 19: "R", 20: "T", 21: "Y", 22: "U", 23: "I", 24: "O", 25: "P", 26: "¨",
    27: "£", 28: "[ENTER]\n", 29: "[CTRL]", 30: "Q", 31: "S", 32: "D", 33: "F", 34: "G",
    35: "H", 36: "J", 37: "K", 38: "L", 39: "M", 40: "%", 41: "µ", 42: "[SHIFT]",
    43: "µ", 44: "W", 45: "X", 46: "C", 47: "V", 48: "B", 49: "N", 50: "?",
    51: ".", 52: "/", 53: "§", 54: "[SHIFT]", 55: "[FN]", 56: "[ALT]", 57: " ", 58: "[CAPSLOCK]",
    61: '[F2]', 74: '-', 71: '7', 100: '[ALT]', 82: '0', 83: '.', 80: '2', 96: '[ENTER]\n', 88: '[F12]',
    86: '>', 103: '[ARROWUP]', 78: '+', 73: '9', 75: '4', 79: '1', 76: '5', 1: '[ESC]'
}

azerty_keys_alt = {
    2: "1", 3: "~", 4: "#", 5: "{", 6: "[", 7: "|", 8: "`", 9: "\\", 10: "Z",
    11: "@", 12: "]", 13: "}", 14: "[BACKSPACE]", 15: "\t", 16: "A", 17: "Z",
    18: "E", 19: "R", 20: "T", 21: "Y", 22: "U", 23: "I", 24: "O", 25: "P", 26: "¨",
    27: "¤", 28: "[ENTER]\n", 29: "[CTRL]", 30: "Q", 31: "S", 32: "D", 33: "F", 34: "G",
    35: "H", 36: "J", 37: "K", 38: "L", 39: "M", 40: "%", 41: "µ", 42: "[SHIFT]",
    43: ">", 44: "W", 45: "X", 46: "C", 47: "V", 48: "B", 49: "N", 50: "?",
    51: ".", 52: "/", 53: "§", 54: "[SHIFT]", 55: "[FN]", 56: "[ALT]", 57: " ", 58: "[CAPSLOCK]",
    61: '[F2]', 74: '-', 71: '7', 100: '[ALT]', 82: '0', 83: '.', 80: '2', 96: '[ENTER]\n', 88: '[F12]',
    86: '<', 103: '[ARROWUP]', 78: '+', 73: '9', 75: '4', 79: '1', 76: '5'
}

with open(filename, 'rb') as keyboard_file:
        isCaps = False
        isShift = False
        isAlt = False
        result = ''
        try :
            while True:
                    data = keyboard_file.read(24)
                    # Timestamp INT, 0, Timestamp_DEC int, 0, type, code (key pressed), value (press/release)

                    typez = struct.unpack('4IHHI', data)[4]
                    code = struct.unpack('4IHHI', data)[5]
                    value = struct.unpack('4IHHI', data)[6]

                    if (code == 54 or code == 42) and value == 0 and typez == 1:
                        isShift = False
                    elif (code == 100 or code == 56) and value == 0 and typez == 1:
                        result += '[ALTSUP]'
                        isAlt = False
                        print('mdr')
                    elif code != 0 and value == 1 and typez == 1:
                        if code == 58:
                            isCaps = not isCaps
                        elif code == 54 or code == 42:
                            isShift = True
                        elif code == 100 or code == 56:
                            result += '[ALT]'
                            isAlt = True
                        elif not azerty_keys.get(code):
                            result += f'[PetitCode{code}]'
                        elif isCaps or isShift:
                            result += azerty_keys_maj.get(code)
                        #elif isAlt:
                        #   print('lool')
                        #  result += azerty_keys_alt.get(code)
                        elif code == 14:
                            result = result[:-1]
                        else:
                            result += azerty_keys.get(code)
        except:
            print (result)
