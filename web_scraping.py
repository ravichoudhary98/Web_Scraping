from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

df = pd.DataFrame()
category = 'enterprises'


site_list = ['http://designspiration.net/image/31711833267/',
             'http://tatobutori.prosite.com/182824/6788722/work/honda-motorcycles-maze',
             'https://www.behance.net/gallery/20914789/Ford-Rear-View-Camera-Print-Ads',
             'https://www.behance.net/gallery/10641505/Alzheimers-Disease-International',
             'http://adsoftheworld.com/media/print/belgian_league_of_alhzeimer_alhzeimers_day',
             'https://www.behance.net/gallery/509295/CARULLA-Knives',
             'http://theinspirationgrid.com/better-by-bike-posters-by-la-comunidad/',
             'https://www.behance.net/gallery/10183083/Nutella-Ad-Campaign',
             'http://designtaxi.com/news/367481/Clever-Sharpie-Print-Ads-Show-How-Great-Logos-Were-Started/',
             'https://www.behance.net/gallery/8263139/Aspirina-Bayer',
             'https://www.behance.net/gallery/PARISLOFT-ADVERTISING/1748942',
             'http://thisisnthappiness.com/post/36674956083/i-believe-in-advertising',
             'https://www.behance.net/gallery/28426457/Faber-Castell-Idea-Print-Campaign',
             'https://www.behance.net/gallery/Softies/8296169',
             'http://www.bitrebels.com/design/retro-game-posters-highlight-environmental-issues/',
             'https://www.canva.com/signup?signupRedirect=%2Fdesign%3Fcreate%3Dtrue%26media%3DMACNwt8s9f0&loginRedirect=%2Fdesign%3Fcreate%3Dtrue%26media%3DMACNwt8s9f0',
             'https://www.behance.net/gallery/18726717/PRINT-Pins-El-Universo',
             'http://www.hvilshoj.com/146176/5755745/portfolio/eva-solo-instagram-02',
             'http://www.gqmagazine.fr/culture-web/le-topito-de-la-semaine/diaporama/les-plus-belles-publicits-minimalistes/2045#7',
             'https://www.behance.net/gallery/7283785/Distronic-Plus-Mercedes-Benz',
             'https://www.behance.net/gallery/28144801/Cut-A-Tree-Kill-A-Life',
             'https://www.behance.net/gallery/25707573/FOXY-Asso-Ultra-Glass',
             'https://www.behance.net/gallery/16197577/MARSHALL-HEADPHONES-CANNES-YOUNG-LIONS-UKRAINE',
             'http://www.inspiration-now.com/miyabi-ads-by-herezie-paris/',
             'http://www.inspiration-now.com/inglorious-fruits-vegetables-by-marcel-paris/',
             'http://designbeep.com/2011/10/29/25-fresh-examples-of-effective-ad-campaigns/',
             'https://www.behance.net/gallery/4139709/Pringles-Galaxy',
             'http://www.luerzersarchive.com/en/features/campaigns/your-favourite-print-ads-of-2014-739.html',
             'https://www.behance.net/gallery/10065759/Strawberry-Fanta',
             'http://adsoftheworld.com/media/print/raid_bug_killer_bumblebee',
             'http://www.mylittlerecettes.com/de-jolis-thes-aromatises/',
             'http://www.adweek.com/adfreak/ikeas-family-tree-ads-show-beds-which-each-new-generation-was-conceived-157659',
             'http://www.luerzersarchive.com/en/magazine/print-detail/mccann-healthcare-worldwide-japan-inc-46499.html',
             'http://www.kickvick.com/genius-double-page-magazine-ads/',
             'http://www.kickvick.com/genius-double-page-magazine-ads/',
             'http://www.fromupnorth.com/creative-advertising-1228/',
             'http://www.unp.me/f44/extremely-clever-ads-80425/index2.html',
             'http://www.arnoldfurnace.com/creative/work/bees',
             'https://daviddoctorrose.wordpress.com/2008/02/16/an-extra-large-coffee-from-mcdonalds/',
             'http://www.cuded.com/2012/01/plant-for-the-planet-traffic/',
             'http://www.fromupnorth.com/creative-advertising-673/',
             'http://www.creativebloq.com/inspiration/print-ads-1233780',
             'https://www.behance.net/gallery/University-Cruzeiro-do-Sul-Visagism/9760617',
             'http://www.creativebloq.com/inspiration/print-ads-1233780',
             'http://guff.com/some-of-the-most-clever-advertisements-by-popular-brands/cd-usb-drive',
             'http://www.creativebloq.com/inspiration/print-ads-1233780',
             'https://www.behance.net/gallery/10891255/TazoExplore-the-World',
             'http://www.coloribus.com/adsarchive/prints/volkswagen-car-parts-a-bad-affects-the-entire-system-2-14400005/',
             'https://www.jwt.com/en/dubai',
             'https://www.behance.net/ethosmtl',
             'https://joepublicunited.co.za/',
             'http://www.lamanostudio.com/',
             'http://www.bartleboglehegarty.com/london/',
             'http://www.davidtheagency.com/',
             ''
    
             ]



driver = webdriver.Chrome(executable_path='/home/acer1/chromedriver')
for site in site_list:
    driver.get(site)
    sleep(5)
    hypertext = driver.find_element_by_tag_name("body").get_attribute('innerHTML')
    text = driver.find_element_by_tag_name("body").get_attribute('innerText')
    df = df.append({'hypertext':hypertext,'text':text,'website':site,'category':category},ignore_index=True)
filename = '/home/acer1/sitedata_enterprises.xls'
writer = pd.ExcelWriter(filename, engine='xlsxwriter')
df.to_excel(writer)
writer.save()
driver.close()
