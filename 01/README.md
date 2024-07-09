# 配置环境

```shell
# 推荐使用 vmr 安装/管理 miniconda

conda --version
#conda 24.5.0

# 配置 py310 环境

conda create --name py310 python=3.10
conda activate py310

pip install jupyterlab==4.0.9
pip install ipywidgets==8.1.1
pip install openai==1.6.1

# 改配置
jupyter lab --generate-config

# 添加 c.ServerApp.ip = '*' 到 ~/.jupyter/jupyter_lab_config.py 文件的末尾
# 前提是先备份
cp ../.jupyter/jupyter_lab_config.py ../.jupyter/jupyter_lab_config.py.bak
echo "c.ServerApp.ip = '*'" >> ~/.jupyter/jupyter_lab_config.py

jupyter-lab  --no-browser --port=8888 --NotebookApp.token='替换为你的密码' .

# jupyter-lab  --no-browser --port=8888 --NotebookApp.token='jasonos' .
# 使用  --no-browser 的原因是我的环境为 ubuntu server 24 LTS
# 环境配置相关，请参考：https://github.com/DjangoPeng/openai-quickstart


```

我的环境是 vscode 穿 Ubuntu Server 24 LTS

相关插件是

```txt
Python Type Hint
Python Path
Python Extension Pack
Python Environment Manager
Python Debugger
Python
Pylance
```

同时，我的 openai 代理地址和相关 key 也都通过环境变量的方式进行上传

```shell

# api-key
echo "1kNS+VLGjx+5Vl2F0+cbVhnCm/HQz0I9u8P5MJp+K8/lm4sU21yDnXUxnAOY5G7ZE+piGd+LYEAEAWFYpzWMAQ==" | openssl enc -aes-256-cbc -a -d -pass pass:"这里是我的中文密码" -pbkdf2 -nosalt

# openai proxy base
echo "jH7yECfNgldpYoVFR8GfVOMGzfFESgk5zxalpu8e8Bs=" | openssl enc -aes-256-cbc -a -d -pass pass:"这里是我的中文密码" -pbkdf2 -nosalt

# 加密的命令把上面的 -d 换成 -e 就行
# openssl 的使用详情请看：openssl enc -h

# 如果是 win10 及以上版本的 windows 系统，建议通过 scoop 安装 openssl 进行解密/加密
```
