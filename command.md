首次配置
------------
git config --global user.name "your_username"  
git config --global user.email your_email@domain.com  
ssh-keygen -t rsa -C "your_email@domain.com"  
cat rsa.id_rsa.pub #将内容复制到github你的项目-seting-Deploy keys-Add deploy key  
ssh -T git@github.com #测试连通性  
git clone https://wangyishuai007@github.com/Eason-Wang/pyScript.git  

上传文件
------------
mkdir xxx  
git init  
git add sendemail.py   
git commit -m "add sendemayl.py"  
git push origin master  

更改文件
------------
git add sendemail.py  
git commit -m "modify"  
git push  
