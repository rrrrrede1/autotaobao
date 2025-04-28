# 示例：用Playwright提取淘宝商品卡片的React Fiber key，即商品ID

from playwright.sync_api import sync_playwright
import time

def main():
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=False)  # headless=False表示打开浏览器界面
        context = browser.new_context()
        page = context.new_page()

        # 1. 登录淘宝
        page.goto("https://login.taobao.com/")
        input("请完成登录后按回车继续...")  # 手动登录

        # 2. 进入指定店铺
        page.goto("https://shop111052165.taobao.com/")
        time.sleep(5)  # 等待页面加载

        # 3. 查询所有商品卡片元素
        elements = page.query_selector_all('.cardContainer--CwazTl0O')

        # 4. 遍历每个卡片，提取其React Fiber Key
        for element in elements:
            react_fiber_key = element.evaluate('''
                (node) => {
                    for (let key in node) {
                        if (key.startsWith("__reactFiber$")) {
                            return node[key] && node[key].key ? node[key].key : null;
                        }
                    }
                    return null;
                }
            ''')
            if react_fiber_key:
                # 保留前12位字符（后面的字符是商品序号，这里我们不需要）
                print(str(react_fiber_key)[:12])

        # 5. 保持页面不关闭
        time.sleep(600)

if __name__ == "__main__":
    main()
