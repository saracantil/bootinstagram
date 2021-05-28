from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="G:\geckodriver-v0.26.0-win64\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/emailsignup/")
        time.sleep(10)
        botao_login = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        botao_login.click()
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(10)

        driver.get("https://www.instagram.com/p/B--j7n9lTcM/")

        comentarios = [
                "@saracantil,@p.goncalvesoficial,@emagrecendo_com_catatau,@jeff.wolf_,danielneves__",
                "@@rafaelrionorte,@capborges.cb,@janaoliveira21,@mariopfernandes,@daviderick.des",
                "@jorgeluis0985,@biancobodybuilder,@babigaluppo,@sindomarsebastiaoda,@renno_gustavo",
                "@prof.gil_aron,@luana.roch,@thalia.teixeiraofc,@miltonsantos613,@daieneapm1_personal",
                "@maykon_master_corte,@victoreletuo,@will_boliveira,@rian.borge,@iara.marta.39",
                "@gildvanalmeidaoliveira,@eu.gui_santosss,@psicologa.malvina,@carlos_eduardopvd,@esheleysantiago",
                "@ricardo522896,@dra.taynahdaeski,@clarck_sv,@ederivancosta,@gleyson.mutante.santos",
                "@elian.ferreira.16,@vanessa.rocha18,@lipe_navaro,@thegeh.barros,@zeliagamel",
                "@reginaldo_fit_oficial,@marcel_souza_1023,@fabiobarnardo,@qgustavo29,@javiteayuda",
                "@daiane.sales.731572,@guilherme.rafael.526,@hugopereiraalbuquerque,@renato.skull,@lizandro_herbert",
                "@dcgrippe,@valdaianefidelis,@day_fit_maromba,@douglas_caldas1,@trainer_maik.oficial",
                "@jarinadosanjos,@aliciaperez947,@guiaguena,@felixkennedydavid,@pessoa7076",
                "@daniguedes7,@carlosaugustofeitosapereira,@andreluizbeniciodossantos,@rf_digaao,@mychael_5",
                "@walmir_jr13,@viivipinheiro,@10011997p,@daianisouza3,@carlinhosssoficial",
                "@luiscgp_,@ruyllerdapaz,@cibelemendesmatheus,@leogomesfreire,@vitinhoo_silvaa01",
                "@susana_seller,@luishenriquedefan,@valeriowitti,@lucassouza9582,@bruno.silva.guimaraes.31",
                "@jonatasoliveira2020,@oficialmatheus013,@pedro_oliveira1319,@paulo.sipriano.589,@mayconmarombafbr",
                "@miliy_siilvaa,@alexepatty22,@anto.salc,@brunnopers0nal_,@wellingtonssdejesus",
                "@f.dc.o,@samuraylopesda,@valdenizioalmeida12,@mario__andreotti,@eu.alvarosilva",
                "@michel.mk.s,@paulo_psos,@carlosguisilva,@emerson.santos557,@fidelisgonthier",
                "@jao_dsouza,@alex_severiano,@felipe_soares0_,@gladiador._,@mayckgrego",
                "@rodrigobastos27,@rjoaootavio,@thiagocosta1392,@ocsamson,@dianaairesrocha",
                "@neguinhoshoww,@wagnerbodystrong,@bezerra0505,@tiagomateusveiga,@alcir_ngmtr",
                "@robert_silva_ofcl,@netomaromba,@luissauer.atleta,@junior.mesquita.50767,@thi.physique",
                "@alexandre_felint,@_grazyx_,@luana_pereira2004,@flavio_as,@danielalmeida8308",
                "@lhbatera,@gabrirl_kn,@pedropagni,@elton.sorato30,@amilton_222",
                "@gabrielteixeira2.0,@cryslian_venancio,@osi.fitnes,@indio__21,@kennedy_ascadasa",
        ]
 
        try:
            for sText in comentarios:    
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentarios = driver.find_element_by_class_name('Ypffh')
                time.sleep(10)
                campo_comentarios.send_keys(sText)
                time.sleep(10)
                campo_comentarios.send_keys(Keys.SPACE)
                time.sleep(10)
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(72)

        except Exception as e:
            print(e)
            time.sleep(10)

jhonatanBot = InstagramBot("","")
jhonatanBot.login()

