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
   training\dataset\dim3\dataset_universal.py

   training\dataset\dim3\tools.py

5. Với tập dataset, setup dữ liệu như sau
   - python dataset_conversion/our.py

   Chú ý: sửa lại thành abs path 2 cái dưới đây

   src_path = '/home/aiotlabws/SonDinh/universal-medical-image-segmentation/uniseg-evaluation/Sarcoma_train_1p/'

   tgt_path = '/home/aiotlabws/SonDinh/universal-medical-image-segmentation/data/Sarcoma_train_1p/'

   dòng 46,47 cho các tập dữ liệu tương ứng => mỗi lần chạy ứng với 1 tập dataset, kết quả lưu ở tgt_path

   - python python dataset_conversion/nii2npy.py

6. Training  
   Lưu ý: sửa lại epochs = 5 trong config\universal\hermes_resunet_3d.yaml để test xem chạy ổn chưa

   - CUDA\_VISIBLE\_DEVICES=0 python train.py \--gpu 0 \--batch\_size 1 \--load hermes\_resunet.pth \--resume \--dataset Sarcoma_train_1p

   => mỗi lần chạy ứng với 1 tập dataset, sửa --dataset tương ứng Sarcoma_train_1p, Sarcoma_train_10p, Sarcoma_train_50p, Sarcoma_train_100p

