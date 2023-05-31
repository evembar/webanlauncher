## Работа с WebanLauncher

Этот документ предназначен для пояснение работы данного лаунчера. 

## Немного о лаунчере

Лаунчер использует модификацию темы Tkinter - Customtkinter. Подробнее про его документацию https://customtkinter.tomschimansky.com/documentation/.
Также для скачивания файла он использует wget(модуль)
И для кастомных окон ошибок или инфы используется CTkMessagebox.
Установка этих библиотек делается через pip isntall ваша_библиотека

## Тема оформления

Если вы хотите поменять цвет кнопок, то впишите в скрипт WebAnLauncher.py следущее:

    customtkinter.set_default_color_theme("Ваш цвет")
Для изменения названия проги, измените 
эти строки

    des.title("Тут название проги")
Также измените название проги в poppup(окно об инфе или ошибке)

    CTkMessagebox(title="WebAnLiMaks Launcher", message=" WebAnLiMaks Launcher\nРазработал - WebMast \nЯзык - Python 3\nWebAnLiMaks 2023", icon  =  'logo.png')
   Эти строчки для этого

![](https://lh3.googleusercontent.com/ZR7BmkRJ3eVSNxMD9V-rLhvpSenFwWlzPFaBPqQ1exkwtr9XGacJPvFLUfQ_Cdt2n6a6rPtwHA7XS--T1IUFeW7_SLgan_9K6Bj8hcRbLFdBAgabzmFsvlsCXScxWWm9C-Ogb1GlVBQFgB5XR-doodl2-a38ZHcSYqiX4tfIF1LgxYat3mcDlDtr1_TOE-WDx37uPgwVj9GLrMR-GQn7KYGR72-2f6gWXo1qDi7naeTZx3vyj6WXMv395ASlYBVaSl30l_RR5sUB9nij0luGo2h3bkugkKWrEmFhxt4JThsCV3PABLgHwXeoSkuReJ3wAfnsDTi1vCpHs0OOIiAOmbNg5nphBVZjSXwdXb87249-ofrOMBeFk_O7E8wxMvC6YPndZDqcUaXlSw4Ky0wb65RJLKh1VTtClYMEcYmOrRIAiD90AtM7MSopfJUz6_AYv7nuRxeS-Mh4FdsA8DCkG3iVVFimoxMM124wjAgp4HPNLO_iuN5rQp-fsF2sEWQU-YXFMAJpA32uCpm4P1l-ZrA0mZCeuiHZALtFWd6y_pPkUG-tI6WDEU48kyexZKZoiTC4Q3GhdKC5eIfkLelt2uPUuuDCO8jIVPD8k6l5lgaDmlDHB_gyyYWTCpoOvPK8drKZ5U2iNxpfeLFpa5wmBnqEYFrB9_ntPx26YjPMQO2sgCdAlLcpXhJc6ME48MowCSOV2ZKqx_sXmYKfd6qJhOcipMF8WM9eN58wegoroK0hcuNRhbvTobP7ARWY3OWN7xuKmXNRd2zhmoLE6xZtLk1Oo6LQF2DsNT4bFQr3aIU2DH2boPFNeiRGsDqe5vbgbfMmX-doJ3TRh7Ot9mYNRbTapC4L100nU_XxMRlx-ldHxfjlSvPxCL_p9vhq7YYSq_RRGFMnz3-CE5rAjgyOeEjgf7TTj8oz6cbcbQb7AgnfmHI7cExhirZEXbfkEZ_xdhwXpQ7gFddpCGFKfKQ9pZVNnh_4nZPgZzSao56d2oXafTZX8Y0RbNa3=w1161-h653-s-no?authuser=0)
 
 Если вы хотите оставить только свое имя, в параметре text пишите в кавычках только свое имя или вас с другом. Между именами 18 пробелов. 
 
![](https://lh3.googleusercontent.com/HmNir--is2Jj1kCIX8tzJRxKYCBGWbnVQmOUDQWsM5RdnwaRa2uHIAGkOXOUSwmtgnYiuGzw66opcV790OpblNCi4YTDkz5wkGq8l3Lf0knOC0G6wiUzi6zBsZ2REXjM0Dln7Z56SwdTGCFxkpSPOYPssqjusFpeIOHox3OwotPjAA8lfrgBkOI9OUwQxA76HMbIimR8k7XoQZjKhGYt1nSpT0qnHksG38V4TIpUTLSoj6lwQhWkOqgnjIFenZJ5Xl4JTTP37nyLhCg2qtqIkPZa4nGzfGd_7YYe--yEToD1AS3NIbSkOT-a59ih0ioEd6ZCHylph1vRdb0M5jeRFbKpxo3qPoo6_lGkwc0SgmrGkzLsoYeTk5JVSwJuoZNMNYm6ni8IcyfA7Dx81BYwFoJPQ77hfBH6B-xTKJqQBaDH85TN_1ks18La8c_zidJo2uQr4KN5dU-rF_4qNwB9fJ31AzVvWicjHyxO1cTfpmHtmSf9Ie9rw_R1Z1SI5ZNYYT4ACo2N1BOPDwj27HPxrlYJTQ-59CrmbIGLoPJMHNoStOYSctFiR3TwR5XIUnNxS_suKrO9iUZCfsO1rSbwlJAbHNku06Tr94vImm8BZ6uPfWcUM4DPuQskOZ65TCavdK_9mk6DBGF4jlzkw3Vc18ovmfKhc621TksS7f20BXesAMPwj-fajo3VdUh-oSQhPnz4zHHt1NkmKKHbcuOm52yBOchNGk-mmlyAQAHwzMrHt1P64zGTCBFc7XPu69_ieae5VHn6P-4dI6MX-aS9npmFGOdYFEYeLOpBaOPIYWcIWKKZcxdsVeR2_pcoIJuRERai5LkwbBCkuBzPeJECoILGu2MqgIwJe_FTG34wMQr3TeRBaxweCGieuzhPgXHgNWB1u0ICWpWRVL-YaBcq1c_TueWkrJnrzpdCKBIX8DbBTHPpQ4Ptmc-kdpBVi1HMQ1UlDztmMbB5SbUWJLL50K7vJD7CwITZWh6IC9Ix56F-4OFowmNCIjgm=w1161-h653-s-no?authuser=0)

Для изменения ссылок на qiwi или donation alerts, измените ссылки в этих переменных qiwi_webmast и donal_maksimys.

Для изменения ссылок на telegram или youtube, измените ссылки в переменных tg_webmast и youtube_webmast для одного пользователя. Для второго аналогично, только после tg_ будет написан maksimys.

Если вы хотите убрать лишние кнопки youtube или telegram, то удаляйте из кода эти переменные. 

	
	tg_webmast_button  =  customtkinter.CTkButton(des, image  =  tg, text  =  '', width  =  25, height  =  25, command  =  get_tg_webmast)

	tg_webmast_button.place(x  =  285, y  =  430)

	  

	youtube_webmast_button  =  customtkinter.CTkButton(des, image  =  youtube, text  =  '', width  =  25, height  =  25, command  =  get_youtube_webmast)

	youtube_webmast_button.place(x  =  285, y  =  465)

	  

	tg_maksimys_button  =  customtkinter.CTkButton(des, image  =  tg, text  =  '', width  =  25, height  =  25, command  =  get_tg_maksimys)

	tg_maksimys_button.place(x  =  435, y  =  430)

	  

	youtube_maksimys_button  =  customtkinter.CTkButton(des, image  =  youtube, text  =  '', width  =  25, height  =  25, command  =  get_youtube_maksimys)

	youtube_maksimys_button.place(x  =  435, y  =  465)

Обратите внимание, что кнопки это все кнопки ютуба и телеги. Не умудритесь конкретно все удалить.

Что касается обложки игры, то меняйте фотку anonymous_poster в папке src/. Чтобы не менять пришлось название фотки, надо изменить в коде после src/ название фотки на свою:

	anonymous_poster  =  PhotoImage(file='src/anonymous_poster.png')

Если вы хотите убрать кнопки выбора версии, то удалите следующие переменные:

	radiotext  =  customtkinter.CTkLabel(des, text='Версия: ', font  = ('Colibri', 20))

	radiotext.place(x=400, y=100)

	  

	radio_var  =  IntVar(value=0)

	radiobutton_1  =  customtkinter.CTkRadioButton(des, text="1.0",

	command=radiobutton_event, variable=  radio_var, value=10)

	radiobutton_1.place(x=500,y  =  100)

	  

	radiobutton_2  =  customtkinter.CTkRadioButton(des, text="1.1",

	command=radiobutton_event, variable=  radio_var, value=11)

	radiobutton_2.place(x=500,y=130) 

После удаления после else пропишите следующее:

	play()

В этой функции уберите следущие строки: 

	if  anonymous_ver  ==  10:

		wget.download('https://github.com/evembar/webanlauncher/releases/download/o/anonymous_windows.webanlimax')

	else:

		wget.download('https://github.com/evembar/webanlauncher/releases/download/1.1/anonymous_windows.webanlimax')

И пропишите свою строку:
	
	wget.download('Ваша ссылка')

Обратите внимание после - этой строчки, где упоминается anonymous_windows ставьте свое название архива. Также в строке, где упоминается .webanlimax, ставьте свое, что была совместимость(архив.webanlimax - это переименованный zip архив). Также при упаковки игры надо, что в корне архива была только папка.
Названия для вхождения папки меняется в этой строке:

	os.chdir('Anonymous-full')

Название exe-шника меняется в этой строке:

	sost  =  os.system('start anonymous.exe')

Чтобы изменить ссылку на игру, меняйте значение переменной:

	about_anonymous  =  'https://evembar.github.io/webanlimaks/-Anonymous-chapter-full.html'

Чтобы изменить строку "Выбрана игра", измените параметр text:

	voted_text.configure(text  =  'Выбрана игра: Anonymous. In search of snus full version')

Чтобы изменить почту, меняйте в этом popup параметр text:

	CTkMessagebox(title="WebAnLiMaks Launcher", message=" По любым вопросам писать на этот адрес\n lbhnik12@gmail.com", icon  =  'gmail.png')

Для изменения иконки лаунчера, меняйте значение в:

	des.iconbitmap('иконка.ico')

# Сборка

Для сборки используйте батник compile.bat. После сборка он сам закроется. В папке dist будет лежать папка с названием скрипта. В неё добавьте папку src, customtkinter и CTkMessagebox. Все они лежат в папке со скриптом.

Вот такой подробный гайд получился. 

# Заключение

если что-то упустил или не понятно, пишите мне и я отвечу

[WebAnLiMaks](https://vk.com/webanlimaks)
