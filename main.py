from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import asyncio
import aiohttp
from pyvirtualdisplay import Display
from sys import platform
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from os import system
from sqlighter import SQLighter
import random

# token = '' #testbot


token = '' #timetable_RGU_Gubkina_bot


bot = Bot(token)
dp = Dispatcher(bot)
db = SQLighter('db.db')


get_btn = KeyboardButton('Получить расписание')
settings_btn = KeyboardButton('Настройки')
start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_kb.add(get_btn, settings_btn)


week_btn_1 = InlineKeyboardButton('предыдущая', callback_data='previous')
week_btn_2 = InlineKeyboardButton('текущая', callback_data='center')
week_btn_3 = InlineKeyboardButton('следующая', callback_data='next')
week_choose_kb = InlineKeyboardMarkup().add(week_btn_1, week_btn_2, week_btn_3)


settings_btn_1 = InlineKeyboardButton('неделя ❌', callback_data='week_save')
settings_btn_1_saved = InlineKeyboardButton('неделя ✅', callback_data='week_saved')
settings_btn_2 = InlineKeyboardButton('факультет ❌', callback_data='fack_save')
settings_btn_2_saved = InlineKeyboardButton('факультет ✅', callback_data='fack_saved')
settings_btn_3 = InlineKeyboardButton('группа ❌', callback_data='group_save')
settings_btn_3_saved = InlineKeyboardButton('группа✅', callback_data='group_saved')


inline_btn_kbtek = InlineKeyboardButton('КБТЭК', callback_data='kbtek')
inline_btn_avt = InlineKeyboardButton('АВТ', callback_data='avt')
inline_btn_ggng = InlineKeyboardButton('ГГНГ', callback_data='ggng')
inline_btn_im = InlineKeyboardButton('ИМ', callback_data='im')
inline_btn_meb = InlineKeyboardButton('МЭБ', callback_data='meb')
inline_btn_pseptt = InlineKeyboardButton('ПСЭПТТ', callback_data='pseptt')
inline_btn_rngm = InlineKeyboardButton('РНГМ', callback_data='rngm')
inline_btn_hte = InlineKeyboardButton('ХТЭ', callback_data='hte')
inline_btn_ey = InlineKeyboardButton('ЭУ', callback_data='ey')
inline_btn_yu = InlineKeyboardButton('Ю', callback_data='yu')
fk_choice_kb = InlineKeyboardMarkup().add(inline_btn_kbtek, inline_btn_avt, inline_btn_ggng, inline_btn_im, inline_btn_meb, inline_btn_pseptt, inline_btn_rngm, inline_btn_hte, inline_btn_ey, inline_btn_yu)


inline_btn_ka_18_01 = InlineKeyboardButton('ка-18-01', callback_data='ка-18-01')
inline_btn_ka_19_03 = InlineKeyboardButton('ка-19-03', callback_data='ка-19-03')
inline_btn_ka_20_03 = InlineKeyboardButton('ка-20-03', callback_data='ка-20-03')
inline_btn_kb_18_01 = InlineKeyboardButton('кб-18-01', callback_data='кб-18-01')
inline_btn_kb_19_10 = InlineKeyboardButton('кб-19-10', callback_data='кб-19-10')
inline_btn_kb_20_07 = InlineKeyboardButton('кб-20-07', callback_data='кб-20-07')
inline_btn_kv_20_04 = InlineKeyboardButton('кв-20-04', callback_data='кв-20-04')
inline_btn_ki_18_01 = InlineKeyboardButton('ки-18-01', callback_data='ки-18-01')
inline_btn_ki_19_01 = InlineKeyboardButton('ки-19-01', callback_data='ки-19-01')
inline_btn_ki_20_01 = InlineKeyboardButton('ки-20-01', callback_data='ки-20-01')
inline_btn_km_19_05 = InlineKeyboardButton('км-19-05', callback_data='км-19-05')
inline_btn_km_19_11 = InlineKeyboardButton('км-19-11', callback_data='км-19-11')
inline_btn_km_20_10 = InlineKeyboardButton('км-20-10', callback_data='км-20-10')
inline_btn_km_20_11 = InlineKeyboardButton('км-20-11', callback_data='км-20-11')
inline_btn_km_20_12 = InlineKeyboardButton('км-20-12', callback_data='км-20-12')
inline_btn_kr_19_07 = InlineKeyboardButton('кр-19-07', callback_data='кр-19-07')
inline_btn_kr_20_09 = InlineKeyboardButton('кр-20-09', callback_data='кр-20-09')
inline_btn_ks_19_04 = InlineKeyboardButton('кс-19-04', callback_data='кс-19-04')
inline_btn_ks_20_05 = InlineKeyboardButton('кс-20-05', callback_data='кс-20-05')
inline_btn_kf_19_02 = InlineKeyboardButton('кф-19-02', callback_data='кф-19-02')
inline_btn_kf_20_02 = InlineKeyboardButton('кф-20-02', callback_data='кф-20-02')
inline_btn_kc_19_09 = InlineKeyboardButton('кц-19-02', callback_data='кц-19-02')
inline_btn_ke_18_01 = InlineKeyboardButton('кэ-18-01', callback_data='кэ-18-01')
inline_btn_ke_18_02 = InlineKeyboardButton('кэ-18-02', callback_data='кэ-18-02')
inline_btn_ke_19_08 = InlineKeyboardButton('кэ-19-08', callback_data='кэ-19-08')
inline_btn_ke_20_06 = InlineKeyboardButton('кэ-20-06', callback_data='кэ-20-06')
inline_btn_ku_18_01 = InlineKeyboardButton('кю-18-01', callback_data='кю-18-01')
inline_btn_ku_19_06 = InlineKeyboardButton('кю-19-06', callback_data='кю-19-06')
inline_btn_ku_20_08 = InlineKeyboardButton('кю-20-08', callback_data='кю-20-08')
inline_btn_ef_17_05 = InlineKeyboardButton('эф-17-05', callback_data='эф-17-05')
inline_btn_ef_17_06 = InlineKeyboardButton('эф-17-06', callback_data='эф-17-06')
group_kbtek_kb = InlineKeyboardMarkup().add(inline_btn_ka_18_01, inline_btn_ka_19_03, inline_btn_ka_20_03, inline_btn_kb_18_01, inline_btn_kb_19_10, inline_btn_kb_20_07, inline_btn_kv_20_04, inline_btn_ki_18_01, inline_btn_ki_19_01, inline_btn_ki_20_01, inline_btn_km_19_05, inline_btn_km_19_11, inline_btn_km_20_10, inline_btn_km_20_11, inline_btn_km_20_12, inline_btn_kr_19_07, inline_btn_kr_20_09, inline_btn_ks_19_04, inline_btn_ks_20_05, inline_btn_kf_19_02, inline_btn_kf_20_02, inline_btn_kc_19_09, inline_btn_ke_18_01, inline_btn_ke_18_02, inline_btn_ke_19_08, inline_btn_ke_20_06, inline_btn_ku_18_01, inline_btn_ku_19_06, inline_btn_ku_20_08, inline_btn_ef_17_05, inline_btn_ef_17_06)


kbtek = {
	'ка-18-01'	: '21&groupId=5165',
	'ка-19-03'	: '21&groupId=6420',
	'ка-20-03'	: '21&groupId=7424',
	'кб-18-01'	: '21&groupId=5187',
	'кб-19-10'	: '21&groupId=6425',
	'кб-20-07'	: '21&groupId=7427',
	'кв-20-04'	: '21&groupId=7425',
	'ки-18-01'	: '21&groupId=5164',
	'ки-19-01'	: '21&groupId=6418',
	'ки-20-01'	: '21&groupId=7394',
	'км-19-05'	: '21&groupId=6417',
	'км-19-11'	: '21&groupId=6809',
	'км-20-10'	: '21&groupId=7430',
	'км-20-11'	: '21&groupId=7606',
	'км-20-12'	: '21&groupId=7607',
	'кр-19-07'	: '21&groupId=6416',
	'кр-20-09'	: '21&groupId=7429',
	'кс-19-04'	: '21&groupId=6421',
	'кс-20-05'	: '21&groupId=7426',
	'кф-19-02'	: '21&groupId=6419',
	'кф-20-02'	: '21&groupId=7395',
	'кц-19-09'	: '21&groupId=6424',
	'кэ-18-01'	: '21&groupId=5185',
	'кэ-18-02'	: '21&groupId=5186',
	'кэ-19-08'	: '21&groupId=6423',
	'кэ-20-06'	: '21&groupId=7440',
	'кю-18-01'	: '21&groupId=5543',
	'кю-19-06'	: '21&groupId=6422',
	'кю-20-08'	: '21&groupId=7428',
	'эф-17-05'	: '21&groupId=4666',
	'эф-17-06'	: '21&groupId=4667',
}


inline_btn_bm_16_03 = InlineKeyboardButton('бм-16-03' , callback_data='бм-16-03')
inline_btn_bm_17_03 = InlineKeyboardButton('бм-17-03' , callback_data='бм-17-03')
inline_btn_bm_17_04 = InlineKeyboardButton('бм-17-04' , callback_data='бм-17-04')
inline_btn_bm_18_03 = InlineKeyboardButton('бм-18-03' , callback_data='бм-18-03')
inline_btn_bm_18_04 = InlineKeyboardButton('бм-18-04' , callback_data='бм-18-04')
inline_btn_bm_19_03 = InlineKeyboardButton('бм-19-03' , callback_data='бм-19-03')
inline_btn_bm_19_04 = InlineKeyboardButton('бм-19-04' , callback_data='бм-19-04')
inline_btn_bm_20_03 = InlineKeyboardButton('бм-20-03' , callback_data='бм-20-03')
inline_btn_bm_20_04 = InlineKeyboardButton('бм-20-04' , callback_data='бм-20-04')
inline_btn_bmm_19_03 = InlineKeyboardButton('бмм-19-03', callback_data='бмм-19-03')
inline_btn_bmm_19_04 = InlineKeyboardButton('бмм-19-04', callback_data='бмм-19-04')
inline_btn_bmm_19_05 = InlineKeyboardButton('бмм-19-05', callback_data='бмм-19-05')
inline_btn_bmm_19_06 = InlineKeyboardButton('бмм-19-06', callback_data='бмм-19-06')
inline_btn_bmm_20_03 = InlineKeyboardButton('бмм-20-03', callback_data='бмм-20-03')
inline_btn_bmm_20_04 = InlineKeyboardButton('бмм-20-04', callback_data='бмм-20-04')
inline_btn_bmm_20_05 = InlineKeyboardButton('бмм-20-05', callback_data='бмм-20-05')
inline_btn_bmm_20_06 = InlineKeyboardButton('бмм-20-06', callback_data='бмм-20-06')
inline_btn_be_17_01 = InlineKeyboardButton('бэ-17-01' , callback_data='бэ-17-01')
inline_btn_be_17_02 = InlineKeyboardButton('бэ-17-02' , callback_data='бэ-17-02')
inline_btn_be_18_01 = InlineKeyboardButton('бэ-18-01' , callback_data='бэ-18-01')
inline_btn_be_18_02 = InlineKeyboardButton('бэ-18-02' , callback_data='бэ-18-02')
inline_btn_be_19_01 = InlineKeyboardButton('бэ-19-01' , callback_data='бэ-19-01')
inline_btn_be_19_02 = InlineKeyboardButton('бэ-19-02' , callback_data='бэ-19-02')
inline_btn_be_20_01 = InlineKeyboardButton('бэ-20-01' , callback_data='бэ-20-01')
inline_btn_be_20_02 = InlineKeyboardButton('бэ-20-02' , callback_data='бэ-20-02')
inline_btn_bem_19_01 = InlineKeyboardButton('бэм-19-01', callback_data='бэм-19-01')
inline_btn_bem_20_01 = InlineKeyboardButton('бэм-20-01', callback_data='бэм-20-01')
inline_btn_bem_20_02 = InlineKeyboardButton('бэм-20-02', callback_data='бэм-20-02')
inline_btn_vmm_18_12 = InlineKeyboardButton('вмм-18-12', callback_data='вмм-18-12')
inline_btn_vmm_19_12 = InlineKeyboardButton('вмм-19-12', callback_data='вмм-19-12')
inline_btn_vmm_19_15 = InlineKeyboardButton('вмм-19-15', callback_data='вмм-19-15')
inline_btn_vmm_20_12 = InlineKeyboardButton('вмм-20-12', callback_data='вмм-20-12')
inline_btn_vmm_20_15 = InlineKeyboardButton('вмм-20-15', callback_data='вмм-20-15')
inline_btn_vem_18_07 = InlineKeyboardButton('вэм-18-07', callback_data='вэм-18-07')
inline_btn_vem_18_08 = InlineKeyboardButton('вэм-18-08', callback_data='вэм-18-08')
inline_btn_vem_19_07 = InlineKeyboardButton('вэм-19-07', callback_data='вэм-19-07')
inline_btn_bem_20_07 = InlineKeyboardButton('вэм-20-07', callback_data='вэм-20-07')
group_meb_kb = InlineKeyboardMarkup().add(inline_btn_bm_16_03, inline_btn_bm_17_03, inline_btn_bm_17_04, inline_btn_bm_18_03, inline_btn_bm_18_04, inline_btn_bm_19_03, inline_btn_bm_19_04, inline_btn_bm_20_03, inline_btn_bm_20_04, inline_btn_bmm_19_03, inline_btn_bmm_19_04, inline_btn_bmm_19_05, inline_btn_bmm_19_06, inline_btn_bmm_20_03, inline_btn_bmm_20_04, inline_btn_bmm_20_05, inline_btn_bmm_20_06, inline_btn_be_17_01, inline_btn_be_17_02, inline_btn_be_18_01, inline_btn_be_18_02, inline_btn_be_19_01, inline_btn_be_19_02, inline_btn_be_20_01, inline_btn_be_20_02, inline_btn_bem_19_01, inline_btn_bem_20_01, inline_btn_bem_20_02, inline_btn_vmm_18_12, inline_btn_vmm_19_12, inline_btn_vmm_19_15, inline_btn_vmm_20_12, inline_btn_vmm_20_15, inline_btn_vem_18_07, inline_btn_vem_18_08, inline_btn_vem_19_07, inline_btn_bem_20_07)


meb = {
    'бм-16-03'  : '12&groupId=3068',
    'бм-17-03'  : '12&groupId=4646',
    'бм-17-04'  : '12&groupId=4647',
    'бм-18-03'  : '12&groupId=5173',
    'бм-18-04'  : '12&groupId=5174',
    'бм-19-03'  : '12&groupId=6480',
    'бм-19-04'  : '12&groupId=6481',
    'бм-20-03'  : '12&groupId=6969',
    'бм-20-04'  : '12&groupId=6970',
    'бмм-19-03' : '12&groupId=6484',
    'бмм-19-04' : '12&groupId=6485',
    'бмм-19-05' : '12&groupId=6500',
    'бмм-19-06' : '12&groupId=6501',
    'бмм-20-03' : '12&groupId=6971',
    'бмм-20-04' : '12&groupId=6972',
    'бмм-20-05' : '12&groupId=6976',
    'бмм-20-06' : '12&groupId=6973',
    'бэ-17-01'  : '12&groupId=4644',
    'бэ-17-02'  : '12&groupId=4645',
    'бэ-18-01'  : '12&groupId=5169',
    'бэ-18-02'  : '12&groupId=5172',
    'бэ-19-01'  : '12&groupId=6478',
    'бэ-19-02'  : '12&groupId=6479',
    'бэ-20-01'  : '12&groupId=6967',
    'бэ-20-02'  : '12&groupId=6968',
    'бэм-19-01' : '12&groupId=6482',
    'бэм-20-01' : '12&groupId=6974',
    'бэм-20-02' : '12&groupId=6975',
    'вмм-18-12' : '12&groupId=5031',
    'вмм-19-12' : '12&groupId=6498',
    'вмм-19-15' : '12&groupId=6507',
    'вмм-20-12' : '12&groupId=7449',
    'вмм-20-15' : '12&groupId=7450',
    'вэм-18-07' : '12&groupId=5027',
    'вэм-18-08' : '12&groupId=5770',
    'вэм-19-07' : '12&groupId=6438',
    'вэм-20-07' : '12&groupId=7436'
}


inline_btn_aa_17_05 = InlineKeyboardButton('аа-17-05', callback_data='аа-17-05')
inline_btn_aa_18_05 = InlineKeyboardButton('аа-18-05', callback_data='аа-18-05')
inline_btn_aa_19_05 = InlineKeyboardButton('аа-19-05', callback_data='аа-19-05')
inline_btn_aa_20_05 = InlineKeyboardButton('аа-20-05', callback_data='аа-20-05')
inline_btn_ai_17_02 = InlineKeyboardButton('аи-17-02', callback_data='аи-17-02')
inline_btn_ai_18_02 = InlineKeyboardButton('аи-18-02', callback_data='аи-18-02')
inline_btn_ai_19_02 = InlineKeyboardButton('аи-19-02', callback_data='аи-19-02')
inline_btn_ai_20_02 = InlineKeyboardButton('аи-20-02', callback_data='аи-20-02')
inline_btn_aim_19_02 = InlineKeyboardButton('аим-19-02', callback_data='аим-19-02')
inline_btn_aim_20_02 = InlineKeyboardButton('аим-20-02', callback_data='аим-20-02')
inline_btn_am_17_06 = InlineKeyboardButton('ам-17-06', callback_data='ам-17-06')
inline_btn_am_18_06 = InlineKeyboardButton('ам-18-06', callback_data='ам-18-06')
inline_btn_am_19_06 = InlineKeyboardButton('ам-19-06', callback_data='ам-19-06')
inline_btn_am_20_06 = InlineKeyboardButton('ам-20-06', callback_data='ам-20-06')
inline_btn_amm_19_06 = InlineKeyboardButton('амм-19-06', callback_data='амм-19-06')
inline_btn_amm_20_06 = InlineKeyboardButton('амм-20-06', callback_data='амм-20-06')
inline_btn_as_17_04 = InlineKeyboardButton('ас-17-04', callback_data='ас-17-04')
inline_btn_as_18_04 = InlineKeyboardButton('ас-18-04', callback_data='ас-18-04')
inline_btn_as_19_04 = InlineKeyboardButton('ас-19-04', callback_data='ас-19-04')
inline_btn_as_20_04 = InlineKeyboardButton('ас-20-04', callback_data='ас-20-04')
inline_btn_asm_19_04 = InlineKeyboardButton('асм-19-04', callback_data='асм-19-04')
inline_btn_asm_19_05 = InlineKeyboardButton('асм-19-05', callback_data='асм-19-05')
inline_btn_asm_20_04 = InlineKeyboardButton('асм-20-04', callback_data='асм-20-04')
inline_btn_asm_20_05 = InlineKeyboardButton('асм-20-05', callback_data='асм-20-05')
inline_btn_at_17_01 = InlineKeyboardButton('ат-17-01', callback_data='ат-17-01')
inline_btn_at_18_01 = InlineKeyboardButton('ат-18-01', callback_data='ат-18-01')
inline_btn_at_19_01 = InlineKeyboardButton('ат-19-01', callback_data='ат-19-01')
inline_btn_at_20_01 = InlineKeyboardButton('ат-20-01', callback_data='ат-20-01')
inline_btn_atm_19_01 = InlineKeyboardButton('атм-19-01', callback_data='атм-19-01')
inline_btn_atm_20_01 = InlineKeyboardButton('атм-20-01', callback_data='атм-20-01')
inline_btn_ae_17_03 = InlineKeyboardButton('аэ-17-03', callback_data='аэ-17-03')
inline_btn_ae_18_03 = InlineKeyboardButton('аэ-18-03', callback_data='аэ-18-03')
inline_btn_ae_19_03 = InlineKeyboardButton('аэ-19-03', callback_data='аэ-19-03')
inline_btn_ae_20_03 = InlineKeyboardButton('аэ-20-03', callback_data='аэ-20-03')
inline_btn_aem_19_03 = InlineKeyboardButton('аэм-19-03', callback_data='аэм-19-03')
inline_btn_aem_20_03 = InlineKeyboardButton('аэм-20-03', callback_data='аэм-20-03')
group_avt_kb = InlineKeyboardMarkup().add(inline_btn_aa_17_05, inline_btn_aa_18_05, inline_btn_aa_19_05, inline_btn_aa_20_05, inline_btn_ai_17_02, inline_btn_ai_18_02, inline_btn_ai_19_02, inline_btn_ai_20_02, inline_btn_aim_19_02, inline_btn_aim_20_02, inline_btn_am_17_06, inline_btn_am_18_06, inline_btn_am_19_06, inline_btn_am_20_06, inline_btn_amm_19_06, inline_btn_amm_20_06, inline_btn_as_17_04, inline_btn_as_18_04, inline_btn_as_19_04, inline_btn_as_20_04, inline_btn_asm_19_04, inline_btn_asm_19_05, inline_btn_asm_20_04, inline_btn_asm_20_05, inline_btn_at_17_01, inline_btn_at_18_01, inline_btn_at_19_01, inline_btn_at_20_01, inline_btn_atm_19_01, inline_btn_atm_20_01, inline_btn_ae_17_03, inline_btn_ae_18_03, inline_btn_ae_19_03, inline_btn_ae_20_03, inline_btn_aem_19_03, inline_btn_aem_20_03)


avt = {
	'аа-17-05' : "5&groupId=4592",
	'аа-18-05' : "5&groupId=5550",
	'аа-19-05' : "5&groupId=6541",
	'аа-20-05' : "5&groupId=7022",
	'аи-17-02' : "5&groupId=4589",
	'аи-18-02' : "5&groupId=5091",
	'аи-19-02' : "5&groupId=6527",
	'аи-20-02' : "5&groupId=7019",
	'аим-19-02' : "5&groupId=6559",
	'аим-20-02' : "5&groupId=7025",
	'ам-17-06' : "5&groupId=4591",
	'ам-18-06' : "5&groupId=5132",
	'ам-19-06' : "5&groupId=6529",
	'ам-20-06' : "5&groupId=7023",
	'амм-19-06' : "5&groupId=6533",
	'амм-20-06' : "5&groupId=7029",
	'ас-17-04' : "5&groupId=4522",
	'ас-18-04' : "5&groupId=5551",
	'ас-19-04' : "5&groupId=6539",
	'ас-20-04' : "5&groupId=7021",
	'асм-19-04' : "5&groupId=6542",
	'асм-19-05' : "5&groupId=6553",
	'асм-20-04' : "5&groupId=7027",
	'асм-20-05' : "5&groupId=7028",
	'ат-17-01' : "5&groupId=4585",
	'ат-18-01' : "5&groupId=5090",
	'ат-19-01' : "5&groupId=6518",
	'ат-20-01' : "5&groupId=7018",
	'атм-19-01' : "5&groupId=6530",
	'атм-20-01' : "5&groupId=7024",
	'аэ-17-03' : "5&groupId=4587",
	'аэ-18-03' : "5&groupId=5092",
	'аэ-19-03' : "5&groupId=6528",
	'аэ-20-03' : "5&groupId=7020",
	'аэм-19-03' : "5&groupId=6532",
	'аэм-20-03' : "5&groupId=7026"	
}


inline_btn_gi_16_04 = InlineKeyboardButton('ги-16-04', callback_data='ги-16-04')
inline_btn_gi_17_04 = InlineKeyboardButton('ги-17-04', callback_data='ги-17-04')
inline_btn_gi_17_05 = InlineKeyboardButton('ги-17-05', callback_data='ги-17-05')
inline_btn_gi_18_04 = InlineKeyboardButton('ги-18-04', callback_data='ги-18-04')
inline_btn_gi_19_04 = InlineKeyboardButton('ги-19-04', callback_data='ги-19-04')
inline_btn_gi_20_04 = InlineKeyboardButton('ги-20-04', callback_data='ги-20-04')
inline_btn_gl_18_08 = InlineKeyboardButton('гл-18-08', callback_data='гл-18-08')
inline_btn_gl_19_08 = InlineKeyboardButton('гл-19-08', callback_data='гл-19-08')
inline_btn_gl_20_08 = InlineKeyboardButton('гл-20-08', callback_data='гл-20-08')
inline_btn_gnm_19_01 = InlineKeyboardButton('гнм-19-01', callback_data='гнм-19-01')
inline_btn_gnm_19_02 = InlineKeyboardButton('гнм-19-02', callback_data='гнм-19-02')
inline_btn_gnm_19_03 = InlineKeyboardButton('гнм-19-03', callback_data='гнм-19-03')
inline_btn_gnm_20_01 = InlineKeyboardButton('гнм-20-01', callback_data='гнм-20-01')
inline_btn_gp_16_01 = InlineKeyboardButton('гп-16-01', callback_data='гп-16-01')
inline_btn_gp_16_09 = InlineKeyboardButton('гп-16-09', callback_data='гп-16-09')
inline_btn_gp_17_01 = InlineKeyboardButton('гп-17-01', callback_data='гп-17-01')
inline_btn_gp_18_01 = InlineKeyboardButton('гп-18-01', callback_data='гп-18-01')
inline_btn_gp_18_09 = InlineKeyboardButton('гп-18-09', callback_data='гп-18-09')
inline_btn_gp_19_01 = InlineKeyboardButton('гп-19-01', callback_data='гп-19-01')
inline_btn_gp_20_01 = InlineKeyboardButton('гп-20-01', callback_data='гп-20-01')
inline_btn_gp_20_09 = InlineKeyboardButton('гп-20-09', callback_data='гп-20-09')
inline_btn_gr_16_02 = InlineKeyboardButton('гр-16-02', callback_data='гр-16-02')
inline_btn_gr_17_02 = InlineKeyboardButton('гр-17-02', callback_data='гр-17-02')
inline_btn_gr_17_07 = InlineKeyboardButton('гр-17-07', callback_data='гр-17-07')
inline_btn_gr_18_02 = InlineKeyboardButton('гр-18-02', callback_data='гр-18-02')
inline_btn_gr_19_02 = InlineKeyboardButton('гр-19-02', callback_data='гр-19-02')
inline_btn_gr_19_07 = InlineKeyboardButton('гр-19-07', callback_data='гр-19-07')
inline_btn_gr_20_02 = InlineKeyboardButton('гр-20-02', callback_data='гр-20-02')
inline_btn_gf_15_03 = InlineKeyboardButton('гф-15-03', callback_data='гф-15-03')
inline_btn_gf_16_03 = InlineKeyboardButton('гф-16-03', callback_data='гф-16-03')
inline_btn_gf_17_03 = InlineKeyboardButton('гф-17-03', callback_data='гф-17-03')
inline_btn_gf_18_03 = InlineKeyboardButton('гф-18-03', callback_data='гф-18-03')
inline_btn_gf_19_03 = InlineKeyboardButton('гф-19-03', callback_data='гф-19-03')
inline_btn_gf_20_03 = InlineKeyboardButton('гф-20-03', callback_data='гф-20-03')
inline_btn_ge_17_06 = InlineKeyboardButton('гэ-17-06', callback_data='гэ-17-06')
inline_btn_ge_18_06 = InlineKeyboardButton('гэ-18-06', callback_data='гэ-18-06')
inline_btn_ge_19_06 = InlineKeyboardButton('гэ-19-06', callback_data='гэ-19-06')
inline_btn_ge_20_06 = InlineKeyboardButton('гэ-20-06', callback_data='гэ-20-06')
inline_btn_gem_20_03 = InlineKeyboardButton('гэм-20-03', callback_data='гэм-20-03')
group_ggng_kb = InlineKeyboardMarkup().add(inline_btn_gi_16_04, inline_btn_gi_17_04, inline_btn_gi_17_05, inline_btn_gi_18_04, inline_btn_gi_19_04, inline_btn_gi_20_04, inline_btn_gl_18_08, inline_btn_gl_19_08, inline_btn_gl_20_08, inline_btn_gnm_19_01, inline_btn_gnm_19_02, inline_btn_gnm_19_03, inline_btn_gnm_20_01, inline_btn_gp_16_01, inline_btn_gp_16_09, inline_btn_gp_17_01, inline_btn_gp_18_01, inline_btn_gp_18_09, inline_btn_gp_19_01, inline_btn_gp_20_01, inline_btn_gp_20_09, inline_btn_gr_16_02, inline_btn_gr_17_02, inline_btn_gr_17_07, inline_btn_gr_18_02, inline_btn_gr_19_02, inline_btn_gr_19_07, inline_btn_gr_20_02, inline_btn_gf_15_03, inline_btn_gf_16_03, inline_btn_gf_17_03, inline_btn_gf_18_03, inline_btn_gf_19_03, inline_btn_gf_20_03, inline_btn_ge_17_06, inline_btn_ge_18_06, inline_btn_ge_19_06, inline_btn_ge_20_06, inline_btn_gem_20_03)


ggng = {
	'ги-16-04' : "0&groupId=2640",
	'ги-17-04' : "0&groupId=4611",
	'ги-17-05' : "0&groupId=4612",
	'ги-18-04' : "0&groupId=5120",
	'ги-19-04' : "0&groupId=6381",
	'ги-20-04' : "0&groupId=6957",
	'гл-18-08' : "0&groupId=5167",
	'гл-19-08' : "0&groupId=6466",
	'гл-20-08' : "0&groupId=6958",
	'гнм-19-01' : "0&groupId=6543",
	'гнм-19-02' : "0&groupId=6544",
	'гнм-19-03' : "0&groupId=6545",
	'гнм-20-01' : "0&groupId=6959",
	'гп-16-01' : "0&groupId=2637",
	'гп-16-09' : "0&groupId=2638",
	'гп-17-01' : "0&groupId=4613",
	'гп-18-01' : "0&groupId=5116",
	'гп-18-09' : "0&groupId=5118",
	'гп-19-01' : "0&groupId=6463",
	'гп-20-01' : "0&groupId=6960",
	'гп-20-09' : "0&groupId=6962",
	'гр-16-02' : "0&groupId=2639",
	'гр-17-02' : "0&groupId=4614",
	'гр-17-07' : "0&groupId=4615",
	'гр-18-02' : "0&groupId=5117",
	'гр-19-02' : "0&groupId=6464",
	'гр-19-07' : "0&groupId=6465",
	'гр-20-02' : "0&groupId=6961",
	'гф-15-03' : "0&groupId=2436",
	'гф-16-03' : "0&groupId=2642",
	'гф-17-03' : "0&groupId=4610",
	'гф-18-03' : "0&groupId=5119",
	'гф-19-03' : "0&groupId=6382",
	'гф-20-03' : "0&groupId=6963",
	'гэ-17-06' : "0&groupId=4619",
	'гэ-18-06' : "0&groupId=5122",
	'гэ-19-06' : "0&groupId=6503",
	'гэ-20-06' : "0&groupId=6964",
	'гэм-20-03' : "0&groupId=6978"
}


inline_btn_ma_17_07 = InlineKeyboardButton("ма-17-07", callback_data='ма-17-07')
inline_btn_ma_18_07 = InlineKeyboardButton("ма-18-07", callback_data='ма-18-07')
inline_btn_ma_19_03 = InlineKeyboardButton("ма-19-03", callback_data='ма-19-03')
inline_btn_ma_20_03 = InlineKeyboardButton("ма-20-03", callback_data='ма-20-03')
inline_btn_mb_17_08 = InlineKeyboardButton("мб-17-08", callback_data='мб-17-08')
inline_btn_mb_18_08 = InlineKeyboardButton("мб-18-08", callback_data='мб-18-08')
inline_btn_mb_19_08 = InlineKeyboardButton("мб-19-08", callback_data='мб-19-08')
inline_btn_mb_20_07 = InlineKeyboardButton("мб-20-07", callback_data='мб-20-07')
inline_btn_mbm_19_04 = InlineKeyboardButton("мбм-19-04", callback_data='мбм-19-04')
inline_btn_mbm_20_04 = InlineKeyboardButton("мбм-20-04", callback_data='мбм-20-04')
inline_btn_md_17_11 = InlineKeyboardButton("мд-17-11", callback_data='мд-17-11')
inline_btn_md_18_11 = InlineKeyboardButton("мд-18-11", callback_data='мд-18-11')
inline_btn_md_19_01 = InlineKeyboardButton("мд-19-01", callback_data='мд-19-01')
inline_btn_md_20_01 = InlineKeyboardButton("мд-20-01", callback_data='мд-20-01')
inline_btn_mm_17_12 = InlineKeyboardButton("мм-17-12", callback_data='мм-17-12')
inline_btn_mm_18_12 = InlineKeyboardButton("мм-18-12", callback_data='мм-18-12')
inline_btn_mm_19_07 = InlineKeyboardButton("мм-19-07", callback_data='мм-19-07')
inline_btn_mm_20_02 = InlineKeyboardButton("мм-20-02", callback_data='мм-20-02')
inline_btn_mo_16_09 = InlineKeyboardButton("мо-16-09", callback_data='мо-16-09')
inline_btn_mo_16_10 = InlineKeyboardButton("мо-16-10", callback_data='мо-16-10')
inline_btn_mo_17_09 = InlineKeyboardButton("мо-17-09", callback_data='мо-17-09')
inline_btn_mo_17_10 = InlineKeyboardButton("мо-17-10", callback_data='мо-17-10')
inline_btn_mo_18_09 = InlineKeyboardButton("мо-18-09", callback_data='мо-18-09')
inline_btn_mo_18_10 = InlineKeyboardButton("мо-18-10", callback_data='мо-18-10')
inline_btn_mo_19_04 = InlineKeyboardButton("мо-19-04", callback_data='мо-19-04')
inline_btn_mo_19_05 = InlineKeyboardButton("мо-19-05", callback_data='мо-19-05')
inline_btn_mo_20_04 = InlineKeyboardButton("мо-20-04", callback_data='мо-20-04')
inline_btn_mo_20_05 = InlineKeyboardButton("мо-20-05", callback_data='мо-20-05')
inline_btn_mp_16_06 = InlineKeyboardButton("мп-16-06", callback_data='мп-16-06')
inline_btn_mp_17_06 = InlineKeyboardButton("мп-17-06", callback_data='мп-17-06')
inline_btn_mp_18_06 = InlineKeyboardButton("мп-18-06", callback_data='мп-18-06')
inline_btn_mp_19_06 = InlineKeyboardButton("мп-19-06", callback_data='мп-19-06')
inline_btn_mp_20_06 = InlineKeyboardButton("мп-20-06", callback_data='мп-20-06')
inline_btn_msm_18_06 = InlineKeyboardButton("мсм-18-06", callback_data='мсм-18-06')
inline_btn_msm_19_06 = InlineKeyboardButton("мсм-19-06", callback_data='мсм-19-06')
inline_btn_msm_20_05 = InlineKeyboardButton("мсм-20-05", callback_data='мсм-20-05')
inline_btn_mtm_18_01 = InlineKeyboardButton("мтм-18-01", callback_data='мтм-18-01')
inline_btn_mtm_18_02 = InlineKeyboardButton("мтм-18-02", callback_data='мтм-18-02')
inline_btn_mtm_18_03 = InlineKeyboardButton("мтм-18-03", callback_data='мтм-18-03')
inline_btn_mtm_19_01 = InlineKeyboardButton("мтм-19-01", callback_data='мтм-19-01')
inline_btn_mtm_19_02 = InlineKeyboardButton("мтм-19-02", callback_data='мтм-19-02')
inline_btn_mtm_19_03 = InlineKeyboardButton("мтм-19-03", callback_data='мтм-19-03')
inline_btn_mtm_19_05 = InlineKeyboardButton("мтм-19-05", callback_data='мтм-19-05')
inline_btn_mtm_20_01 = InlineKeyboardButton("мтм-20-01", callback_data='мтм-20-01')
inline_btn_mtm_20_02 = InlineKeyboardButton("мтм-20-02", callback_data='мтм-20-02')
inline_btn_mtm_20_03 = InlineKeyboardButton("мтм-20-03", callback_data='мтм-20-03')
group_im_kb = InlineKeyboardMarkup().add(inline_btn_ma_17_07, inline_btn_ma_18_07, inline_btn_ma_19_03, inline_btn_ma_20_03, inline_btn_mb_17_08, inline_btn_mb_18_08, inline_btn_mb_19_08, inline_btn_mb_20_07, inline_btn_mbm_19_04, inline_btn_mbm_20_04, inline_btn_md_17_11, inline_btn_md_18_11, inline_btn_md_19_01, inline_btn_md_20_01, inline_btn_mm_17_12, inline_btn_mm_18_12, inline_btn_mm_19_07, inline_btn_mm_20_02, inline_btn_mo_16_09, inline_btn_mo_16_10, inline_btn_mo_17_09, inline_btn_mo_17_10, inline_btn_mo_18_09, inline_btn_mo_18_10, inline_btn_mo_19_04, inline_btn_mo_19_05, inline_btn_mo_20_04, inline_btn_mo_20_05, inline_btn_mp_16_06, inline_btn_mp_17_06, inline_btn_mp_18_06, inline_btn_mp_19_06, inline_btn_mp_20_06, inline_btn_msm_18_06, inline_btn_msm_19_06, inline_btn_msm_20_05, inline_btn_mtm_18_01, inline_btn_mtm_18_02, inline_btn_mtm_18_03, inline_btn_mtm_19_01, inline_btn_mtm_19_02, inline_btn_mtm_19_03, inline_btn_mtm_19_05, inline_btn_mtm_20_01, inline_btn_mtm_20_02, inline_btn_mtm_20_03)


im = {
	"ма-17-07" : "3&groupId=4572",
	"ма-18-07" : "3&groupId=4975",
	"ма-19-03" : "3&groupId=6383",
	"ма-20-03" : "3&groupId=6951",
	"мб-17-08" : "3&groupId=4573",
	"мб-18-08" : "3&groupId=4976",
	"мб-19-08" : "3&groupId=6389",
	"мб-20-07" : "3&groupId=6955",
	"мбм-19-04" : "3&groupId=6395",
	"мбм-20-04" : "3&groupId=6947",
	"мд-17-11" : "3&groupId=4575",
	"мд-18-11" : "3&groupId=4977",
	"мд-19-01" : "3&groupId=6384",
	"мд-20-01" : "3&groupId=6949",
	"мм-17-12" : "3&groupId=4576",
	"мм-18-12" : "3&groupId=4978",
	"мм-19-07" : "3&groupId=6388",
	"мм-20-02" : "3&groupId=6950",
	"мо-16-09" : "3&groupId=2677",
	"мо-16-10" : "3&groupId=2678",
	"мо-17-09" : "3&groupId=4577",
	"мо-17-10" : "3&groupId=4578",
	"мо-18-09" : "3&groupId=4979",
	"мо-18-10" : "3&groupId=4980",
	"мо-19-04" : "3&groupId=6386",
	"мо-19-05" : "3&groupId=6387",
	"мо-20-04" : "3&groupId=6952",
	"мо-20-05" : "3&groupId=6953",
	"мп-16-06" : "3&groupId=2679",
	"мп-17-06" : "3&groupId=4579",
	"мп-18-06" : "3&groupId=4981",
	"мп-19-06" : "3&groupId=6390",
	"мп-20-06" : "3&groupId=6954",
	"мсм-18-06" : "3&groupId=5013",
	"мсм-19-06" : "3&groupId=6396",
	"мсм-20-05" : "3&groupId=6948",
	"мтм-18-01" : "3&groupId=5009",
	"мтм-18-02" : "3&groupId=5010",
	"мтм-18-03" : "3&groupId=5011",
	"мтм-19-01" : "3&groupId=6391",
	"мтм-19-02" : "3&groupId=6392",
	"мтм-19-03" : "3&groupId=6393",
	"мтм-19-05" : "3&groupId=6394",
	"мтм-20-01" : "3&groupId=6944",
	"мтм-20-02" : "3&groupId=6945",
	"мтм-20-03" : "3&groupId=6946"
}


inline_btn_vn_16_01 = InlineKeyboardButton("вн-16-01", callback_data='вн-16-01')
inline_btn_vn_17_01 = InlineKeyboardButton("вн-17-01", callback_data='вн-17-01')
inline_btn_vn_18_01 = InlineKeyboardButton("вн-18-01", callback_data='вн-18-01')
inline_btn_vn_19_01 = InlineKeyboardButton("вн-19-01", callback_data='вн-19-01')
inline_btn_vn_20_01 = InlineKeyboardButton("вн-20-01", callback_data='вн-20-01')
inline_btn_vnm_18_02 = InlineKeyboardButton("внм-18-02", callback_data='внм-18-02')
inline_btn_vnm_18_17 = InlineKeyboardButton("внм-18-17", callback_data='внм-18-17')
inline_btn_vnm_19_02 = InlineKeyboardButton("внм-19-02", callback_data='внм-19-02')
inline_btn_vnm_19_15 = InlineKeyboardButton("внм-19-15", callback_data='внм-19-15')
inline_btn_vnm_20_17 = InlineKeyboardButton("внм-20-17", callback_data='внм-20-17')
inline_btn_vnm_20_52 = InlineKeyboardButton("внм-20-52", callback_data='внм-20-52')
inline_btn_ta_16_07 = InlineKeyboardButton("та-16-07", callback_data='та-16-07')
inline_btn_ta_17_07 = InlineKeyboardButton("та-17-07", callback_data='та-17-07')
inline_btn_ta_18_07 = InlineKeyboardButton("та-18-07", callback_data='та-18-07')
inline_btn_tv_16_08 = InlineKeyboardButton("тв-16-08", callback_data='тв-16-08')
inline_btn_tv_17_08 = InlineKeyboardButton("тв-17-08", callback_data='тв-17-08')
inline_btn_tv_18_08 = InlineKeyboardButton("тв-18-08", callback_data='тв-18-08')
inline_btn_tmm_18_11 = InlineKeyboardButton("тмм-18-11", callback_data='тмм-18-11')
inline_btn_tn_16_01 = InlineKeyboardButton("тн-16-01", callback_data='тн-16-01')
inline_btn_tn_16_02 = InlineKeyboardButton("тн-16-02", callback_data='тн-16-02')
inline_btn_tn_17_01 = InlineKeyboardButton("тн-17-01", callback_data='тн-17-01')
inline_btn_tn_17_02 = InlineKeyboardButton("тн-17-02", callback_data='тн-17-02')
inline_btn_tn_18_01 = InlineKeyboardButton("тн-18-01", callback_data='тн-18-01')
inline_btn_tn_18_02 = InlineKeyboardButton("тн-18-02", callback_data='тн-18-02')
inline_btn_tnm_18_01 = InlineKeyboardButton("тнм-18-01", callback_data='тнм-18-01')
inline_btn_tnm_18_02 = InlineKeyboardButton("тнм-18-02", callback_data='тнм-18-02')
inline_btn_tnm_18_03 = InlineKeyboardButton("тнм-18-03", callback_data='тнм-18-03')
inline_btn_tnm_18_04 = InlineKeyboardButton("тнм-18-04", callback_data='тнм-18-04')
inline_btn_tnm_19_01 = InlineKeyboardButton("тнм-19-01", callback_data='тнм-19-01')
inline_btn_tnm_19_02 = InlineKeyboardButton("тнм-19-02", callback_data='тнм-19-02')
inline_btn_tnm_19_03 = InlineKeyboardButton("тнм-19-03", callback_data='тнм-19-03')
inline_btn_tnm_19_04 = InlineKeyboardButton("тнм-19-04", callback_data='тнм-19-04')
inline_btn_tnm_19_05 = InlineKeyboardButton("тнм-19-05", callback_data='тнм-19-05')
inline_btn_tnm_19_06 = InlineKeyboardButton("тнм-19-06", callback_data='тнм-19-06')
inline_btn_tnm_19_07 = InlineKeyboardButton("тнм-19-07", callback_data='тнм-19-07')
inline_btn_tnm_19_08 = InlineKeyboardButton("тнм-19-08", callback_data='тнм-19-08')
inline_btn_tnm_19_11 = InlineKeyboardButton("тнм-19-11", callback_data='тнм-19-11')
inline_btn_tnm_20_01 = InlineKeyboardButton("тнм-20-01", callback_data='тнм-20-01')
inline_btn_tnm_20_02 = InlineKeyboardButton("тнм-20-02", callback_data='тнм-20-02')
inline_btn_tnm_20_03 = InlineKeyboardButton("тнм-20-03", callback_data='тнм-20-03')
inline_btn_tnm_20_04 = InlineKeyboardButton("тнм-20-04", callback_data='тнм-20-04')
inline_btn_tnm_20_05 = InlineKeyboardButton("тнм-20-05", callback_data='тнм-20-05')
inline_btn_tnm_20_06 = InlineKeyboardButton("тнм-20-06", callback_data='тнм-20-06')
inline_btn_tnm_20_07 = InlineKeyboardButton("тнм-20-07", callback_data='тнм-20-07')
inline_btn_tnm_20_08 = InlineKeyboardButton("тнм-20-08", callback_data='тнм-20-08')
inline_btn_tnm_20_09 = InlineKeyboardButton("тнм-20-09", callback_data='тнм-20-09')
inline_btn_tp_16_03 = InlineKeyboardButton("тп-16-03", callback_data='тп-16-03')
inline_btn_tp_16_04 = InlineKeyboardButton("тп-16-04", callback_data='тп-16-04')
inline_btn_tp_17_03 = InlineKeyboardButton("тп-17-03", callback_data='тп-17-03')
inline_btn_tp_17_04 = InlineKeyboardButton("тп-17-04", callback_data='тп-17-04')
inline_btn_tp_18_03 = InlineKeyboardButton("тп-18-03", callback_data='тп-18-03')
inline_btn_tp_18_04 = InlineKeyboardButton("тп-18-04", callback_data='тп-18-04')
inline_btn_tp_19_01 = InlineKeyboardButton("тп-19-01", callback_data='тп-19-01')
inline_btn_tp_19_02 = InlineKeyboardButton("тп-19-02", callback_data='тп-19-02')
inline_btn_tp_19_03 = InlineKeyboardButton("тп-19-03", callback_data='тп-19-03')
inline_btn_tp_19_04 = InlineKeyboardButton("тп-19-04", callback_data='тп-19-04')
inline_btn_tp_19_07 = InlineKeyboardButton("тп-19-07", callback_data='тп-19-07')
inline_btn_tp_20_01 = InlineKeyboardButton("тп-20-01", callback_data='тп-20-01')
inline_btn_tp_20_02 = InlineKeyboardButton("тп-20-02", callback_data='тп-20-02')
inline_btn_tp_20_03 = InlineKeyboardButton("тп-20-03", callback_data='тп-20-03')
inline_btn_tp_20_04 = InlineKeyboardButton("тп-20-04", callback_data='тп-20-04')
inline_btn_tp_20_07 = InlineKeyboardButton("тп-20-07", callback_data='тп-20-07')
inline_btn_ts_16_05 = InlineKeyboardButton("тс-16-05", callback_data='тс-16-05')
inline_btn_ts_16_06 = InlineKeyboardButton("тс-16-06", callback_data='тс-16-06')
inline_btn_ts_17_05 = InlineKeyboardButton("тс-17-05", callback_data='тс-17-05')
inline_btn_ts_17_06 = InlineKeyboardButton("тс-17-06", callback_data='тс-17-06')
inline_btn_ts_18_05 = InlineKeyboardButton("тс-18-05", callback_data='тс-18-05')
inline_btn_ts_18_06 = InlineKeyboardButton("тс-18-06", callback_data='тс-18-06')
inline_btn_ts_19_05 = InlineKeyboardButton("тс-19-05", callback_data='тс-19-05')
inline_btn_ts_19_06 = InlineKeyboardButton("тс-19-06", callback_data='тс-19-06')
inline_btn_ts_20_05 = InlineKeyboardButton("тс-20-05", callback_data='тс-20-05')
inline_btn_ts_20_06 = InlineKeyboardButton("тс-20-06", callback_data='тс-20-06')
group_pseptt_kb = InlineKeyboardMarkup().add(inline_btn_vn_16_01, inline_btn_vn_17_01, inline_btn_vn_18_01, inline_btn_vn_19_01, inline_btn_vn_20_01, inline_btn_vnm_18_02, inline_btn_vnm_18_17, inline_btn_vnm_19_02, inline_btn_vnm_19_15, inline_btn_vnm_20_17, inline_btn_vnm_20_52, inline_btn_ta_16_07, inline_btn_ta_17_07, inline_btn_ta_18_07, inline_btn_tv_16_08, inline_btn_tv_17_08, inline_btn_tv_18_08, inline_btn_tmm_18_11, inline_btn_tn_16_01, inline_btn_tn_16_02, inline_btn_tn_17_01, inline_btn_tn_17_02, inline_btn_tn_18_01, inline_btn_tn_18_02, inline_btn_tnm_18_01, inline_btn_tnm_18_02, inline_btn_tnm_18_03, inline_btn_tnm_18_04, inline_btn_tnm_19_01, inline_btn_tnm_19_02, inline_btn_tnm_19_03, inline_btn_tnm_19_04, inline_btn_tnm_19_05, inline_btn_tnm_19_06, inline_btn_tnm_19_07, inline_btn_tnm_19_08, inline_btn_tnm_19_11, inline_btn_tnm_20_01, inline_btn_tnm_20_02, inline_btn_tnm_20_03, inline_btn_tnm_20_04, inline_btn_tnm_20_05, inline_btn_tnm_20_06, inline_btn_tnm_20_07, inline_btn_tnm_20_08, inline_btn_tnm_20_09, inline_btn_tp_16_03, inline_btn_tp_16_04, inline_btn_tp_17_03, inline_btn_tp_17_04, inline_btn_tp_18_03, inline_btn_tp_18_04, inline_btn_tp_19_01, inline_btn_tp_19_02, inline_btn_tp_19_03, inline_btn_tp_19_04, inline_btn_tp_19_07, inline_btn_tp_20_01, inline_btn_tp_20_02, inline_btn_tp_20_03, inline_btn_tp_20_04, inline_btn_tp_20_07, inline_btn_ts_16_05, inline_btn_ts_16_06, inline_btn_ts_17_05, inline_btn_ts_17_06, inline_btn_ts_18_05, inline_btn_ts_18_06, inline_btn_ts_19_05, inline_btn_ts_19_06, inline_btn_ts_20_05, inline_btn_ts_20_06)


pseptt = {
	"вн-16-01" : "2&groupId=2648",
	"вн-17-01" : "2&groupId=4686",
	"вн-18-01" : "2&groupId=5021",
	"вн-19-01" : "2&groupId=6437",
	"вн-20-01" : "2&groupId=7433",
	"внм-18-02" : "2&groupId=5047",
	"внм-18-17" : "2&groupId=5024",
	"внм-19-02" : "2&groupId=6476",
	"внм-19-15" : "2&groupId=6509",
	"внм-20-17" : "2&groupId=7434",
	"внм-20-52" : "2&groupId=7435",
	"та-16-07" : "2&groupId=2703",
	"та-17-07" : "2&groupId=4656",
	"та-18-07" : "2&groupId=5054",
	"тв-16-08" : "2&groupId=2704",
	"тв-17-08" : "2&groupId=4657",
	"тв-18-08" : "2&groupId=5055",
	"тмм-18-11" : "2&groupId=5549",
	"тн-16-01" : "2&groupId=2697",
	"тн-16-02" : "2&groupId=2698",
	"тн-17-01" : "2&groupId=4649",
	"тн-17-02" : "2&groupId=4653",
	"тн-18-01" : "2&groupId=5048",
	"тн-18-02" : "2&groupId=5049",
	"тнм-18-01" : "2&groupId=5056",
	"тнм-18-02" : "2&groupId=5058",
	"тнм-18-03" : "2&groupId=5059",
	"тнм-18-04" : "2&groupId=5060",
	"тнм-19-01" : "2&groupId=6426",
	"тнм-19-02" : "2&groupId=6429",
	"тнм-19-03" : "2&groupId=6516",
	"тнм-19-04" : "2&groupId=6430",
	"тнм-19-05" : "2&groupId=6724",
	"тнм-19-06" : "2&groupId=6427",
	"тнм-19-07" : "2&groupId=6428",
	"тнм-19-08" : "2&groupId=6517",
	"тнм-19-11" : "2&groupId=7577",
	"тнм-20-01" : "2&groupId=7053",
	"тнм-20-02" : "2&groupId=7054",
	"тнм-20-03" : "2&groupId=7055",
	"тнм-20-04" : "2&groupId=7056",
	"тнм-20-05" : "2&groupId=7057",
	"тнм-20-06" : "2&groupId=7058",
	"тнм-20-07" : "2&groupId=7059",
	"тнм-20-08" : "2&groupId=7060",
	"тнм-20-09" : "2&groupId=7061",
	"тп-16-03" : "2&groupId=2699",
	"тп-16-04" : "2&groupId=2700",
	"тп-17-03" : "2&groupId=4651",
	"тп-17-04" : "2&groupId=4652",
	"тп-18-03" : "2&groupId=5050",
	"тп-18-04" : "2&groupId=5051",
	"тп-19-01" : "2&groupId=6405",
	"тп-19-02" : "2&groupId=6406",
	"тп-19-03" : "2&groupId=6407",
	"тп-19-04" : "2&groupId=6408",
	"тп-19-07" : "2&groupId=6411",
	"тп-20-01" : "2&groupId=7409",
	"тп-20-02" : "2&groupId=7410",
	"тп-20-03" : "2&groupId=7411",
	"тп-20-04" : "2&groupId=7412",
	"тп-20-07" : "2&groupId=7415",
	"тс-16-05" : "2&groupId=2701",
	"тс-16-06" : "2&groupId=2702",
	"тс-17-05" : "2&groupId=4654",
	"тс-17-06" : "2&groupId=4655",
	"тс-18-05" : "2&groupId=5052",
	"тс-18-06" : "2&groupId=5053",
	"тс-19-05" : "2&groupId=6409",
	"тс-19-06" : "2&groupId=6410",
	"тс-20-05" : "2&groupId=7413",
	"тс-20-06" : "2&groupId=7414"
}


inline_btn_rn_20_06 = InlineKeyboardButton("рн-20-06", callback_data='рн-20-06')
inline_btn_rn_20_11 = InlineKeyboardButton("рн-20-11", callback_data='рн-20-11')
inline_btn_rnm_19_01 = InlineKeyboardButton("рнм-19-01", callback_data='рнм-19-01')
inline_btn_rnm_19_02 = InlineKeyboardButton("рнм-19-02", callback_data='рнм-19-02')
inline_btn_rnm_19_03 = InlineKeyboardButton("рнм-19-03", callback_data='рнм-19-03')
inline_btn_rnm_19_04 = InlineKeyboardButton("рнм-19-04", callback_data='рнм-19-04')
inline_btn_rnm_19_05 = InlineKeyboardButton("рнм-19-05", callback_data='рнм-19-05')
inline_btn_rnm_19_06 = InlineKeyboardButton("рнм-19-06", callback_data='рнм-19-06')
inline_btn_rnm_19_09 = InlineKeyboardButton("рнм-19-09", callback_data='рнм-19-09')
inline_btn_rnm_19_10 = InlineKeyboardButton("рнм-19-10", callback_data='рнм-19-10')
inline_btn_rnm_19_11 = InlineKeyboardButton("рнм-19-11", callback_data='рнм-19-11')
inline_btn_rnm_20_01 = InlineKeyboardButton("рнм-20-01", callback_data='рнм-20-01')
inline_btn_rnm_20_02 = InlineKeyboardButton("рнм-20-02", callback_data='рнм-20-02')
inline_btn_rnm_20_03 = InlineKeyboardButton("рнм-20-03", callback_data='рнм-20-03')
inline_btn_rnm_20_04 = InlineKeyboardButton("рнм-20-04", callback_data='рнм-20-04')
inline_btn_rnm_20_05 = InlineKeyboardButton("рнм-20-05", callback_data='рнм-20-05')
inline_btn_rnm_20_06 = InlineKeyboardButton("рнм-20-06", callback_data='рнм-20-06')
inline_btn_rnm_20_08 = InlineKeyboardButton("рнм-20-08", callback_data='рнм-20-08')
inline_btn_rnm_20_09 = InlineKeyboardButton("рнм-20-09", callback_data='рнм-20-09')
inline_btn_rnm_20_10 = InlineKeyboardButton("рнм-20-10", callback_data='рнм-20-10')
inline_btn_rnm_20_11 = InlineKeyboardButton("рнм-20-11", callback_data='рнм-20-11')
inline_btn_rs_18_10 = InlineKeyboardButton("рс-18-10", callback_data='рс-18-10')
inline_btn_rs_19_10 = InlineKeyboardButton("рс-19-10", callback_data='рс-19-10')
inline_btn_rs_20_10 = InlineKeyboardButton("рс-20-10", callback_data='рс-20-10')
inline_btn_rf_15_09 = InlineKeyboardButton("рф-15-09", callback_data='рф-15-09')
inline_btn_rf_16_09 = InlineKeyboardButton("рф-16-09", callback_data='рф-16-09')
inline_btn_rf_17_09 = InlineKeyboardButton("рф-17-09", callback_data='рф-17-09')
inline_btn_rf_18_09 = InlineKeyboardButton("рф-18-09", callback_data='рф-18-09')
inline_btn_rf_19_09 = InlineKeyboardButton("рф-19-09", callback_data='рф-19-09')
inline_btn_rf_20_09 = InlineKeyboardButton("рф-20-09", callback_data='рф-20-09')
group_rngm_kb = InlineKeyboardMarkup().add(inline_btn_rn_20_06, inline_btn_rn_20_11, inline_btn_rnm_19_01, inline_btn_rnm_19_02, inline_btn_rnm_19_03, inline_btn_rnm_19_04, inline_btn_rnm_19_05, inline_btn_rnm_19_06, inline_btn_rnm_19_09, inline_btn_rnm_19_10, inline_btn_rnm_19_11, inline_btn_rnm_20_01, inline_btn_rnm_20_02, inline_btn_rnm_20_03, inline_btn_rnm_20_04, inline_btn_rnm_20_05, inline_btn_rnm_20_06, inline_btn_rnm_20_08, inline_btn_rnm_20_09, inline_btn_rnm_20_10, inline_btn_rnm_20_11, inline_btn_rs_18_10, inline_btn_rs_19_10, inline_btn_rs_20_10, inline_btn_rf_15_09, inline_btn_rf_16_09, inline_btn_rf_17_09, inline_btn_rf_18_09, inline_btn_rf_19_09, inline_btn_rf_20_09)


rngm = {
	"рб-17-01" : "1&groupId=4598",
	"рб-17-02" : "1&groupId=4599",
	"рб-18-01" : "1&groupId=5155",
	"рб-18-02" : "1&groupId=5156",
	"рб-19-01" : "1&groupId=6486",
	"рб-19-02" : "1&groupId=6487",
	"рб-19-03" : "1&groupId=6495",
	"рб-20-01" : "1&groupId=7030",
	"рб-20-02" : "1&groupId=7031",
	"рб-20-03" : "1&groupId=7032",
	"рг-17-07" : "1&groupId=4604",
	"рг-17-08" : "1&groupId=4605",
	"рг-18-06" : "1&groupId=5160",
	"рг-18-07" : "1&groupId=5161",
	"рг-18-08" : "1&groupId=5162",
	"рг-19-07" : "1&groupId=6490",
	"рг-19-08" : "1&groupId=6491",
	"рг-20-07" : "1&groupId=7038",
	"рг-20-08" : "1&groupId=7039",
	"рмм-19-12" : "1&groupId=6728",
	"рмм-19-13" : "1&groupId=6535",
	"рмм-20-12" : "1&groupId=7051",
	"рмм-20-13" : "1&groupId=7052",
	"рн-17-03" : "1&groupId=4600",
	"рн-17-04" : "1&groupId=4601",
	"рн-17-05" : "1&groupId=4602",
	"рн-17-06" : "1&groupId=4603",
	"рн-18-03" : "1&groupId=5157",
	"рн-18-04" : "1&groupId=5158",
	"рн-18-05" : "1&groupId=5159",
	"рн-19-04" : "1&groupId=6488",
	"рн-19-05" : "1&groupId=6489",
	"рн-19-06" : "1&groupId=6497",
	"рн-19-11" : "1&groupId=6810",
	"рн-20-04" : "1&groupId=7033",
	"рн-20-05" : "1&groupId=7034",
	"рн-20-06" : "1&groupId=7036",
	"рн-20-11" : "1&groupId=7037",
	"рнм-19-01" : "1&groupId=6522",
	"рнм-19-02" : "1&groupId=6523",
	"рнм-19-03" : "1&groupId=6524",
	"рнм-19-04" : "1&groupId=6525",
	"рнм-19-05" : "1&groupId=6526",
	"рнм-19-06" : "1&groupId=6534",
	"рнм-19-09" : "1&groupId=6557",
	"рнм-19-10" : "1&groupId=6556",
	"рнм-19-11" : "1&groupId=6558",
	"рнм-20-01" : "1&groupId=6992",
	"рнм-20-02" : "1&groupId=6993",
	"рнм-20-03" : "1&groupId=6994",
	"рнм-20-04" : "1&groupId=6995",
	"рнм-20-05" : "1&groupId=6996",
	"рнм-20-06" : "1&groupId=6997",
	"рнм-20-08" : "1&groupId=6999",
	"рнм-20-09" : "1&groupId=7000",
	"рнм-20-10" : "1&groupId=7001",
	"рнм-20-11" : "1&groupId=7050",
	"рс-18-10" : "1&groupId=5166",
	"рс-19-10" : "1&groupId=6494",
	"рс-20-10" : "1&groupId=7041",
	"рф-15-09" : "1&groupId=2507",
	"рф-16-09" : "1&groupId=2714",
	"рф-17-09" : "1&groupId=4608",
	"рф-18-09" : "1&groupId=5163",
	"рф-19-09" : "1&groupId=6492",
	"рф-20-09" : "1&groupId=7040"
}


inline_btn_hv_17_07 = InlineKeyboardButton("хв-17-07", callback_data="хв-17-07")
inline_btn_hv_18_07 = InlineKeyboardButton("хв-18-07", callback_data="хв-18-07")
inline_btn_ht_17_01 = InlineKeyboardButton("хт-17-01", callback_data="хт-17-01")
inline_btn_ht_17_02 = InlineKeyboardButton("хт-17-02", callback_data="хт-17-02")
inline_btn_ht_17_03 = InlineKeyboardButton("хт-17-03", callback_data="хт-17-03")
inline_btn_ht_17_04 = InlineKeyboardButton("хт-17-04", callback_data="хт-17-04")
inline_btn_ht_17_05 = InlineKeyboardButton("хт-17-05", callback_data="хт-17-05")
inline_btn_ht_17_06 = InlineKeyboardButton("хт-17-06", callback_data="хт-17-06")
inline_btn_ht_18_01 = InlineKeyboardButton("хт-18-01", callback_data="хт-18-01")
inline_btn_ht_18_02 = InlineKeyboardButton("хт-18-02", callback_data="хт-18-02")
inline_btn_ht_18_03 = InlineKeyboardButton("хт-18-03", callback_data="хт-18-03")
inline_btn_ht_18_04 = InlineKeyboardButton("хт-18-04", callback_data="хт-18-04")
inline_btn_ht_18_05 = InlineKeyboardButton("хт-18-05", callback_data="хт-18-05")
inline_btn_ht_18_06 = InlineKeyboardButton("хт-18-06", callback_data="хт-18-06")
inline_btn_ht_19_01 = InlineKeyboardButton("хт-19-01", callback_data="хт-19-01")
inline_btn_ht_19_02 = InlineKeyboardButton("хт-19-02", callback_data="хт-19-02")
inline_btn_ht_19_03 = InlineKeyboardButton("хт-19-03", callback_data="хт-19-03")
inline_btn_ht_19_04 = InlineKeyboardButton("хт-19-04", callback_data="хт-19-04")
inline_btn_ht_19_05 = InlineKeyboardButton("хт-19-05", callback_data="хт-19-05")
inline_btn_ht_19_06 = InlineKeyboardButton("хт-19-06", callback_data="хт-19-06")
inline_btn_ht_19_07 = InlineKeyboardButton("хт-19-07", callback_data="хт-19-07")
inline_btn_ht_20_01 = InlineKeyboardButton("хт-20-01", callback_data="хт-20-01")
inline_btn_ht_20_02 = InlineKeyboardButton("хт-20-02", callback_data="хт-20-02")
inline_btn_ht_20_03 = InlineKeyboardButton("хт-20-03", callback_data="хт-20-03")
inline_btn_ht_20_04 = InlineKeyboardButton("хт-20-04", callback_data="хт-20-04")
inline_btn_ht_20_05 = InlineKeyboardButton("хт-20-05", callback_data="хт-20-05")
inline_btn_ht_20_06 = InlineKeyboardButton("хт-20-06", callback_data="хт-20-06")
inline_btn_ht_20_07 = InlineKeyboardButton("хт-20-07", callback_data="хт-20-07")
inline_btn_htm_19_01 = InlineKeyboardButton("хтм-19-01", callback_data="хтм-19-01")
inline_btn_htm_19_02 = InlineKeyboardButton("хтм-19-02", callback_data="хтм-19-02")
inline_btn_htm_19_03 = InlineKeyboardButton("хтм-19-03", callback_data="хтм-19-03")
inline_btn_htm_19_05 = InlineKeyboardButton("хтм-19-05", callback_data="хтм-19-05")
inline_btn_htm_20_01 = InlineKeyboardButton("хтм-20-01", callback_data="хтм-20-01")
inline_btn_htm_20_02 = InlineKeyboardButton("хтм-20-02", callback_data="хтм-20-02")
inline_btn_htm_20_03 = InlineKeyboardButton("хтм-20-03", callback_data="хтм-20-03")
inline_btn_htm_20_04 = InlineKeyboardButton("хтм-20-04", callback_data="хтм-20-04")
inline_btn_he_17_08 = InlineKeyboardButton("хэ-17-08", callback_data="хэ-17-08")
inline_btn_he_18_08 = InlineKeyboardButton("хэ-18-08", callback_data="хэ-18-08")
inline_btn_he_19_08 = InlineKeyboardButton("хэ-19-08", callback_data="хэ-19-08")
inline_btn_he_20_08 = InlineKeyboardButton("хэ-20-08", callback_data="хэ-20-08")
inline_btn_hem_19_07 = InlineKeyboardButton("хэм-19-07", callback_data="хэм-19-07")
inline_btn_hem_20_05 = InlineKeyboardButton("хэм-20-05", callback_data="хэм-20-05")
group_hte_kb = InlineKeyboardMarkup().add(inline_btn_hv_17_07, inline_btn_hv_18_07, inline_btn_ht_17_01, inline_btn_ht_17_02, inline_btn_ht_17_03, inline_btn_ht_17_04, inline_btn_ht_17_05, inline_btn_ht_17_06, inline_btn_ht_18_01, inline_btn_ht_18_02, inline_btn_ht_18_03, inline_btn_ht_18_04, inline_btn_ht_18_05, inline_btn_ht_18_06, inline_btn_ht_19_01, inline_btn_ht_19_02, inline_btn_ht_19_03, inline_btn_ht_19_04, inline_btn_ht_19_05, inline_btn_ht_19_06, inline_btn_ht_19_07, inline_btn_ht_20_01, inline_btn_ht_20_02, inline_btn_ht_20_03, inline_btn_ht_20_04, inline_btn_ht_20_05, inline_btn_ht_20_06, inline_btn_ht_20_07, inline_btn_htm_19_01, inline_btn_htm_19_02, inline_btn_htm_19_03, inline_btn_htm_19_05, inline_btn_htm_20_01, inline_btn_htm_20_02, inline_btn_htm_20_03, inline_btn_htm_20_04, inline_btn_he_17_08, inline_btn_he_18_08, inline_btn_he_19_08, inline_btn_he_20_08, inline_btn_hem_19_07, inline_btn_hem_20_05)


hte = {
	"хв-17-07" : "4&groupId=4571",
	"хв-18-07" : "4&groupId=5071",
	"хт-17-01" : "4&groupId=4565",
	"хт-17-02" : "4&groupId=4566",
	"хт-17-03" : "4&groupId=4567",
	"хт-17-04" : "4&groupId=4568",
	"хт-17-05" : "4&groupId=4569",
	"хт-17-06" : "4&groupId=4570",
	"хт-18-01" : "4&groupId=5067",
	"хт-18-02" : "4&groupId=5068",
	"хт-18-03" : "4&groupId=5069",
	"хт-18-04" : "4&groupId=5070",
	"хт-18-05" : "4&groupId=5074",
	"хт-18-06" : "4&groupId=5075",
	"хт-19-01" : "4&groupId=6467",
	"хт-19-02" : "4&groupId=6468",
	"хт-19-03" : "4&groupId=6469",
	"хт-19-04" : "4&groupId=6470",
	"хт-19-05" : "4&groupId=6472",
	"хт-19-06" : "4&groupId=6473",
	"хт-19-07" : "4&groupId=6471",
	"хт-20-01" : "4&groupId=7002",
	"хт-20-02" : "4&groupId=7003",
	"хт-20-03" : "4&groupId=7004",
	"хт-20-04" : "4&groupId=7005",
	"хт-20-05" : "4&groupId=7011",
	"хт-20-06" : "4&groupId=7012",
	"хт-20-07" : "4&groupId=7006",
	"хтм-19-01" : "4&groupId=6440",
	"хтм-19-02" : "4&groupId=6441",
	"хтм-19-03" : "4&groupId=6442",
	"хтм-19-05" : "4&groupId=6790",
	"хтм-20-01" : "4&groupId=7007",
	"хтм-20-02" : "4&groupId=7008",
	"хтм-20-03" : "4&groupId=7009",
	"хтм-20-04" : "4&groupId=7010",
	"хэ-17-08" : "4&groupId=4607",
	"хэ-18-08" : "4&groupId=5072",
	"хэ-19-08" : "4&groupId=6474",
	"хэ-20-08" : "4&groupId=7013",
	"хэм-19-07" : "4&groupId=6443",
	"хэм-20-05" : "4&groupId=7043"
}


inline_btn_vm_16_03 = InlineKeyboardButton("вм-16-03", callback_data="вм-16-03")
inline_btn_vm_17_01 = InlineKeyboardButton("вм-17-01", callback_data="вм-17-01")
inline_btn_vm_18_01 = InlineKeyboardButton("вм-18-01", callback_data="вм-18-01")
inline_btn_vm__19_01 = InlineKeyboardButton("вм-19-01", callback_data="вм-19-01")
inline_btn_vm_20_01 = InlineKeyboardButton("вм-20-01", callback_data="вм-20-01")
inline_btn_vmm__18_04 = InlineKeyboardButton("вмм-18-04", callback_data="вмм-18-04")
inline_btn_vmm_18_09 = InlineKeyboardButton("вмм-18-09", callback_data="вмм-18-09")
inline_btn_vmm_19_04 = InlineKeyboardButton("вмм-19-04", callback_data="вмм-19-04")
inline_btn_vmm_19_09 = InlineKeyboardButton("вмм-19-09", callback_data="вмм-19-09")
inline_btn_vmm_20_13 = InlineKeyboardButton("вмм-20-13", callback_data="вмм-20-13")
inline_btn_vem_18_09 = InlineKeyboardButton("вэм-18-09", callback_data="вэм-18-09")
inline_btn_vem_18_12 = InlineKeyboardButton("вэм-18-12", callback_data="вэм-18-12")
inline_btn_vem_19_12 = InlineKeyboardButton("вэм-19-12", callback_data="вэм-19-12")
inline_btn_vem_18_15 = InlineKeyboardButton("вэм-19-15", callback_data="вэм-19-15")
inline_btn_vem_20_09 = InlineKeyboardButton("вэм-20-09", callback_data="вэм-20-09")
inline_btn_zm_16_01 = InlineKeyboardButton("зм-16-01", callback_data="зм-16-01")
inline_btn_zm_17_01 = InlineKeyboardButton("зм-17-01", callback_data="зм-17-01")
inline_btn_zm_18_01 = InlineKeyboardButton("зм-18-01", callback_data="зм-18-01")
inline_btn_zm_19_01 = InlineKeyboardButton("зм-19-01", callback_data="зм-19-01")
inline_btn_ze_16_05 = InlineKeyboardButton("зэ-16-05", callback_data="зэ-16-05")
inline_btn_ze_17_01 = InlineKeyboardButton("зэ-17-01", callback_data="зэ-17-01")
inline_btn_ze_18_01 = InlineKeyboardButton("зэ-18-01", callback_data="зэ-18-01")
inline_btn_ze_19_01 = InlineKeyboardButton("зэ-19-01", callback_data="зэ-19-01")
inline_btn_em_17_03 = InlineKeyboardButton("эм-17-03", callback_data="эм-17-03")
inline_btn_em_18_04 = InlineKeyboardButton("эм-18-04", callback_data="эм-18-04")
inline_btn_em_19_03 = InlineKeyboardButton("эм-19-03", callback_data="эм-19-03")
inline_btn_em_20_03 = InlineKeyboardButton("эм-20-03", callback_data="эм-20-03")
inline_btn_emm_19_01 = InlineKeyboardButton("эмм-19-01", callback_data="эмм-19-01")
inline_btn_ee_17_01 = InlineKeyboardButton("ээ-17-01", callback_data="ээ-17-01")
inline_btn_ee_17_02 = InlineKeyboardButton("ээ-17-02", callback_data="ээ-17-02")
inline_btn_ee_18_01 = InlineKeyboardButton("ээ-18-01", callback_data="ээ-18-01")
inline_btn_ee_18_02 = InlineKeyboardButton("ээ-18-02", callback_data="ээ-18-02")
inline_btn_ee_18_03 = InlineKeyboardButton("ээ-18-03", callback_data="ээ-18-03")
inline_btn_ee_19_01 = InlineKeyboardButton("ээ-19-01", callback_data="ээ-19-01")
inline_btn_ee_19_02 = InlineKeyboardButton("ээ-19-02", callback_data="ээ-19-02")
inline_btn_ee_20_01 = InlineKeyboardButton("ээ-20-01", callback_data="ээ-20-01")
inline_btn_ee_20_02 = InlineKeyboardButton("ээ-20-02", callback_data="ээ-20-02")
inline_btn_ee_19_02 = InlineKeyboardButton("ээм-19-02", callback_data="ээм-19-02")
group_ey_kb = InlineKeyboardMarkup().add(inline_btn_vm_16_03, inline_btn_vm_17_01, inline_btn_vm_18_01, inline_btn_vm__19_01, inline_btn_vm_20_01, inline_btn_vmm__18_04, inline_btn_vmm_18_09, inline_btn_vmm_19_04, inline_btn_vmm_19_09, inline_btn_vmm_20_13, inline_btn_vem_18_09, inline_btn_vem_18_12, inline_btn_vem_19_12, inline_btn_vem_18_15, inline_btn_vem_20_09, inline_btn_zm_16_01, inline_btn_zm_17_01, inline_btn_zm_18_01, inline_btn_zm_19_01, inline_btn_ze_16_05, inline_btn_ze_17_01, inline_btn_ze_18_01, inline_btn_ze_19_01, inline_btn_em_17_03, inline_btn_em_18_04, inline_btn_em_19_03, inline_btn_em_20_03, inline_btn_emm_19_01, inline_btn_ee_17_01, inline_btn_ee_17_02, inline_btn_ee_18_01, inline_btn_ee_18_02, inline_btn_ee_18_03, inline_btn_ee_19_01, inline_btn_ee_19_02, inline_btn_ee_20_01, inline_btn_ee_20_02, inline_btn_ee_19_02)


ey = {
	"вм-16-03" : "6&groupId=2649",
	"вм-17-01" : "6&groupId=4683",
	"вм-18-01" : "6&groupId=5022",
	"вм-19-01" : "6&groupId=6512",
	"вм-20-01" : "6&groupId=7432",
	"вмм-18-04" : "6&groupId=5029",
	"вмм-18-09" : "6&groupId=5030",
	"вмм-19-04" : "6&groupId=6506",
	"вмм-19-09" : "6&groupId=6508",
	"вмм-20-13" : "6&groupId=7448",
	"вэм-18-09" : "6&groupId=5025",
	"вэм-18-12" : "6&groupId=5026",
	"вэм-19-12" : "6&groupId=6496",
	"вэм-19-15" : "6&groupId=6513",
	"вэм-20-09" : "6&groupId=7437",
	"зм-16-01" : "6&groupId=4175",
	"зм-17-01" : "6&groupId=4912",
	"зм-18-01" : "6&groupId=5037",
	"зм-19-01" : "6&groupId=6866",
	"зэ-16-05" : "6&groupId=4176",
	"зэ-17-01" : "6&groupId=4913",
	"зэ-18-01" : "6&groupId=5038",
	"зэ-19-01" : "6&groupId=6867",
	"эм-17-03" : "6&groupId=4664",
	"эм-18-04" : "6&groupId=5184",
	"эм-19-03" : "6&groupId=6349",
	"эм-20-03" : "6&groupId=7418",
	"эмм-19-01" : "6&groupId=6351",
	"ээ-17-01" : "6&groupId=4662",
	"ээ-17-02" : "6&groupId=4663",
	"ээ-18-01" : "6&groupId=5181",
	"ээ-18-02" : "6&groupId=5182",
	"ээ-18-03" : "6&groupId=5756",
	"ээ-19-01" : "6&groupId=6347",
	"ээ-19-02" : "6&groupId=6348",
	"ээ-20-01" : "6&groupId=7416",
	"ээ-20-02" : "6&groupId=7417",
	"ээм-19-02" : "6&groupId=6352"
}


inline_btn_vum_18_02 = InlineKeyboardButton("вюм-18-02", callback_data="вюм-18-02")
inline_btn_vum_18_03 = InlineKeyboardButton("вюм-18-03", callback_data="вюм-18-03")
inline_btn_vum_19_02 = InlineKeyboardButton("вюм-19-02", callback_data="вюм-19-02")
inline_btn_vum_19_03 = InlineKeyboardButton("вюм-19-03", callback_data="вюм-19-03")
inline_btn_vum_19_03 = InlineKeyboardButton("вюм-20-03", callback_data="вюм-20-03")
inline_btn_zu_16_03 = InlineKeyboardButton("зю-16-03", callback_data="зю-16-03")
inline_btn_zuv_18_01 = InlineKeyboardButton("зюв-18-01", callback_data="зюв-18-01")
inline_btn_zuv_19_01 = InlineKeyboardButton("зюв-19-01", callback_data="зюв-19-01")
inline_btn_ur_17_01 = InlineKeyboardButton("юр-17-01", callback_data="юр-17-01")
inline_btn_ur_17_02 = InlineKeyboardButton("юр-17-02", callback_data="юр-17-02")
inline_btn_ur_17_03 = InlineKeyboardButton("юр-17-03", callback_data="юр-17-03")
inline_btn_ur_17_04 = InlineKeyboardButton("юр-17-04", callback_data="юр-17-04")
inline_btn_ur_18_01 = InlineKeyboardButton("юр-18-01", callback_data="юр-18-01")
inline_btn_ur_18_02 = InlineKeyboardButton("юр-18-02", callback_data="юр-18-02")
inline_btn_ur_18_03 = InlineKeyboardButton("юр-18-03", callback_data="юр-18-03")
inline_btn_ur_18_04 = InlineKeyboardButton("юр-18-04", callback_data="юр-18-04")
inline_btn_ur_19_01 = InlineKeyboardButton("юр-19-01", callback_data="юр-19-01")
inline_btn_ur_19_02 = InlineKeyboardButton("юр-19-02", callback_data="юр-19-02")
inline_btn_ur_19_03 = InlineKeyboardButton("юр-19-03", callback_data="юр-19-03")
inline_btn_ur_20_01 = InlineKeyboardButton("юр-20-01", callback_data="юр-20-01")
inline_btn_ur_20_02 = InlineKeyboardButton("юр-20-02", callback_data="юр-20-02")
inline_btn_urm_19_04 = InlineKeyboardButton("юрм-19-04", callback_data="юрм-19-04")
inline_btn_urm_20_04 = InlineKeyboardButton("юрм-20-04", callback_data="юрм-20-04")
group_yu_kb = InlineKeyboardMarkup().add(inline_btn_vum_18_02, inline_btn_vum_18_03, inline_btn_vum_19_02, inline_btn_vum_19_03, inline_btn_vum_19_03, inline_btn_zu_16_03, inline_btn_zuv_18_01, inline_btn_zuv_19_01, inline_btn_ur_17_01, inline_btn_ur_17_02, inline_btn_ur_17_03, inline_btn_ur_17_04, inline_btn_ur_18_01, inline_btn_ur_18_02, inline_btn_ur_18_03, inline_btn_ur_18_04, inline_btn_ur_19_01, inline_btn_ur_19_02, inline_btn_ur_19_03, inline_btn_ur_20_01, inline_btn_ur_20_02, inline_btn_urm_19_04, inline_btn_urm_20_04)


yu = {
	"вюм-18-02" : "7&groupId=5034",
	"вюм-18-03" : "7&groupId=5035",
	"вюм-19-02" : "7&groupId=6398",
	"вюм-19-03" : "7&groupId=6399",
	"вюм-20-03" : "7&groupId=7445",
	"зю-16-03" : "7&groupId=4177",
	"зюв-18-01" : "7&groupId=5041",
	"зюв-19-01" : "7&groupId=6868",
	"юр-17-01" : "7&groupId=4621",
	"юр-17-02" : "7&groupId=4622",
	"юр-17-03" : "7&groupId=4623",
	"юр-17-04" : "7&groupId=4624",
	"юр-18-01" : "7&groupId=5016",
	"юр-18-02" : "7&groupId=5017",
	"юр-18-03" : "7&groupId=5018",
	"юр-18-04" : "7&groupId=5019",
	"юр-19-01" : "7&groupId=6376",
	"юр-19-02" : "7&groupId=6377",
	"юр-19-03" : "7&groupId=6378",
	"юр-20-01" : "7&groupId=6986",
	"юр-20-02" : "7&groupId=6987",
	"юрм-19-04" : "7&groupId=6397",
	"юрм-20-04" : "7&groupId=6989"
}


async def get_picture(f_id_and_gr_numb, moove='center'):
	opts = Options()
	opts.headless = True
	cap = DesiredCapabilities().FIREFOX
	cap["marionette"] = True #optional
	assert opts.headless
	if platform == "linux" or platform == "linux2":
		display = Display(visible=0, size=(1920, 1600))
		display.start()
		browser = webdriver.Firefox(capabilities=cap, options=opts)
	elif platform == "win32":
		browser = webdriver.Firefox(capabilities=cap, executable_path=r"O:\\Олег\\программирование\\python\\timetable-rtu\\geckodriver.exe", options=opts)
	browser.set_window_size('1920','1600')
	browser.get(("https://lk.gubkin.ru/schedule/#/activities/faculties?facultyId=" + f_id_and_gr_numb))
	await asyncio.sleep(5)
	if moove != 'center':
		actions = ActionChains(browser)
		if moove == 'next':
			button = browser.find_element_by_class_name('cp-date-switch-right')
			button.click()
		elif moove == 'previous':
			button = browser.find_element_by_class_name('cp-date-switch-left')
			button.click()
		await asyncio.sleep(1)
	browser.get_screenshot_as_file(f_id_and_gr_numb + '.png')
	browser.close()
	if platform == "linux" or platform == "linux2":
		display.stop()
	return True


@dp.message_handler(commands=['start', 'help'])
async def handle_start_help(message: types.Message):
	if not db.user_exists(message.from_user.id):
			db.add_user(message)
	await message.answer('Привет, данный бот поможет тебе узнать расписание РГУНГ \nсообщение разработчику - /mail *текст обращения*', reply_markup=start_kb)


@dp.callback_query_handler()
async def process_callback_button1(callback_query: types.CallbackQuery):
	global week_choose_temp
	await bot.answer_callback_query(callback_query.id)
	if (callback_query.data == 'week_save' or callback_query.data == 'week_saved' or callback_query.data == 'fack_save' or callback_query.data == 'fack_saved' or callback_query.data == 'group_save' or callback_query.data == 'group_saved'):
		if callback_query.data == 'week_save':
			db.save_week(callback_query.message.chat.id)
		elif callback_query.data == 'week_saved':
			db.remove_week(callback_query.message.chat.id)
			db.clear_week(callback_query.message.chat.id)
		elif callback_query.data == 'fack_save':
			db.save_fack(callback_query.message.chat.id)
		elif callback_query.data == 'fack_saved':
			db.remove_fack(callback_query.message.chat.id)
			db.clear_fack(callback_query.message.chat.id)
		elif callback_query.data == 'group_save':
			db.save_group(callback_query.message.chat.id)
		elif callback_query.data == 'group_saved':
			db.remove_group(callback_query.message.chat.id)
			db.clear_group(callback_query.message.chat.id)
		settings_kb = InlineKeyboardMarkup()
		if db.get_settings_status(callback_query.message.chat.id)[0][0][0] == 1:
			settings_kb.add(settings_btn_1_saved)
		else:
			settings_kb.add(settings_btn_1)
		if db.get_settings_status(callback_query.message.chat.id)[1][0][0] == 1:
			settings_kb.add(settings_btn_2_saved)
		else:
			settings_kb.add(settings_btn_2)
		if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1:
			settings_kb.add(settings_btn_3_saved)
		else:
			settings_kb.add(settings_btn_3)
		await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text='настройки: ', reply_markup=settings_kb)
	elif (callback_query.data== 'previous') or (callback_query.data== 'center') or (callback_query.data== 'next'):
		week_choose_temp = callback_query.data
		if db.get_settings_status(callback_query.message.chat.id)[1][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[1][0][0] != None:
			if db.get_settings(callback_query.message.chat.id)[1][0][0]=='kbtek' and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_kbtek_kb)
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='avt' and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_avt_kb)
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='ggng' and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_ggng_kb)
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='im' and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_im_kb)
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='meb' and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_meb_kb)
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='pseptt' and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_pseptt_kb)
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='rngm' and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_rngm_kb)
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='hte' and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_hte_kb)
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='ey' and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_ey_kb)
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='yu' and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_yu_kb)
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='kbtek' and db.get_settings(callback_query.message.chat.id)[2][0][0] != None:
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
				await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
				await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
				await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
				await asyncio.wait_for(get_picture(kbtek[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
				file = kbtek[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
				await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
				if platform == "linux" or platform == "linux2":
					system('sudo rm "' + file + '"')
				elif platform == "win32":
					system('del "' + file + '"')
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='avt' and db.get_settings(callback_query.message.chat.id)[2][0][0] != None:
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
				await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
				await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
				await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
				await asyncio.wait_for(get_picture(avt[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
				file = avt[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
				await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
				if platform == "linux" or platform == "linux2":
					system('sudo rm "' + file + '"')
				elif platform == "win32":
					system('del "' + file + '"')
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='ggng' and db.get_settings(callback_query.message.chat.id)[2][0][0] != None:
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
				await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
				await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
				await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
				await asyncio.wait_for(get_picture(ggng[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
				file = ggng[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
				await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
				if platform == "linux" or platform == "linux2":
					system('sudo rm "' + file + '"')
				elif platform == "win32":
					system('del "' + file + '"')
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='im' and db.get_settings(callback_query.message.chat.id)[2][0][0] != None:
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
				await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
				await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
				await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
				await asyncio.wait_for(get_picture(im[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
				file = im[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
				await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
				if platform == "linux" or platform == "linux2":
					system('sudo rm "' + file + '"')
				elif platform == "win32":
					system('del "' + file + '"')
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='meb' and db.get_settings(callback_query.message.chat.id)[2][0][0] != None:
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
				await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
				await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
				await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
				await asyncio.wait_for(get_picture(meb[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
				file = meb[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
				await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
				if platform == "linux" or platform == "linux2":
					system('sudo rm "' + file + '"')
				elif platform == "win32":
					system('del "' + file + '"')
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='pseptt' and db.get_settings(callback_query.message.chat.id)[2][0][0] != None:
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
				await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
				await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
				await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
				await asyncio.wait_for(get_picture(pseptt[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
				file = pseptt[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
				await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
				if platform == "linux" or platform == "linux2":
					system('sudo rm "' + file + '"')
				elif platform == "win32":
					system('del "' + file + '"')
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='rngm' and db.get_settings(callback_query.message.chat.id)[2][0][0] != None:
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
				await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
				await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
				await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
				await asyncio.wait_for(get_picture(rngm[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
				file = rngm[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
				await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
				if platform == "linux" or platform == "linux2":
					system('sudo rm "' + file + '"')
				elif platform == "win32":
					system('del "' + file + '"')
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='hte' and db.get_settings(callback_query.message.chat.id)[2][0][0] != None:
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
				await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
				await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
				await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
				await asyncio.wait_for(get_picture(hte[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
				file = hte[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
				await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
				if platform == "linux" or platform == "linux2":
					system('sudo rm "' + file + '"')
				elif platform == "win32":
					system('del "' + file + '"')
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='ey' and db.get_settings(callback_query.message.chat.id)[2][0][0] != None:
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
				await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
				await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
				await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
				await asyncio.wait_for(get_picture(ey[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
				file = ey[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
				await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
				if platform == "linux" or platform == "linux2":
					system('sudo rm "' + file + '"')
				elif platform == "win32":
					system('del "' + file + '"')
			elif db.get_settings(callback_query.message.chat.id)[1][0][0]=='yu' and db.get_settings(callback_query.message.chat.id)[2][0][0] != None:
				db.comand_statistic(db.get_settings(callback_query.message.chat.id)[1][0][0])
				await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
				await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
				await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
				await asyncio.wait_for(get_picture(yu[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
				file = yu[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
				await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
				if platform == "linux" or platform == "linux2":
					system('sudo rm "' + file + '"')
				elif platform == "win32":
					system('del "' + file + '"')
		else:
			await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text='Выбери факультет:', reply_markup=fk_choice_kb)
			if db.get_settings_status(callback_query.message.chat.id)[0][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[0][0][0] == None:
				db.add_week(callback_query.message.chat.id,callback_query.data)
	elif callback_query.data=='kbtek':
		db.comand_statistic(callback_query.data)
		if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] != None and (db.get_settings(callback_query.message.chat.id)[2][0][0] in kbtek):
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(kbtek[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
			file = kbtek[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		else:
			await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_kbtek_kb)
			if db.get_settings_status(callback_query.message.chat.id)[1][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[1][0][0] == None:
				db.add_fack(callback_query.message.chat.id,callback_query.data)
	elif callback_query.data=='avt':
		db.comand_statistic(callback_query.data)
		if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] != None and (db.get_settings(callback_query.message.chat.id)[2][0][0] in avt):
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(avt[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
			file = avt[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		else:
			await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_avt_kb)
			if db.get_settings_status(callback_query.message.chat.id)[1][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[1][0][0] == None:
				db.add_fack(callback_query.message.chat.id,callback_query.data)
	elif callback_query.data=='ggng':
		db.comand_statistic(callback_query.data)
		if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] != None and (db.get_settings(callback_query.message.chat.id)[2][0][0] in ggng):
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(ggng[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
			file = ggng[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		else:
			await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_ggng_kb)
			if db.get_settings_status(callback_query.message.chat.id)[1][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[1][0][0] == None:
				db.add_fack(callback_query.message.chat.id,callback_query.data)
	elif callback_query.data=='im':
		db.comand_statistic(callback_query.data)
		if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] != None and (db.get_settings(callback_query.message.chat.id)[2][0][0] in im):
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(im[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
			file = im[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		else:
			await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_im_kb)
			if db.get_settings_status(callback_query.message.chat.id)[1][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[1][0][0] == None:
				db.add_fack(callback_query.message.chat.id,callback_query.data)
	elif callback_query.data=='meb':
		db.comand_statistic(callback_query.data)
		if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] != None and (db.get_settings(callback_query.message.chat.id)[2][0][0] in meb):
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(meb[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
			file = meb[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		else:
			await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_meb_kb)
			if db.get_settings_status(callback_query.message.chat.id)[1][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[1][0][0] == None:
				db.add_fack(callback_query.message.chat.id,callback_query.data)
	elif callback_query.data=='pseptt':
		db.comand_statistic(callback_query.data)
		if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] != None and (db.get_settings(callback_query.message.chat.id)[2][0][0] in pseptt):
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(pseptt[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
			file = pseptt[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		else:
			await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_pseptt_kb)		
			if db.get_settings_status(callback_query.message.chat.id)[1][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[1][0][0] == None:
				db.add_fack(callback_query.message.chat.id,callback_query.data)
	elif callback_query.data=='rngm':
		db.comand_statistic(callback_query.data)
		if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] != None and (db.get_settings(callback_query.message.chat.id)[2][0][0] in rngm):
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(rngm[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
			file = rngm[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		else:
			await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_rngm_kb)		
			if db.get_settings_status(callback_query.message.chat.id)[1][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[1][0][0] == None:
				db.add_fack(callback_query.message.chat.id,callback_query.data)
	elif callback_query.data=='hte':
		db.comand_statistic(callback_query.data)
		if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] != None and (db.get_settings(callback_query.message.chat.id)[2][0][0] in hte):
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(hte[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
			file = hte[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		else:
			await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_hte_kb)		
			if db.get_settings_status(callback_query.message.chat.id)[1][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[1][0][0] == None:
				db.add_fack(callback_query.message.chat.id,callback_query.data)
	elif callback_query.data=='ey':
		db.comand_statistic(callback_query.data)
		if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] != None and (db.get_settings(callback_query.message.chat.id)[2][0][0] in ey):
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(ey[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
			file = ey[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		else:
			await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_ey_kb)
			if db.get_settings_status(callback_query.message.chat.id)[1][0][0] == 1 and db.get_settings(message.from_user.idcallback_query.message.chat.id)[1][0][0] == None:
				db.add_fack(message.from_user.idcallback_query.message.chat.id,callback_query.data)
	elif callback_query.data=='yu':
		db.comand_statistic(callback_query.data)
		if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] != None and (db.get_settings(callback_query.message.chat.id)[2][0][0] in yu):
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(yu[db.get_settings(callback_query.message.chat.id)[2][0][0]], moove = week_choose_temp), timeout=30.0)
			file = yu[db.get_settings(callback_query.message.chat.id)[2][0][0]] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		else:
			await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="Выбери группу:", reply_markup=group_yu_kb)
			if db.get_settings_status(callback_query.message.chat.id)[1][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[1][0][0] == None:
				db.add_fack(callback_query.message.chat.id,callback_query.data)
	else:
		if callback_query.data in kbtek:
			if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				db.add_group(callback_query.message.chat.id,callback_query.data)
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(kbtek[callback_query.data], moove = week_choose_temp), timeout=30.0)
			file = kbtek[callback_query.data] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'), reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		elif callback_query.data in meb:
			if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				db.add_group(callback_query.message.chat.id,callback_query.data)
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(meb[callback_query.data], moove = week_choose_temp), timeout=30.0)
			file = meb[callback_query.data] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'),reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		elif callback_query.data in avt:
			if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				db.add_group(callback_query.message.chat.id,callback_query.data)
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(avt[callback_query.data], moove = week_choose_temp), timeout=30.0)
			file = avt[callback_query.data] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'),reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		elif callback_query.data in im:
			if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				db.add_group(callback_query.message.chat.id,callback_query.data)
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(im[callback_query.data], moove = week_choose_temp), timeout=30.0)
			file = im[callback_query.data] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'),reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		elif callback_query.data in pseptt:
			if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				db.add_group(callback_query.message.chat.id,callback_query.data)
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(pseptt[callback_query.data], moove = week_choose_temp), timeout=30.0)
			file = pseptt[callback_query.data] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'),reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		elif callback_query.data in rngm:
			if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				db.add_group(callback_query.message.chat.id,callback_query.data)
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(rngm[callback_query.data], moove = week_choose_temp), timeout=30.0)
			file = rngm[callback_query.data] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'),reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')
		elif callback_query.data in hte:
			if db.get_settings_status(callback_query.message.chat.id)[2][0][0] == 1 and db.get_settings(callback_query.message.chat.id)[2][0][0] == None:
				db.add_group(callback_query.message.chat.id,callback_query.data)
			await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
			await bot.send_message(chat_id=callback_query.message.chat.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
			await bot.send_chat_action(chat_id=callback_query.message.chat.id, action='upload_photo')
			await asyncio.wait_for(get_picture(hte[callback_query.data], moove = week_choose_temp), timeout=30.0)
			file = hte[callback_query.data] + '.png'
			await bot.send_document(chat_id=callback_query.message.chat.id, document=open(file, 'rb'),reply_markup=start_kb)
			if platform == "linux" or platform == "linux2":
				system('sudo rm "' + file + '"')
			elif platform == "win32":
				system('del "' + file + '"')


@dp.message_handler(commands=['mail'])
async def handle_start_help(message: types.Message):
	if message.text.capitalize() == '/mail':
		await message.answer('Используйте: /mail текст сообщения...')
	else:
		await message.answer('Ваше обращение отправлено разработчику: \n\n{0}'.format(message.text.capitalize()[6:]))
		await bot.send_message(214196761, '{0} пишет: \n\n{1}'.format(message.from_user.id, message.text.capitalize()[6:]))


@dp.message_handler(content_types=['document', 'audio', 'sticker', 'photo', 'entities', 'animation', 'video', 'video_note', 'voice', 'contact', 'game', 'poll', 'location']) 
async def handle_docs_audio(message: types.Message):
	r = random.randint(0,2)
	if r == 0:
		await message.answer('Ого, файлик, прикольно')
	elif r == 1:
		await message.answer('я конечно посмотрю это на досуге, но это не то чем я обычно занимаюсь 🤖')
	elif r == 2:
		await message.answer('сделаю вид, что этого тут никогда не было...')


@dp.message_handler( content_types=['text'])
async def by_massage(message: types.Message):
	if not db.user_exists(message.from_user.id):
			db.add_user(message)
	if (message.text.capitalize() == 'Получить расписание'):
		if db.get_settings_status(message.from_user.id)[0][0][0] == 1 and db.get_settings(message.from_user.id)[0][0][0] != None:
			global week_choose_temp
			week_choose_temp = db.get_settings(message.from_user.id)[0][0][0]
			if db.get_settings_status(message.from_user.id)[1][0][0] == 1 and db.get_settings(message.from_user.id)[1][0][0] != None:
				if db.get_settings_status(message.from_user.id)[2][0][0] == 1 and db.get_settings(message.from_user.id)[2][0][0] != None:
					await bot.send_message(chat_id=message.from_user.id, text="Ожидайте, ваш запрос обрабатывается...", reply_markup= types.ReplyKeyboardRemove())
					await bot.send_chat_action(chat_id=message.from_user.id, action='upload_photo')
					f_get = db.get_settings(message.from_user.id)[1][0][0]
					f_get_2 = db.get_settings(message.from_user.id)[2][0][0]
					if f_get == 'kbtek':
						await asyncio.wait_for(get_picture(kbtek[db.get_settings(message.from_user.id)[2][0][0]], moove = db.get_settings(message.from_user.id)[0][0][0]), timeout=30.0)
						file = kbtek[db.get_settings(message.from_user.id)[2][0][0]] + '.png'
					elif f_get == 'avt':
						await asyncio.wait_for(get_picture(avt[db.get_settings(message.from_user.id)[2][0][0]], moove = db.get_settings(message.from_user.id)[0][0][0]), timeout=30.0)
						file = avt[db.get_settings(message.from_user.id)[2][0][0]] + '.png'
					elif f_get == 'ggng':
						await asyncio.wait_for(get_picture(ggng[db.get_settings(message.from_user.id)[2][0][0]], moove = db.get_settings(message.from_user.id)[0][0][0]), timeout=30.0)
						file = ggng[db.get_settings(message.from_user.id)[2][0][0]] + '.png'
					elif f_get == 'im':
						await asyncio.wait_for(get_picture(im[db.get_settings(message.from_user.id)[2][0][0]], moove = db.get_settings(message.from_user.id)[0][0][0]), timeout=30.0)
						file = im[db.get_settings(message.from_user.id)[2][0][0]] + '.png'
					elif f_get == 'meb':
						await asyncio.wait_for(get_picture(meb[db.get_settings(message.from_user.id)[2][0][0]], moove = db.get_settings(message.from_user.id)[0][0][0]), timeout=30.0)
						file = meb[db.get_settings(message.from_user.id)[2][0][0]] + '.png'
					elif f_get == 'pseptt':
						await asyncio.wait_for(get_picture(pseptt[db.get_settings(message.from_user.id)[2][0][0]], moove = db.get_settings(message.from_user.id)[0][0][0]), timeout=30.0)
						file = pseptt[db.get_settings(message.from_user.id)[2][0][0]] + '.png'
					elif f_get == 'rngm':
						await asyncio.wait_for(get_picture(rngm[db.get_settings(message.from_user.id)[2][0][0]], moove = db.get_settings(message.from_user.id)[0][0][0]), timeout=30.0)
						file = rngm[db.get_settings(message.from_user.id)[2][0][0]] + '.png'
					elif f_get == 'hte':
						await asyncio.wait_for(get_picture(hte[db.get_settings(message.from_user.id)[2][0][0]], moove = db.get_settings(message.from_user.id)[0][0][0]), timeout=30.0)
						file = hte[db.get_settings(message.from_user.id)[2][0][0]] + '.png'
					elif f_get == 'ey':
						await asyncio.wait_for(get_picture(ey[db.get_settings(message.from_user.id)[2][0][0]], moove = db.get_settings(message.from_user.id)[0][0][0]), timeout=30.0)
						file = ey[db.get_settings(message.from_user.id)[2][0][0]] + '.png'
					elif f_get == 'yu':
						await asyncio.wait_for(get_picture(yu[db.get_settings(message.from_user.id)[2][0][0]], moove = db.get_settings(message.from_user.id)[0][0][0]), timeout=30.0)
						file = yu[db.get_settings(message.from_user.id)[2][0][0]] + '.png'
					await bot.send_document(chat_id=message.from_user.id, document=open(file, 'rb'),reply_markup=start_kb)
					if platform == "linux" or platform == "linux2":
						system('sudo rm "' + file + '"')
					elif platform == "win32":
						system('del "' + file + '"')
				else:
					if db.get_settings(message.from_user.id)[1][0][0]=='kbtek':
						await message.answer("Выбери группу:", reply_markup=group_kbtek_kb)
						db.comand_statistic(db.get_settings(message.from_user.id)[1][0][0])
					elif db.get_settings(message.from_user.id)[1][0][0]=='avt':
						await message.answer("Выбери группу:", reply_markup=group_avt_kb)
						db.comand_statistic(db.get_settings(message.from_user.id)[2][0][0])
					elif db.get_settings(message.from_user.id)[1][0][0]=='ggng':
						await message.answer("Выбери группу:", reply_markup=group_ggng_kb)
						db.comand_statistic(db.get_settings(message.from_user.id)[2][0][0])
					elif db.get_settings(message.from_user.id)[1][0][0]=='im':
						await message.answer("Выбери группу:", reply_markup=group_im_kb)
						db.comand_statistic(db.get_settings(message.from_user.id)[2][0][0])
					elif db.get_settings(message.from_user.id)[1][0][0]=='meb':
						await message.answer("Выбери группу:", reply_markup=group_meb_kb)
						db.comand_statistic(db.get_settings(message.from_user.id)[2][0][0])
					elif db.get_settings(message.from_user.id)[1][0][0]=='pseptt':
						await message.answer("Выбери группу:", reply_markup=group_pseptt_kb)
						db.comand_statistic(db.get_settings(message.from_user.id)[2][0][0])
					elif db.get_settings(message.from_user.id)[1][0][0]=='rngm':
						await message.answer("Выбери группу:", reply_markup=group_rngm_kb)
						db.comand_statistic(db.get_settings(message.from_user.id)[2][0][0])
					elif db.get_settings(message.from_user.id)[1][0][0]=='hte':
						await message.answer("Выбери группу:", reply_markup=group_hte_kb)
						db.comand_statistic(db.get_settings(message.from_user.id)[2][0][0])
					elif db.get_settings(message.from_user.id)[1][0][0]=='ey':
						await message.answer("Выбери группу:", reply_markup=group_ey_kb)
						db.comand_statistic(db.get_settings(message.from_user.id)[2][0][0])
					elif db.get_settings(message.from_user.id)[1][0][0]=='yu':
						await message.answer("Выбери группу:", reply_markup=group_ye_kb)
						db.comand_statistic(db.get_settings(message.from_user.id)[2][0][0])
			else:
				await message.answer('Выбери факультет:', reply_markup=fk_choice_kb)
		else:
			await message.answer('Выбери неделю:', reply_markup=week_choose_kb)
		if not db.user_exists(message.from_user.id):
			db.add_user(message)
		db.user_used(message.from_user.id)
	elif (message.text.capitalize() == 'Настройки'):
		settings_kb = InlineKeyboardMarkup()
		if db.get_settings_status(message.from_user.id)[0][0][0] == 1:
			settings_kb.add(settings_btn_1_saved)
		else:
			settings_kb.add(settings_btn_1)
		if db.get_settings_status(message.from_user.id)[1][0][0] == 1:
			settings_kb.add(settings_btn_2_saved)
		else:
			settings_kb.add(settings_btn_2)
		if db.get_settings_status(message.from_user.id)[2][0][0] == 1:
			settings_kb.add(settings_btn_3_saved)
		else:
			settings_kb.add(settings_btn_3)
		await message.answer('Настройки:', reply_markup=settings_kb)
		await bot.send_message(message.from_user.id, 'При активации функции сохранения при следующем запросе расписания настройки будут сохранены и выставлены по умолчанию для последующих запросов')
	elif ((message.text.capitalize()[0:4] == 'Push') and (message.from_user.id == 214196761)):
		push_text = str(message.text[5:])
		await message.answer('Рассылка активирована')
		name = 0
		while name < (db.get_users()[-1][0]):
			try:
				await bot.send_message(db.get_users()[name][1], push_text)
			except:
				await bot.send_message(214196761, "ошибка рассылки для " + str(db.get_users()[name][1]))
			name +=1
	elif ((message.text.capitalize()[0:6] == 'Answer') and (message.from_user.id == 214196761)):
		await bot.send_message(message.text[7:16], 'Ответ от разработчика:\n\n{0}'.format(message.text[17:]))
	elif ((message.text.capitalize()[0:9] == 'Statistic') and (message.from_user.id == 214196761)):
		name = 0
		users = ''
		count_users = int(db.get_users()[-1][0])
		count_users_50=0
		while count_users > 50:
			count_users_50+=1
			count_users-=50
		if count_users > 0:
			count_users_50+=1
		for i in range(0,count_users_50):
			temp_count=0
			users = ''
			while temp_count < 50:
				try:
					users+=str(db.get_users()[name]) + '\n'
				except:
					pass
				name+=1
				temp_count+=1
			await bot.send_message(214196761, 'Пользователи:\n\n{0}'.format(users))
		command_numb = 0
		commands = ''
		while command_numb < (db.get_comand_statistic()[-1][0]):
			commands += str(db.get_comand_statistic()[command_numb]) + '\n'
			command_numb+=1
		await bot.send_message(214196761, 'Статистика команд:\n\n{0}'.format(commands))


if __name__ == '__main__':	
	executor.start_polling(dp, skip_updates=True)
	global week_choose_temp
	week_choose_temp = ''