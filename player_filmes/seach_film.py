# type: ignore
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    if options is not None:
        chrome_options = webdriver.ChromeOptions()
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(
        service= chrome_service,
        options= chrome_options,
        )
    return chrome_browser

def make_button(driver, CSS):
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,CSS)
        )
    )
    return button

def search(serie, email, password, tempo):
    TIME_TO_WAIT = tempo
    options = ("--start-maximized",)
    browser = make_chrome_browser(*options)
    browser.get('https://www.max.com/br/')

    
    aceitar_cookies = make_button(browser, "#onetrust-accept-btn-handler")
    aceitar_cookies.click()

    button = browser.find_elements(By.CSS_SELECTOR,'#header-nav')
    entrar = button[3]
    entrar.click()
    
    elemento_com_shadow = make_button(browser, '#app > div.StyledPageContainer-Beam-Web-User__sc-6hfijb-0.lbeabk > div > div.StyledPageBodyContainer-Beam-Web-User__sc-6hfijb-2.HolsJ.skipNavFocusable > div.StyledPageContentWrapper-Beam-Web-User__sc-6hfijb-3.tZvxf > gi-login-username-and-mvpd')

    script = "return arguments[0].shadowRoot"
    shadow_root = browser.execute_script(
        script,
        elemento_com_shadow
    )
    
    elemento_com_shadow_2 = make_button(shadow_root, 'div > div > div.login-username-container > div > gi-login-username')

    shadow_root_2= browser.execute_script(
        script,
        elemento_com_shadow_2
    )

    input_username = make_button(shadow_root_2 ,'#login-username-input')
    input_password = make_button(shadow_root_2, '#login-password-input')
    input_username.send_keys(email)
    input_password.send_keys(password)
    input_password.send_keys(Keys.ENTER)

    acessar_perfil = make_button(browser,'#layer-root-app-content > div.LayoutContentWrapper-Beam-Web-Ent__sc-v8sfp9-0.cCtVum > main > div > div.StyledProfilePickerSection-Beam-Web-Ent__sc-h1h161-2.kbUnzc > div:nth-child(1) > button > div > div > div.StyledAvatarContainer-Beam-Web-Ent__sc-1td0ui1-8.icvmck > img')
    acessar_perfil.click()

    pesquisa = make_button(browser,'#layer-root-app-content > div.LayoutContentWrapper-Beam-Web-Ent__sc-v8sfp9-0 > nav > div.StyledNavRightContainer-Beam-Web-Ent__sc-19tahja-4.crpeDe > a:nth-child(1)')
    pesquisa.click()

    informar_serie = make_button(browser, '#restoration_container > section > div > input')
    informar_serie.send_keys(serie)
    sleep(2)
    informar_serie.send_keys(Keys.ENTER)

    resultados_pesquisa = make_button(browser, '#restoration_container > div:nth-child(3) > section')
    links_resultado = WebDriverWait(resultados_pesquisa,20).until(
        EC.presence_of_all_elements_located(
            (By.TAG_NAME, 'a')
        )
    )
    link1 = links_resultado[0]
    link1.click()

    try: 
        player = make_button(browser, '#restoration_container > section.StyledMainContainer-Beam-Web-Ent__sc-odbkq-0.jJWfut.StyledHero-Beam-Web-Ent__sc-1060yse-0.jgKEEV > div:nth-child(2) > div > div > div > div > div.StyledButtonRowWrapper-Beam-Web-Ent__sc-1kctvbk-0.gaIyau > div.StyledButtonsWrapper-Beam-Web-Ent__sc-1gl4wj-2.dBkzEp.StyledButtonRow-Beam-Web-Ent__sc-1kctvbk-1.mNNif > button.StyledButton-Beam-Web-Ent__sc-14xy2rk-0.emdCBM.StyledPrimaryGroupButton-Beam-Web-Ent__sc-ad2ws6-0.irZrww.skipNavFocusable')
        player.click()
        
    except:
        try:
            player = make_button(browser, '#restoration_container > section.StyledMainContainer-Beam-Web-Ent__sc-odbkq-0.jJWfut.StyledHero-Beam-Web-Ent__sc-1060yse-0.jgKEEV > div:nth-child(2) > div > div > div > div > div.StyledButtonRowWrapper-Beam-Web-Ent__sc-1kctvbk-0.gaIyau > div.StyledButtonsWrapper-Beam-Web-Ent__sc-1gl4wj-2.dBkzEp.StyledButtonRow-Beam-Web-Ent__sc-1kctvbk-1.mNNif > button')
            player.click()
        except:
            print('ERRO AO DAR PLAY NO VÍDEO')
    sleep(5)

    move_mouse = ActionChains(browser)
    move_mouse.move_by_offset(10,10).perform()
    sleep(2)

    full_screen = make_button(browser, '#overlay-root > div:nth-child(4) > div > div.ControlsContainer-Beam-Web-Ent__sc-1la552d-1.byFmvQ > div.ControlsFooter-Beam-Web-Ent__sc-1la552d-9.hWpeaK > div.ControlsFooterBottom-Beam-Web-Ent__sc-1la552d-11.fjfAHS > div.ControlsFooterBottomRight-Beam-Web-Ent__sc-1la552d-15.dfDLDT > button:nth-child(3) > svg')
    full_screen.click()
 
    sleep(TIME_TO_WAIT)
    return 
    