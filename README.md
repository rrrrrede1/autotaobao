# 有需要可以联系闲鱼同名rrrrrede1
# 淘宝商品卡片提取工具

这是一个使用 **Playwright** 自动化提取淘宝店铺商品卡片中商品ID的简单脚本。

## 安装方法

1. 安装 Python 3.8+
2. 安装依赖：
   ```bash
   pip install playwright
   playwright install
   ```

3. 将本项目的 `example.py` 文件保存到本地。

## 使用方法

1. 运行脚本：
   ```bash
   python example.py
   ```

2. 浏览器会自动打开淘宝登录页，请**手动扫码登录**或**输入账号密码登录**。
   
3. 登录完成后，回到控制台，按下回车键继续。

4. 程序会自动跳转到目标店铺，提取商品卡片ID，并在终端输出。

5. 浏览器会保持打开状态 10 分钟，供手动查看或调试。

## 注意事项

- **首次使用 Playwright** 时，执行 `playwright install` 下载浏览器驱动。
- 本脚本不包含自动登录功能，需**手动完成淘宝登录**。
- 如果店铺页面结构变动（比如类名 `.cardContainer--CwazTl0O` 变化），需要手动调整脚本里的类名选择器。

## 示例输出

```text
682878295322
682878295323
682878295324
...
```

每一行代表一个商品的唯一识别号（截取前12位）。

## 还原链接

   ```text
   https://detail.tmall.com/item.htm?id={id}
   https://item.taobao.com/item.htm?id={id}
   ```

在{id}处填上商品ID即可，看具体情况分为淘宝和天猫店铺进行填写。

# 许可证

本项目采用 **[GNU Affero General Public License v3.0](https://www.gnu.org/licenses/agpl-3.0.html)** 许可证，任何人都可以自由使用、修改和分发本项目的代码，但有以下限制：

1. 你必须将所有修改的代码以相同的 AGPL 许可证开源
2. 如果你在网络服务中运行该项目的修改版，必须向所有访问该服务的用户提供源代码

详见 [LICENSE 文件](./LICENSE)
