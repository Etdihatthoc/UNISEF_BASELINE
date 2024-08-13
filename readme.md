**Set up thí nghiệm**

1. Clone github [https://github.com/Etdihatthoc/UNISEF\_BASELINE](https://github.com/Etdihatthoc/UNISEF\_BASELINE)   
2. Tải pretrained model từ Drive   
   cd UNISEF\_BASELINE  
   wget https://cloudreve.vmv.re/api/v3/file/source/22096/hermes\_resunet.pth\\?sign\\=zzipfrjfRYmQtmiC5bhIRu4jE71Z\_ZDzRniaTLyR5rM%3D%3A0  
     
3. Tạo môi trường ảo, install các package :   
   pip install \-r requirements.txt  
   git clone [https://github.com/Etdihatthoc/apex](https://github.com/Etdihatthoc/apex)  
   cd apex  
   python3 setup.py install  
   cd ..  
     
4. Với tập dataset, setup dữ liệu như sau  
   Trước hết, tạo các folder data/1p\_train, data/10p\_train, data/50p\_train, data/100p\_train, prepoccessing\_data trong UNISEF\_BASELINE  
     
- python dataset\_conversion/our.py

  Chú ý: sửa 

   src\_path \= '/home/aiotlabws/SonDinh/universal-medical-image-segmentation/uniseg-evaluation/50p\_train/'

      tgt\_path \= '/home/aiotlabws/SonDinh/universal-medical-image-segmentation/data/50p\_train/'

  dòng 46,47 cho các tập dữ liệu tương ứng \=\> mỗi lần chạy ứng với 1 tập dataset, kết quả lưu ở tgt\_path 


- python python dataset\_conversion/nii2npy.py

6\. Training  
 

- CUDA\_VISIBLE\_DEVICES=0 python train.py \--gpu 0 \--batch\_size 1 \--load hermes\_resunet.pth \--resume \--dataset 1p\_train

