**Set up thí nghiệm**

1. git clone -b main_3 [https://github.com/Etdihatthoc/UNISEF\_BASELINE](https://github.com/Etdihatthoc/UNISEF\_BASELINE)   
2. Tải pretrained model 
   cd UNISEF\_BASELINE  
   wget https://cloudreve.vmv.re/api/v3/file/source/22096/hermes_resunet.pth?sign=zzipfrjfRYmQtmiC5bhIRu4jE71Z_ZDzRniaTLyR5rM%3D%3A0

   sau khi tải xong đổi tên thành hermes\_resunet.pth

3. Tạo môi trường ảo, install các package :   

   pip install \-r requirements.txt  
   git clone [https://github.com/Etdihatthoc/apex](https://github.com/Etdihatthoc/apex) 
   cd apex  
   python3 setup.py install  
   cd ..  

4. CHÚ Ý: Sửa lại abs path trong:

   - training\dataset\dim3\dataset_universal.py (self.data_root = '')

   - training\dataset\dim3\tools.py (base_path ="")

5. Với tập dataset, setup dữ liệu như sau

   Chú ý: 
         Nếu bị lỗi torch._six = > vào \apex\apex\amp\\_initialize.py sửa lại torch._six import string_classes bằng string_classes = str

         Sửa lại thành abs path 2 cái dưới đây trong mỗi file

      Ví Dụ: 
      
      src_path = '/home/aiotlabws/SonDinh/universal-medical-image-segmentation/uniseg-evaluation/Sarcoma_train_1p/'
      tgt_path = '/home/aiotlabws/SonDinh/universal-medical-image-segmentation/data/Sarcoma_train_1p/'
   
      => mỗi lần chạy ứng với 1 tập dataset, kết quả lưu ở tgt_path. Chạy 4 command dưới đây
   - python dataset_conversion/1p_train.py

   - python dataset_conversion/10p_train.py

   - python dataset_conversion/50p_train.py

   - python dataset_conversion/100p_train.py

      Sửa lại abs path trong file dataset_conversion/nii2npy.py ví dụ:
      
      source_path = '/content/drive/MyDrive/UNISEF_BASELINE/data/'
      target_path = '/content/drive/MyDrive/UNISEF_BASELINE/prepoccessing_data/'

   - python dataset_conversion/nii2npy.py

6. Training  
   Lưu ý: sửa lại epochs = 5 trong config\universal\hermes_resunet_3d.yaml để test xem chạy ổn chưa

   - CUDA\_VISIBLE\_DEVICES=0 python train.py \--gpu 0 \--batch\_size 1 \--load hermes\_resunet.pth \--resume \--dataset Sarcoma_train_1p

   => mỗi lần chạy ứng với 1 tập dataset, sửa --dataset tương ứng Sarcoma_train_1p, Sarcoma_train_10p, Sarcoma_train_50p

