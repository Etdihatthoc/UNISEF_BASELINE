**Set up thí nghiệm**

1. Clone github [https://github.com/Etdihatthoc/UNISEF\_BASELINE](https://github.com/Etdihatthoc/UNISEF\_BASELINE)   
2. Tải pretrained model từ Drive   
   cd UNISEF\_BASELINE  
   wget https://cloudreve.vmv.re/api/v3/file/source/22096/hermes\_resunet.pth\\?sign\\=zzipfrjfRYmQtmiC5bhIRu4jE71Z\_ZDzRniaTLyR5rM%3D%3A0  
   
   sau khi tải xong đổi tên thành hermes\_resunet.pth

3. Tạo môi trường ảo, install các package :   
   pip install \-r requirements.txt  
   git clone [https://github.com/Etdihatthoc/apex](https://github.com/Etdihatthoc/apex)  
   cd apex  
   python3 setup.py install  
   cd ..  
     
4\. Training  

- CUDA\_VISIBLE\_DEVICES=0 python train.py \--gpu 0 \--batch\_size 1 \--load hermes\_resunet.pth \--resume \--dataset 1p\_train

