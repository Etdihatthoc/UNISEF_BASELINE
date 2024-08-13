import os

# Đường dẫn tới thư mục chứa các tập train
base_path = "/home/aiotlabws/SonDinh/universal-medical-image-segmentation/uniseg-evaluation"

# Tạo một dictionary chứa các tập train và test
train_test_split = {}

# Liệt kê các thư mục con trong base_path
subdirs = ['1p_train', '10p_train', '50p_train', '100p_train','test']

# Lặp qua các thư mục con
for subdir in subdirs:
    images_path = os.path.join(base_path, subdir, "images")
    # Liệt kê tất cả các tệp .nii.gz trong thư mục images và loại bỏ phần đuôi .nii.gz
    train_files = [os.path.splitext(os.path.splitext(f)[0])[0] for f in os.listdir(images_path) if f.endswith(".nii.gz")]
    
    # Test files giống nhau cho tất cả các tập (giả sử bạn muốn dùng chính các file train này)
    test_files = train_files  # Nếu test files khác, bạn có thể cập nhật lại dòng này
    
    # Tạo key-value cho train và test
    train_test_split[f"{subdir}_train"] = train_files
    train_test_split[f"{subdir}_test"] = test_files

# In ra kết quả
print(train_test_split)
