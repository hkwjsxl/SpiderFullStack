import pytesseract
from PIL import Image



if __name__ == '__main__':
    img = Image.open('img_1.png')
    # code = pytesseract.image_to_string(img)
    code = pytesseract.image_to_string(img, lang='chi_sim')  # 识别汉字
    print(code)



