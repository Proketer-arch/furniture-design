# 14. Реестр источников

Дата сбора внешних источников: 2026-10-15; инженерное дополнение QA-01: 2026-10-16; сверка по оригиналам и новые источники (BL-25…BL-28, HT-07, HT-08, BY-05, BY-06, UH-04, GR-01…GR-03, SA-01, IF-01, MM-01, GL-11): 2026-10-19. Внешние ссылки открывались в сессии исследования через веб-инструменты. Если источник отдал искажённый текст (числа без подписей), это указано в колонке «Качество». В `rules.yaml` правила ссылаются на эти идентификаторы.

Теги достоверности (подробно — в [00-method.md](00-method.md)): **Н** норматив, **П** первичный документ производителя, **И** инженерная практика / пакет AFABRIK, **Р** ориентир (вторичный источник), **?** нужно решение.

Качество: **чётко** — значения и подписи читаются; **частично** — часть значений без подписей, использованы только однозначные; **справочно** — страница-каталог без размерных данных.

## 1. Пакет AFABRIK (исходные требования пользователя)

| ID | Что | Где |
|---|---|---|
| AF-01 | Пять DOCX S1–S5 → Markdown; правила K01–K19, W01–W13, вопросы C01–C12 | `docs/furniture-projecting-2026-10-15/` |

## 2. Blum

| ID | Документ | URL | Тег | Качество |
|---|---|---|---|---|
| BL-01 | LEGRABOX: ассортимент (высоты N/M/K/C/F, нагрузки, NL) | https://www.blum.com/kz/ru/products/boxsystems/legrabox/programme/ | П | чётко |
| BL-02 | MD-013/5 (04.24) LEGRABOX pure, инструкция по сборке | https://d2.blum.com/services/BEC003/lbx0001-md-013_md_dok_bau_$sall_$aof_$v5.pdf | П | частично: схемы без подписей; формулы дна и задней стенки подтверждены оригиналом BL-25 |
| BL-03 | MD-015/4 (04.24) LEGRABOX free, инструкция по сборке | https://d2.blum.com/services/BEC003/lbx0002-md-015_md_dok_bau_$sall_$aof_$v4.pdf | П | частично |
| BL-04 | LEGRABOX: размеры (09/2015), копия Richelieu | https://static.richelieu.com/documents/docsGr/117/711/5/1177115/1750793.pdf | П (старая редакция) | частично |
| BL-05 | LEGRABOX pure: планировочные данные (копия LDL) | https://www.ldlonline.co.uk/media/wysiwyg/others/media/legrabox-pure.pdf | П (копия) | частично |
| BL-06 | TANDEMBOX antaro EP-639/1 UK-UA/07.24: информация для заказа и проектирования | https://d2.blum.com/services/BEC003/cme108331_ep_dok_bau_$suk-ua_$aof_$v1.pdf | П | чётко (оригинал EP-639/1 прочитан полностью 2026-10-19; LT = NL + 3, дно и задняя стенка с подписями) |
| BL-07 | SPACE CORNER MA-493/0 (01.14), монтаж | https://demos-trade.cz/product-file/download/42203 | П (копия) | частично |
| BL-08 | SPACE CORNER: обзор (ширина 900–1200, 65 кг) | https://www.blum.com/kz/ru/products/cabinet-applications/space-corner/overview/ | П | чётко |
| BL-09 | SPACE TOWER td-082 v4: информация для проектирования | https://d2.blum.com/services/BEC003/box0036-td-082_td_dok_bau_$sru_$aof_$v4.pdf | П | частично; оригинал TD-082/4 прочитан 2026-10-19: высота SPACE TOWER 1684 (D-07 закрыт частично) |
| BL-10 | AVENTOS top EP-609/1 RU (09.23): информация для заказа и проектирования | https://antarion.by/upload/medialibrary/abb/z7g4uw6a1hp0aa9vk67h8nabehvfq8vj/AVENTOS top Информация для заказа и проектирования.pdf | П (копия дистрибьютора) | частично: таблицы HS/HL перемешаны |
| BL-11 | AVENTOS: общий обзор (типы, LF, мин. глубины) | https://antarion.by/upload/media_files_antarion/blum_media/aventos_media/obshhij-obzor-podemnyh-mehanizmov-aventos.pdf | П (копия, редакция не указана) | частично |
| BL-12 | AVENTOS HK-XS | https://www.fiera.ru/download/AVENTOS_HK-XS.pdf | П (копия) | чётко |
| BL-13 | AVENTOS HF и HK: страницы ассортимента | https://www.blum.com/kz/ru/products/liftsystems/aventos-hf/programme/ ; https://www.blum.com/kz/ru/products/liftsystems/aventos-hk/programme/ | П | справочно |
| BL-14 | AVENTOS HF top TD-142/3 EN 06.26 (читался в сессии; URL в заметках не сохранён) | требуется повторно получить с blum.com | П | не перепроверен в этой редакции базы; значения HF top в правилах взяты из BL-10; в правилах не цитируется |
| BL-15 | CLIP top BLUMOTION 110° для тонких фасадов (технические данные) | https://antarion.by/upload/media_files_antarion/blum_media/sistemy_petel_media/broshjura-tehnicheskoe-rukovodstvo-clip-top-blumotion-dlja-to… (адрес усечён в заметках) | П (копия) | частично |
| BL-16 | CLIP top BLUMOTION: информация для заказа и проектирования | https://antarion.by/upload/media_files_antarion/blum_media/sistemy_petel_media/broshjura-informacija-dlja-zakaza-proektirovanija-clip-top-bl… (адрес усечён) | П (копия) | частично |
| BL-17 | CLIP top BLUMOTION 155° с нулевым вхождением, TD-091/2 | https://antarion.by/upload/media_files_antarion/blum_media/sistemy_petel_media/broshjura-clip-top-blumotion-155°-s-nulevym-vhozhdeniem.pdf | П (копия) | частично |
| BL-18 | Каталог Blum 2024/25, стр. 119 (число петель по весу фасада) | https://publications.blum.com/2024/catalogue/en/119/ | П | частично |
| BL-19 | Blum: число петель (вес 4–6 → 2, 6–12 → 3; ширина ≤600, до 650 +1) | https://ea.blum.com/en/number-of-hinges/ | П | чётко |
| BL-20 | EXPANDO T (крепление тонких фасадов от 8 мм) | https://d2.blum.com/services/BEC003/clp0021-ep-392_ep_dok_bau_$sru_$aof_$v2.pdf | П | чётко |
| BL-21 | TIP-ON BLUMOTION EP-412/3 | https://d2.blum.com/services/BEC003/tob0010-ep-412_ep_dok_bau_$sbg-bg_$aof_$v3.pdf | П | чётко (модели S0…L5) |
| BL-22 | CLIP top BLUMOTION 110°: планировочные данные TD-148 | https://media.architectureau.com/media/files/TD-148_BAU%20Flyer%20AW3%20(1).pdf | П (копия) | частично |
| BL-23 | Спецификации петель Blum (пределы толщины двери) | https://cabinotch.us/media/wysiwyg/FAQ/BlumHingeSpecifications.pdf | Р (дилер) | частично |
| BL-24 | Каталог Blum 2022 и 2024/25: прочие страницы (60, 195–199, 273, 309, 335, 385; 70–125) | https://publications.blum.com/2024/catalogue/en/ (номер страницы в конце) | П | справочно/частично; в правилах не цитируется |
| BL-25 | LEGRABOX EP-390/5: информация для заказа и проектирования (оригинал с подписями; формулы дна LW−35 / NL−10 / NL−21, задняя LW−38) | https://www.blum.com/file/lbx0264-ep-390_ep_dok_bau?country=kz&language=ru | П | чётко (прочитан 2026-10-19) |
| BL-26 | MERIVOBOX EP-530/5: информация для заказа и проектирования (высоты N/M/K/E, дно LW−51 × NL−26, LT = NL + 3) | https://www.blum.com/file/me25532842_ep_dok_bau?country=kz&language=ru | П | чётко (прочитан 2026-10-19) |
| BL-27 | CLIP top BLUMOTION EP-150/4: формулы наложения (110° стандартная и специальная, 155°), таблица минимальных зазоров 16–26 | https://www.blum.com/file/clp0007-ep-150_ep_dok_bau?country=kz&language=ru | П | чётко (стр. 20–25, прочитан 2026-10-19) |
| BL-28 | AVENTOS top EP-609/3: диапазоны KH, минимальные глубины, формулы HK top и HK-XS, FAo (ссылка из заметок проекта; соответствие коду EP-609/3 проверено по тексту файла) | https://www.blum.com/file/cme83198_ep_dok_bau?country=kz&language=ru | П | чётко (прочитан 2026-10-19) |

## 3. Hettich

| ID | Документ | URL | Тег | Качество |
|---|---|---|---|---|
| HT-01 | InnoTech Atira: аргументационная папка | https://www.hettich.com/fileadmin/Media_Center/Catalogue/02_Argumentationsfolder_InnoTech_Atira_ru.pdf | П | чётко |
| HT-02 | Каталог TuI RU: ArciTech, монтажная ситуация (bk_432, 434, 436, 438) | https://catalog.hettich.com/General/TuI/ru_RU/catalogs/TuI_ru_RU/pdf/save/bk_432.pdf (и далее) | П | частично: подписи схем перемешаны |
| HT-03 | Каталог TuI RU: Easys и минимальные размеры (bk_565 и соседние bk_560–590) | https://catalog.hettich.com/General/TuI/ru_RU/catalogs/TuI_ru_RU/pdf/save/bk_565.pdf | П | частично |
| HT-04 | Sensys 2016 (RU) | https://www.hettich.com/fileadmin/Media_Center/Catalogue/Sensys_2016_HFT_RU_16275.pdf | П | частично |
| HT-05 | Откидные фасады: Lift Advanced (HF, HK, HL, HS) | https://hta.hettich.com/en-ca/flap-fittings/lift-advanced ; https://web.hettich.com/fileadmin/Media_Center/11_General/01_Catalogues/TA_2016_01_en_DE_03_Flap_fittings.pdf ; https://catalog.hettich.com/General/TA_2023/de_DE/catalogs/TA_2023_de_DE/pdf/save/bk_224.pdf | П | частично |
| HT-06 | Hettich Product Guide 2022 | https://www.hettich.com/fileadmin/Media_Center/Catalogue/Hettich_Product_Guide_2022_HAU.pdf | П | справочно; в правилах не цитируется |
| HT-07 | InnoTech Atira, каталог 2024: формулы BB / RB / BL, таблица минимальных глубин, EB, PL / RL | https://www.eboss.co.nz/assets/literature/371/53310/2024_-InnoTech-Atira-Catalogue.pdf | П (копия дистрибьютора) | чётко (прочитан 2026-10-19) |
| HT-08 | AvanTech YOU, каталог 2020: BB / RB = LB − 24, BL = NL − 26 / NL − 21, LT, нагрузки (URL не сохранён; файл — avantech_you_2020.pdf в рабочей копии сессии) | вернуться на hettich.com, раздел AvanTech YOU | П | чётко (прочитан 2026-10-19) |

## 4. Boyard

| ID | Документ | URL | Тег | Качество |
|---|---|---|---|---|
| BY-01 | Каталог BOYARD онлайн: системы выдвижения, петли, EVO | https://www.boyard.biz/catalog/slide_systems ; https://www.boyard.biz/catalog/hinges_systems ; https://www.boyard.biz/catalog/hinges_systems/evo | П | справочно/чётко |
| BY-02 | Каталог функциональной фурнитуры BOYARD 2024 (PDF, 36,8 МБ) | https://www.boyard.biz/storage/docs/Каталог-функциональной-фурнитуры-BOYARD-2024.pdf | П | страницы читались фрагментами (формат FlippingBook) |
| BY-03 | Каталог лицевой фурнитуры BOYARD 2024 (PDF, 14,1 МБ) | https://www.boyard.biz/storage/docs/Каталог-лицевой-фурнитуры-BOYARD-2024.pdf | П | справочно; в правилах не цитируется |
| BY-04 | B-Box (Boyard), описание | https://algraf.ru/sistema-vydvizheniya-b-box-boyard | Р | частично; в правилах не цитируется |
| BY-05 | Boyard DB9891 (400–500): паспорт скрытой направляющей — NL + 3, длина дна NL − 10, ширина дна LW − 50, нагрузки, шаги присадки | https://www.boyard.biz/catalog/slide_systems (карточка DB9891, PDF DB9891_400-500) | П | чётко (прочитан 2026-10-19) |
| BY-06 | Boyard START SB40W.1/450 и SB18W.1/270: паспорта (боковина 167, проём 203, зазор 4–6, рейка PUSH, труба SBS12); формул дна нет | https://www.boyard.biz/catalog/slide_systems/start_soft | П | чётко по перечисленному; формулы дна отсутствуют |

## 5. Unihopper, GTV

| ID | Документ | URL | Тег | Качество |
|---|---|---|---|---|
| UH-01 | Unihopper Magic Box и направляющие скрытого монтажа | https://unihopper.ru/unihopper-magic-box-2649-2/ ; https://unihopper.ru/inner-magic-box-2821/ ; https://unihopper.ru/concealed-slides-2807/ | П | справочно (без формул) |
| UH-02 | Unihopper Magicbox H80, инструкция (ManualsLib, фрагмент) | https://www.manualslib.com/manual/1903692/Unihopper-Magicbox-H80.html | П | частично; нужные формулы LW−35 / LW−38 читаются |
| UH-03 | Каталог и инструкции Unihopper (Яндекс.Диск, закрыт для роботов) | https://disk.yandex.ru/d/lfMVJxuWdXxrBQ | П | не прочитан (robots); заменён UH-04 с официального сайта |
| GT-01 | GTV Axis Pro | https://e-mf.msk.ru/retractable_systems/gtv_axis_pro/ ; https://gtv-rus.com.ru/images/rrrfiles/digital/foldery/08.11_AXIS_PRO.pdf ; https://gtv.com.pl/wp-content/uploads/2026/07/EN-RU_AXIS_PRO_30-04-2026-online.pdf | П | частично |
| UH-04 | Unihopper, фирменный каталог «Система выдвижных ящиков»: Magic Box (дно LW−35 × NL−10, NL + 5, проём A + 45) и POBOX H130 (дно LW−81 × NL−9, задняя LW−84, проём 160) | https://unihopper.pro/company/docs/ ; Magic Box: https://unihopper.pro/upload/iblock/ada/7odtux8zc9x5vvkw9wp4t0v2t11md5pb.pdf ; POBOX: https://unihopper.pro/upload/iblock/ba3/eovot18z3h7zkgc712qst8sjhkw95mke.pdf | П | чётко (прочитан 2026-10-19) |

## 5.1. Grass, Salice, Italiana Ferramenta, Makmart (добавлено 2026-10-19)

| ID | Документ | URL | Тег | Качество |
|---|---|---|---|---|
| GR-01 | Grass Nova Pro Scala, документ 110074-09/2018: EB, BB = LWK − 2·EB, BL = NL − 19 / NL − 13, MET = NL + 3 / NL + 12 (URL не сохранён; файл scala110074.pdf в рабочей копии сессии) | вернуться на grass.at или к дистрибьютору | П | чётко (прочитан 2026-10-19) |
| GR-02 | Grass Nova Pro Scala H250, документ 113691 (высота 250) | URL не сохранён (scala_h250.pdf) | П | частично |
| GR-03 | Grass Tiomos 110° (справочная страница Häfele 9.52): Ø35, толщина до 24, ограничение угла 85° | https://www.hafele.com (страница 9.52; URL точной страницы не сохранён) | П (дистрибьютор) | частично |
| SA-01 | Salice Silentia+ 94° / 105°: коды плеча (crank) A / D / G / P, формулы D и A, регулировка, число петель (график) | https://www.cabinetmakerwarehouse.com/wp-content/uploads/Salice_Silentia_Series_-100_105_Degree_Frameless_Hinge.pdf ; полный каталог — файл silentia_cat.pdf (URL не сохранён) | П (копия дистрибьютора) | частично: каталог американский, массы в lbs |
| IF-01 | Italiana Ferramenta Kimana (петля Ø26, 90°) | URL не сохранён (kimana.pdf) | П | частично |
| MM-01 | Makmart SC 1764/A: инструкция по сборке стандартного ящика с релингами (дно и задняя LW−79, Lu, F = LW−31, D) | https://www.makmart.ru (SC 1764/A, 11.11) | П | чётко (прочитан 2026-10-19) |

## 6. Нормативы, поставщик, профили, остров, техника, рынок

| ID | Документ | URL | Тег | Качество |
|---|---|---|---|---|
| NR-01 | ГОСТ 13025.1-85, таблица 6 (текст редакции 1990; действующую редакцию 17.05.2005 не видел) | https://www.kontur-extern.ru/info/normativ/document/9/235402-mebel-bytovaya-funktsionalnye-razmery-otdeleniy-dlya-khraneniya-gost-13025-1-85 | Н | чётко |
| MD-01 | МДМ-Комплект, техническая справка по петлям Ferrari | https://cdn.mdm-complect.ru/PDF/hinges_tech-inf.pdf | П/Р (поставщик пользователя) | частично |
| MD-02 | МДМ-Комплект K12_tab | https://cdn.mdm-complect.ru/PDF/K12_tab.pdf | П/Р | не использован для чисел |
| GL-01 | Emuca: Gola Upper (внутренняя глубина 19, зазор 37, ≥2 до двери) | https://www.emuca.com/kitchen/gola-profile-e/horizontal-gola-e-profile/upper-profile | П (Emuca) | чётко |
| GL-02 | Emuca: Gola-R Central, длины 2,35 и 3,9 м | https://www.emuca.com/kitchen/gola-profile-e/horizontal-gola-e-profile/central-gola-r-profile-for-kitchen-furniture | П | справочно |
| GL-03 | Würth: Gola Horizontal C (26×72,7) и L (27×56), 4000 мм | https://wurthlac.com/product/167461/4000mm-Gola-Horizontal-C-Profile-Stainless-Steel ; https://wurthlac.com/product/167460/4000mm-Gola-Horizontal-L-Profile-Stainless-Steel | П | чётко |
| GL-04 | Richelieu: Gola Wall Unit Profile | https://www.richelieu.com/us/en/category/moldings-corbels-and-components/metal-and-pvc-moldings-profiles-and-rails/molding-samples-and-packa… | П | справочно |
| GL-05 | Gloria Kuhni: профиль Gola (40–45 мм) | https://gloriakuhni.ru/kuhni/profil-gola | Р | частично |
| GL-06 | stroy-podskazka: размеры вертикальных профилей | https://stroy-podskazka.ru/stroitelnyj-profil/gola/ | Р | частично |
| GL-07 | Форум мебельщиков: расчёт высоты фасадов с Gola (зазор под ручку 30–35, свес 5/10) | https://forum.sdelaimebel.ru/topic/33074-integrirovannaya-ruchka-profil-gola-kak-rasschitat-vyisotu-fasadov/ | Р | частично |
| GL-08 | Руководство по Gola (mebelkomplekt.ru): уменьшение высоты фасада, цоколь +60, длины 1000/2000/3000/4100 | https://mebelkomplekt.ru/wp-content/uploads/2022/11/MEBEL-DLYA-KUHNI-GOLA-_2022.10.pdf | П (производитель мебели) | чётко; прочитан полностью 2026-10-19 (редакция 2022.10, 20 стр.); припуск реза в тексте не найден |
| GL-09 | Статья по Gola (inner.su) | прочитана в сессии; URL не сохранён | Р | не перепроверен, использован как ориентир; в правилах не цитируется |
| GL-10 | Stavros: профильные ручки и Gola (длины 250–2200, высоты фасадов, ограничения) | https://www.stavros.ru/articles/profilnye-ruchki-i-gola-dlya-kukhni-kak-vybrat-skrytuyu-ruchku-dlya-fasadov/ | Р | чётко |
| GL-11 | Makmart GOLA Trend: 4464.33P (профиль горизонтальный, одно закругление, 26 × 56,5, 4200 мм, заглушки, угол 90°, держатели SU116.DS59 / SU136.DS59), 5954 (LED, 27 × 56,4) | https://www.makmart.ru (каталожные листы GOLA Trend; URL файла не сохранён) | П | чётко (прочитан 2026-10-19) |
| IS-01 | Gloria Kuhni: кухня с островом (проходы, свесы, глубина) | https://gloriakuhni.ru/blog/kuhnya-s-ostrovom-razmery-rasstoyaniya-planirovka | Р | чётко |
| IS-02 | JLC Online / NKBA (42″ и 48″ проходы, 24″ на место) | https://www.jlconline.com/remodeling/guidlines-for-kitchen-island-functionality | Н/Р (США) | чётко |
| IS-03 | Antares: оптимальная высота кухни и шкафов | https://www.antarescompany.ru/poleznye-materialy/optimal-naya-vysota-kuhni-i-kuhonnyh-shkafov/ | Р | чётко |
| IS-04 | Сборка мебели (Киев): стандарты кухни | https://sborkamebeli.kiev.ua/standarti-kuhni/ | Р | чётко |
| IS-05 | Табуретка: расчёт размеров кухни | https://www.taburetka.ua/ru/stati/kak-rasschitat-razmery-kuhni-prakticheskie-sovety-729 | Р | чётко |
| AP-01 | Hausdorf: размеры встраиваемых холодильников | https://www.hausdorf.ru/articles/razmery-vstraivaemykh-kholodilnikov.html | Р | чётко |
| AP-02 | iChip: ниша встраиваемой посудомоечной машины | https://ichip.ru/sovety/pokupka/razmery-vstraivaemoj-posudomoechnoj-mashiny-dlya-kuhni-923952 | Р | чётко |
| AP-03 | Samsung: размеры духового шкафа и ниши | https://www.samsung.com/ru/home-appliances/buying-guide/how-to-choose-the-oven-dimension/ | Р | чётко |
| MK-01 | BFM: 18-й пакет санкций ЕС, фурнитура (07–08.2025) | https://www.bfm.ru/news/580567 | Р | чётко |
| MK-02 | medyn.su: Blum, Hettich и аналоги (15.11.2025) | https://medyn.su/materialy-i-fasady-kuhon/furnitura-blum-hettich/ | Р | чётко |
| MK-03 | МК Savio: 10 брендов фурнитуры | https://mk-savio.ru/zhurnal-eksperta-korpusnaya-mebel/furnitura-dlya-kuhni-razbiraem-10-brendov-ot-premium-do-ekonom/ | Р | чётко |
| MK-04 | Альта-Софт / Бизнес-ФМ: бизнес перестраивается после ограничений (11.08.2025) | https://www.alta.ru/external_news/120880/ | Р | чётко; направляющие в статье не упомянуты |
| MK-05 | ООО «Вереск» (shkaf-kupe.ru): сравнение Blum, Hettich, Boyard (21.05.2026) | https://www.shkaf-kupe.ru/article/chestnoe-sravnenie-blum-hettich-boyard/ | Р | блог мебельной фабрики; цифры ресурса и цен без методики |
| MK-06 | tdmspb.ru: страница бренда Blum, позиции «в наличии» (дата страницы не указана) | https://tdmspb.ru/info/brands/furnitura-blum/ | Р | подтверждает наличие у розницы; дата неизвестна |
| MK-07 | РБК Исследования рынков: рынок мебельной фурнитуры в России (анонс выпуска 2023; издания 2024–2026) | https://marketing.rbc.ru/research/issue/75601/ | Р | анонс: импорт более 91 % рынка (2022), Китай более 73 % импорта; санкционный раздел не виден |
| MK-08 | Fidal: 20-й пакет санкций ЕС (28.04.2026) | https://www.fidal.com/en/news/adoption-20th-sanctions-package-against-russia | Р | в обзоре фурнитура не упомянута; перечень открытый («etc.»), полный текст регламента не проверен |

## 7. Недоступные источники (попытки без результата)

- `manualslib.com` и `disk.yandex.ru` — robots; полный PDF Unihopper с этих адресов получить не удалось (каталог получен с официального сайта — UH-04).
- `newfurnitura.ru` — ошибка клиента; `mdm-complect.ru:443` — ошибка сервера (рабочий адрес — `cdn.mdm-complect.ru`).
- `spb.expo-torg.ru` — бинарный PDF, текст не извлечён.
- `unihopper.com` — редирект на посторонний wiki-сайт; не использовался.
- `www.mdm-complect.ru` — запрет роботов (robots): чертёж и каталожные листы Gola МДМ-Комплект не получены; Gola взят из Makmart GOLA Trend (GL-11) и руководства Мебелькомплект (GL-08); чертёж профиля МДМ запрашивается у владельца (D-12).
- URL ряда файлов, скачанных 2026-10-19 (HT-08, GR-01, GR-02, GR-03, IF-01, SA-01 полный каталог, GL-11), в заметках сессии не сохранились; файлы доступны только в рабочей копии сессии.
- Каталог Hettich RU: страницы bk_420–bk_610 открывались, но размерных формул ArciTech/AvanTech YOU для **ArciTech** нашлись только на bk_432–bk_438 (используются), для **AvanTech YOU** формулы дна и задней стенки найдены позже в каталоге 2020 года (HT-08).

## 8. Инженерные дополнения по аудиту

| ID | Что | Где | Тег | Граница достоверности |
|---|---|---|---|---|
| QA-01 | Выводы аудита сборки: открытый стык фартука, пересечение цоколя с боковинами/опорами, отсутствие повторной проверки после изменения ПММ | [Метод и обезличенные численные примеры](15-project-assembly-and-acceptance.md) | И | Дополнение процесса от 2026-10-16; не норматив и не источник размеров конкретной фурнитуры. Проверка арифметики примеров не заменяет чтение SKP. |
