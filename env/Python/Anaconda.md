# Windows下使用Anaconda

## 安装

- 环境变量  
E:\Anaconda（Python需要）  
E:\Anaconda\Scripts（conda自带脚本）  
E:\Anaconda\Library\bin（jupyter notebook动态库）  
E:\Anaconda\Library\mingw-w64\bin（使用C with python的时候）  
E:\Anaconda\Library\usr\bin  

## 常用命令 
    # 列出所有环境
    conda env list
    
    # 查看环境下安装的包
    conda list  # 查看通过conda方式安装的包
    pip list    # 查看通过pip方式安装的包
    
    # 创建虚拟环境
    conda  create -n python38  python=3.8 包名2 包名3 ...
    
    # 激活指定环境（conda4之前的版本是：source activate envName）
    conda activate envName
    
    # 退出当前环境
    conda deactivate
    
    # 删除环境
    conda remove -n py38 --all
