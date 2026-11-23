# 08. Реестр источников

Дата сбора: 23.11.2026. Внешние страницы открывались веб-инструментами в сессии исследования. Если страница не открылась и число взято из поисковой выдачи, это сказано в колонке «Качество»; такие числа помечены тегом **Р** или вынесены в открытые данные ([07](07-conflicts-and-questions.md)). Правила в `rules.yaml` ссылаются на идентификаторы ниже.

Теги: **Н** норматив, **П** документ производителя, **Р** ориентир (форум, статья, магазин), **И** практика или решение AFABRIK.

## 1. AFABRIK и решения владельца

| ID | Что | Где | Тег |
|---|---|---|---|
| AF-01 | Пакет AFABRIK: W01–W13, ТЗ шкафа (поля W-R, W-B, W-S, W-Z, W-D, W-I, W-E), C01–C12 | [01-design-base.md](../furniture-projecting-2026-10-15/instructions/01-design-base.md), [wardrobe-brief.md](../furniture-projecting-2026-10-15/specifications/wardrobe-brief.md) | И |
| OW-01 | Уточнения владельца 23.11.2026: корпус всегда ЛДСП 16; фасады 16, 18 и толще; задние стенки — ХДФ 4 в паз (отступ 16, занимает 20), ЛДСП 8–9 в четверть (занимает 8–9), ЛДСП 16 между боковинами (не подтверждено); накладная ХДФ не применяется; глубина корпуса — по боковине | Передано через сессию проверки правил кухни; для кухни внесено в PR furniture-design#2 (R-CAR-02, R-CAR-04) | И |
| KR-01 | База правил кухни и решения 23.11.2026 по практике СНГ: фасад = модуль − 3 (R-DIM-07), не смешивать бренды (R-SUP-01), выбор и число петель (R-HNG-01, R-HNG-02, R-HNG-04), масса фасада (R-FRN-04), добор у стены (R-JNC-08) | [база кухни](../kitchen-construction-rules-2026-10-15/README.md) | И |

## 2. Нормативы

| ID | Документ | URL | Тег | Качество |
|---|---|---|---|---|
| NR-01 | ГОСТ 13025.1-85 «Мебель бытовая. Функциональные размеры отделений для хранения» (с Изм. 1–3): пп. 2.2, 2.3, 3.1, 3.3, 7, 8.1; табл. 1, 2, 5; черт. 1 и 2 | https://meganorm.ru/Data2/1/4294838/4294838129.htm | Н | чётко; черт. 1 и 2 прочитаны как изображения: 560 min, 1400 min, 900 min, 50 min, 170 min |
| NR-02 | ГОСТ 16371-2014 «Мебель. Общие технические условия»: пп. 5.2.1 (табл. 1), 5.2.2, 5.2.3, 5.2.8 (табл. 2), 5.2.26, 5.2.30 (табл. 3), 5.2.31 (табл. 4) | https://meganorm.ru/mega_doc/norm/gost_gosudarstvennyj-standart/18/gost_16371-2014_mezhgosudarstvennyy_standart_mebel_obshchie.html | Н | чётко, кроме табл. 4 (устойчивость) — ячейки извлеклись не полностью (D-08) |
| NR-03 | ГОСТ 19882-91 «Мебель корпусная. Методы испытаний на устойчивость, прочность и деформируемость»: п. 1.6 (нагрузки q_F, q_L), пп. 8.2–8.6, прил. 2 | https://meganorm.ru/Data2/1/4294833/4294833545.htm | Н | чётко |
| NR-04 | ГОСТ 28102-89 (методы испытаний штанг) | https://meganorm.ru/Data2/1/4294826/4294826673.htm | Н | справочно; в правилах не цитируется отдельно |

## 3. Системы купе

| ID | Документ | URL | Тег | Качество |
|---|---|---|---|---|
| AR-01 | Каталог продукции ARISTO 2020 (PDF дилера): «Стандарт», «Эконом», NOVA, SLIM LINE, «4 в 1» — формулы створок и вставок, пределы, соотношение H : W | https://aristo-chel.ru/wp-content/uploads/2020/03/Katalog_produkcii_ARISTO_2020.pdf | П | чётко по тексту; привязка формул к профилям — по подписям страниц, ключевые строки сверены вручную (Нпр − 40, (L + 25)/2, Ннап − 57, Вкр = Вшк − 93, 4/1 и 3/1) |
| AR-02 | ARISTO «Допустимые размеры и нагрузки» (BRAVO, штанги) | https://www.aristo.expert/upload/iblock/5c6/yhhb7rc1b8gqj5cw3mdkh12dir99mvk7/Sistemy-ARISTO-Dopustimye-razmery-i-nagruzki.pdf | П | не открылся; числа из поисковой выдачи |
| RP-01 | Raumplus, инструкция «Серия 1200», версия 1.7 (2016) | https://raumplus.ua/image/catalog/instrukcii/s_1200.pdf | П | чётко (Нпр − 45, перехлёст 12, 500–1800 × 700–3500, 180 кг) |
| RP-02 | Листовка Raumplus (направляющие, пределы систем, ролик 80 кг, доводчик 750) | https://fdkm.ru/images/doc/raumplus/Listovka_raumplus.pdf | П | чётко; копия дилера |
| KM-01 | «Командор»: каталог дверей-купе (нагрузка на ролик 25 кг) | https://business.td-komandor.ru/katalog/dveri-kupe | П | частично; документы с формулами закрыты (403), D-01 |

## 4. Петли, пантографы, опоры

| ID | Документ | URL | Тег | Качество |
|---|---|---|---|---|
| BL-01 | Blum: число петель по массе и ширине двери | https://ea.blum.com/en/number-of-hinges/ | П | чётко |
| BL-02 | Blum: ограничители угла для петель 155° (92° — ящик не задевает дверь, 110° — защита ручки) | https://ea.blum.com/en/opening-angle-stops-155-hinges/ | П | чётко |
| BL-03 | Blum, каталог петель (США): график числа петель, правило «расстояние между крайними петлями больше ширины двери» | https://s3.amazonaws.com/s3-absupply-net/pdf/blum_hinge_catalog.pdf | П | частично: высоты считаны с графика |
| HT-01 | Hettich, техническая информация по петлям (копия каталога, стр. 216–217): число петель по высоте и массе, отступ 60–100, расстояние ≥ 280 | https://www.lignoshop.de/out/media/hettich-scharniere-techn-infos.pdf | П | чётко; копия продавца |
| HT-02 | Hettich Duo Lift Basic (пантограф): 600–830 / 830–1150, 10 кг | https://shop.hettich.com/kg_RO/Alte-produse/Sisteme-de-depozitare/Compartimentare-corp-mobilier/Suporturi-%C3%AEmbr%C4%83c%C4%83minte/Duo-Lift-Basic-830---1150-mm/p/9079720 | П | чётко |
| HT-03 | Hettich Korrekt: опоры под цоколь 70/80/100, 450 кг | https://shop.hettich.com/ge_EN/Further-products/Plinth-adjustment-fittings/Korrekt-height-adjustable-leg%2C-450-kg-each/Korrekt-levelling-foot%2C-Plinth-height-70/p/9306015 | П | чётко |
| HT-04 | Hettich: выдвижной держатель плечиков на Quadro, KT 350, 25 кг | https://shop.hettich.com/md_EN/Verdere-producten/wandkastinrichting/Kledingkastinrichting/Kleerhangerhouder/Kleerhangerhouder-met-ladegeleider-op-Quadro-basis%2C-350-mm%2C-zilver/p/9136276 | П | из поисковой выдачи, D-02 |
| HT-05 | Hettich: выпрямитель фасада с алюминиевой крышкой, фасад 18–30, высота до 2600 | https://shop.hettich.com/mt_RU/Sliding-door-systems/Accessories-for-sliding-door-systems/Adjustment-fittings/Adjustment-fitting-with-aluminium-cover/p/9252651 | П | чётко; изделие из раздела раздвижных дверей |
| HF-01 | Häfele, пантографы (через продавца): 560–950 / 10 кг; 870–1190 / 15 кг | https://www.hwt-pro.com/en/cupboard-kitchen-fittings/coat-lifts/3796/ | П | чётко для первой модели; вторая — из выдачи |
| MD-01 | МДМ-Комплект, техническая справка по петлям Ferrari: число петель по высоте и массе, зазор 1,5, «фасад уже короба на 3» | https://www.mdm-complect.ru/PDF/hinges_tech-inf.pdf | П | чётко |
| IK-01 | IKEA PAX: крепление к стене | https://www.ikea.com/us/en/customer-service/pax-wall-anchoring-pub3b2d6060 | П | чётко |

## 5. Форумы, статьи, калькуляторы

| ID | Что | URL | Тег | Качество |
|---|---|---|---|---|
| FR-01 | Форум «Сделай мебель»: максимальная длина полки из ДСП | https://forum.sdelaimebel.ru/topic/1471-maksimalnaya-dlina-polki-iz-dsp/ | Р | чётко |
| FR-02 | Форум «Сделай мебель»: ящики под дверями купе | https://forum.sdelaimebel.ru/topic/14111-vyidvizhnyie-yashhiki-pod-dvertsami-shkafa-kupe/ | Р | чётко |
| FR-03 | Mastergrad: расчёт шкафа-купе на базе Raumplus | https://mastergrad.com/forums/t22409-raschet-razmerov-shkafa-kupe-na-baze-raum-plus-podskazhite-kak-sdelat/ | Р | чётко |
| FR-04 | Promebelclub: длина полок 16 мм, прогиб на полкодержателях | https://promebelclub.ru/forum/ (тема не уточнена: t=334 или t=6954) | Р | из поисковой выдачи |
| FR-05 | Festool Owners Group: накладная петля 110° мешает ящику за дверью | https://festoolownersgroup.com/threads/blum-full-overlay-hinges-interfere-with-drawer-behind-door.69397 | Р | из поисковой выдачи |
| ST-01 | «Тинькофф Журнал»: как сделать встроенный шкаф (глубина 600, зоны 1500–1700 / 1000–1100, ящики 150–250) | https://t-j.ru/kak-sdelat-nedorogoi-vstroennyi-shkaf/ | Р | чётко |
| ST-02 | Halvacard: как собрать шкаф-купе (диагонали ≤ 5 мм на 1 м, сборка лёжа) | https://media.halvacard.ru/construction-and-repair/kak-samostoyatelno-sobrat-shkaf-kupe | Р | чётко |
| ST-03 | Halvacard: как спланировать наполнение шкафа (верхняя одежда ≥ 1300) | https://media.halvacard.ru/construction-and-repair/kak-splanirovat-napolnenie-shkafa | Р | чётко |
| ST-04 | sdmeb.ru: проектируем шкаф-купе (система «съедает» 100, корпус 600 — перегородки 500) | http://www.sdmeb.ru/shkafy-kupe/proektiruem-shkaf-kupe.html | Р | чётко |
| ST-05 | shkaf-kupe-info.ru: ящики внутри шкафа (проставка 30–50) | https://shkaf-kupe-info.ru/shkafkupe-proekt/kak-sdelat-yaschiki-vnutri-shkafa.html | Р | чётко |
| ST-06 | Lacena: фальш-панели для шкафов-купе (80–120) | https://lacena.ru/all/falsh-paneli-dlya-shkafov-kupe-chto-eto-i-zachem/ | Р | чётко |
| ST-07 | Domov.by: установка шкафа-купе (перепад потолка 10–20, направляющая по уровню) | https://domov.by/remont/ustanovka-shkafa-kupe/ | Р | чётко |
| ST-08 | РБК Недвижимость: створка до 1200, механизм около 100 | https://realty.rbc.ru/news/5f73017f9a7947d2206f1f0a | Р | частично (выдача) |
| ST-09 | Liga.net: число дверей купе (2 — 900–1800, 3 — 1800–2500) | https://news.liga.net/all/pr/shkaf-kupe-3-soveta-dlya-vybora-idealnoy-modeli | Р | чётко |
| ST-10 | Техописание фабрики «Универсал»: запас места для сборки +30 по высоте, +50 по ширине | https://static12.insales.ru/files/1/1260/1098988/original/Тех.описание_Универсал.pdf | Р | из поисковой выдачи |
| ST-11 | Divan-krovat.by: торцевая штанга при корпусе 450–500 | https://divan-krovat.by/blog/shtanga-dlya-shkafa-kupe/ | Р | чётко |
| ST-12 | Teletype (mebel-spb): ширина секции и ящика в купе (ящик 500 в секции 560); форматы плит в магазинах (2750 × 1830) | https://teletype.in/@mebel-spb/pochemu-shirina-dverey-shkafa-imeet-znachenie ; https://www.prom.uz/ads/ldsp-2750-1830-16/ | Р | из поисковой выдачи / карточка магазина |
| ST-13 | Яндекс Маркет, подборка: крепить шкаф к стене от 2400 | https://market.yandex.ru/cc/Awud7B | Р | из поисковой выдачи |
| CA-01 | Sagulator (Woodbin): калькулятор прогиба полки, цель около 1,7 мм на 1 м | https://woodbin.com/calcs/sagulator/ | Р | чётко |
