import argparse
from PIL import Image
import pytesseract

# Đường dẫn tới Tesseract nếu cần thiết
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def perform_ocr(image_path):
    try:
        img = Image.open(image_path)
        
        # Chuyển ảnh sang grayscale và sau đó sang nhị phân
        img = img.convert('L')  # Chuyển sang ảnh xám
        img = img.point(lambda x: 0 if x < 140 else 255)  # Binarization
        
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Đã xảy ra lỗi: {e}"

def main():
    # Tạo đối tượng phân tích tham số dòng lệnh
    parser = argparse.ArgumentParser(description="OCR Tool - Nhận diện ký tự từ ảnh")
    
    # Thêm tham số 'image' để người dùng chỉ định ảnh đầu vào
    parser.add_argument('image', type=str, help="Đường dẫn tới tệp ảnh")
    
    # Phân tích các tham số dòng lệnh
    args = parser.parse_args()
    
    # Thực hiện OCR với ảnh đã chỉ định
    result = perform_ocr(args.image)
    
    # In kết quả OCR
    print("Văn bản trích xuất từ ảnh:\n")
    print(result)

if __name__ == '__main__':
    main()
