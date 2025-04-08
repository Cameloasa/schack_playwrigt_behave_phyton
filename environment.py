from playwright.sync_api import sync_playwright

def before_all(context):
    print("before_all rulat")
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    context.browser = context.browser_type.launch(headless=True)

def before_scenario(context, scenario):
    print("before_scenario rulat")
    context.page = context.browser.new_page()
    context.base_url = "https://forverkliga.se/JavaScript/whose-turn/"
    print("base_url setat:", context.base_url)  # Mutat după setare

def after_scenario(context, scenario):
    print("after_scenario rulat")
    if hasattr(context, 'page') and context.page:  # Verificăm dacă page există
        context.page.close()

def after_all(context):
    print("after_all rulat")
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()