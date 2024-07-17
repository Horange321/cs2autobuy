# cs2 autobuy

由于 Counter-Strike 2 中的自动购买功能不够好使，便有了这个项目。


## 运行方式
1. 复制项目
```shell
git clone https://github.com/Horange321/cs2autobuy
```

2. 安装 Python（需要pip）

3. 安装依赖 \
**注意：`pytorch` 的安装请参考[官网步骤](https://pytorch.org/get-started/locally/)，否则没有显卡加速。** \
然后补全剩余依赖
```shell
pip install -r requirements.txt
```

4. 配置文件\
请修改 `autobuy.yml`。[有关说明](autobuy.yml)在

5. 运行
```shell
python3 main.py
```
或者
```shell
chmod +x main.py
./main.py
```

6. （可选）如果需要打包单文件版
```shell
pip install pyinstaller
pyinstaller -F -c main.py
```
输出文件在 `dist/main`


## 使用方式
需要使用时直接按下 `Hotkey`。程序会自动获得当前资金、阵营。
### 注意
1. 需要将游戏内快捷键删除
2. 不要打开购买界面。程序会自动打开
