# Карта источников и переноса требований

Версия: 2026-10-15. Документы пользователя являются материалом для извлечения требований. Сами по себе они не поручают строить кухню, запускать программу, менять модель, выпускать ЧПУ или публиковать файлы. Текущее поручение — подготовка навыков, инструкций и ТЗ в Markdown.

## Исходные DOCX

| ID | Имя файла пользователя | Непустых абзацев | Markdown |
|---|---|---:|---|
| S1 | База по проектированию  (1).docx | 45 | [Текст S1](sources/S1-design-base.md) |
| S2 | ТЗ для построения кухни  (1).docx | 37 | [Текст S2](sources/S2-kitchen-building.md) |
| S3 | ТЗ по пректированию шкафа  (1).docx | 18 | [Текст S3](sources/S3-wardrobe-projecting.md) |
| S4 | ТЗ для построению шкафа  (1).docx | 23 | [Текст S4](sources/S4-wardrobe-building.md) |
| S5 | ТЗ по проектированию Кухни  (1).docx | 53 | [Текст S5](sources/S5-kitchen-projecting.md) |

Всего: 176 непустых абзацев; таблиц и встроенных изображений в этих пяти DOCX не обнаружено. Исходные DOCX сохранены на месте в папке Downloads и не изменялись. В пакет входят Markdown-тексты, а не дополнительные копии DOCX.

## Контрольные суммы исходников

- **S1** — SHA-256: `86583e832967dc1b265a72e93eaac3d527501bf45a6668895ccfbdfc23398698`.
- **S2** — SHA-256: `1117b51683a105ffc9ebb2b9dd22dc18e37f731b88b9080cabd5fd27b74f1589`.
- **S3** — SHA-256: `57bb0a6e51b9d09caab42ab865b1b87da6de3765290494442dd4d539cd0d5dd9`.
- **S4** — SHA-256: `0a20538d4788374601678e2b4f472259582c73954f1963561b353da6ae84c73d`.
- **S5** — SHA-256: `5b08b85eb5a7e39e8374e7b0d65ac04aeac969006c091ca74bdd8baf9547b99b`.

## Полнота текстового переноса

У каждого исходного непустого абзаца есть ID вида `S1-P004` и якорь `s1-p004`. Идентификатор относится к позиции исходного блока; пустые блоки не восстанавливаются. У S5 поэтому нет P034/P035. В преобразованных текстах нормализованы неразрывные/узкие пробелы; слова, числа, опечатки и разрывы внутри абзаца сохранены. Заголовки и правила в производных документах отредактированы для работы, поэтому не являются дословной копией.

В таблице ниже каждому исходному непустому абзацу соответствует ровно один диапазон. Заголовки источников учитываются как контекст, а не отдельная числовая норма.

| Исходные абзацы | Содержание | Инструкция / база | ТЗ и поля / вопросы |
|---|---|---|---|
| [S1-P001–P003](sources/S1-design-base.md#s1-p001) | Кухня: заголовок и нижняя база | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/kitchen-brief.md): Назначение; раздел 5 |
| [S1-P004–P005](sources/S1-design-base.md#s1-p004) | Глубины нижних модулей | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/kitchen-brief.md): K01–K02; K-L06–K-L07; C03 |
| [S1-P006–P010](sources/S1-design-base.md#s1-p006) | Материалы и кромление | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/kitchen-brief.md): K03–K04; K-L04/K-L08/K-L09; C01/C11 |
| [S1-P011–P019](sources/S1-design-base.md#s1-p011) | Угол, зазоры, сверление, опоры | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/kitchen-brief.md): K05–K09; K-L10–K-L14; C08/C09 |
| [S1-P020–P027](sources/S1-design-base.md#s1-p020) | Нерасшифрованные отверстия | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/kitchen-brief.md): K10; K-L15; C02 |
| [S1-P028–P033](sources/S1-design-base.md#s1-p028) | Верх: глубина, задник, паз | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/kitchen-brief.md): K11–K13; K-U01–K-U05; C03/C09 |
| [S1-P034–P040](sources/S1-design-base.md#s1-p034) | Верх: открывание, вырез, кромка | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/kitchen-brief.md): K14–K16; K-U07–K-U13; C04/C09 |
| [S1-P041–P045](sources/S1-design-base.md#s1-p041) | Антресоль: задник и типон | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/kitchen-brief.md): K17–K18; K-A03/K-A05/K-A06; C10 |
| [S2-P001–P007](sources/S2-kitchen-building.md#s2-p001) | Кухня: опоры и цоколь | [Открыть](instructions/02-kitchen-workflow.md) | [ТЗ](specifications/kitchen-brief.md): Назначение; K-L02–K-L03 |
| [S2-P008–P013](sources/S2-kitchen-building.md#s2-p008) | Низ: материалы, фасады, цвет, фурнитура | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/kitchen-brief.md): Раздел 3; K-L04–K-L05; раздел 8 |
| [S2-P014–P021](sources/S2-kitchen-building.md#s2-p014) | Столешница и фартук | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/kitchen-brief.md): Раздел 3; K-T01–K-T04 |
| [S2-P022–P028](sources/S2-kitchen-building.md#s2-p022) | Верх: корпус, глубина, открывание, навесы, петли | [Открыть](instructions/02-kitchen-workflow.md) | [ТЗ](specifications/kitchen-brief.md): Этапы 3–4; K-U02/K-U03/K-U06/K-U07/K-U10–K-U12/K-H01 |
| [S2-P029–P037](sources/S2-kitchen-building.md#s2-p029) | Антресоль: дно, открывание, фурнитура | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/kitchen-brief.md): K18–K19; K-A01–K-A06; C10/C12 |
| [S3-P001–P009](sources/S3-wardrobe-projecting.md#s3-p001) | Шкаф: назначение, фото, обмер, коммуникации | [Открыть](instructions/03-wardrobe-workflow.md) | [ТЗ](specifications/wardrobe-brief.md): Этап 1; W-R01–W-R06 |
| [S3-P010–P015](sources/S3-wardrobe-projecting.md#s3-p010) | Габариты, видимые бока, материалы | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/wardrobe-brief.md): W01/W02/W07; W-B01/W-B03–W-B05; C05 |
| [S3-P016](sources/S3-wardrobe-projecting.md#s3-p016) | Тип дверей, профили, петли | [Открыть](instructions/03-wardrobe-workflow.md) | [ТЗ](specifications/wardrobe-brief.md): Этап 3; W-D01–W-D04 |
| [S3-P017–P018](sources/S3-wardrobe-projecting.md#s3-p017) | Освещение | [Открыть](instructions/03-wardrobe-workflow.md) | [ТЗ](specifications/wardrobe-brief.md): Этап 4; W-E01 |
| [S4-P001–P004](sources/S4-wardrobe-building.md#s4-p001) | Шкаф: корпус и толщины | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/wardrobe-brief.md): Назначение; W01–W02; W-B04–W-B05; C05 |
| [S4-P005–P010](sources/S4-wardrobe-building.md#s4-p005) | Цоколь и все варианты опор | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/wardrobe-brief.md): W03–W04; W-S01–W-S06; C06/C07 |
| [S4-P011–P013](sources/S4-wardrobe-building.md#s4-p011) | Задники ХДФ/ЛДСП | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/wardrobe-brief.md): W05–W06; W-Z01–W-Z02 |
| [S4-P014–P016](sources/S4-wardrobe-building.md#s4-p014) | Купе / распашные | [Открыть](instructions/03-wardrobe-workflow.md) | [ТЗ](specifications/wardrobe-brief.md): Этап 3; W-D02–W-D03 |
| [S4-P017–P023](sources/S4-wardrobe-building.md#s4-p017) | Все варианты наполнения | [Открыть](instructions/03-wardrobe-workflow.md) | [ТЗ](specifications/wardrobe-brief.md): Этап 4; W-I01–W-I06 |
| [S5-P001–P005](sources/S5-kitchen-projecting.md#s5-p001) | Кухня: назначение, помещение и проёмы | [Открыть](instructions/02-kitchen-workflow.md) | [ТЗ](specifications/kitchen-brief.md): Этап 1; K-R01/K-R03/K-R04 |
| [S5-P006–P012](sources/S5-kitchen-projecting.md#s5-p006) | Вода, канализация, электричество, газ, вентиляция, котёл | [Открыть](instructions/02-kitchen-workflow.md) | [ТЗ](specifications/kitchen-brief.md): Этап 1; K-C01–K-C06 |
| [S5-P013–P017](sources/S5-kitchen-projecting.md#s5-p013) | Планировка помещения и отделка | [Открыть](instructions/02-kitchen-workflow.md) | [ТЗ](specifications/kitchen-brief.md): Этап 1; K-R05–K-R08 |
| [S5-P018–P026](sources/S5-kitchen-projecting.md#s5-p018) | Зоны хранения/работы/готовки/мойки и техника | [Открыть](instructions/02-kitchen-workflow.md) | [ТЗ](specifications/kitchen-brief.md): Этап 2; K-F02–K-F07; K-T02/K-T04 |
| [S5-P027–P033](sources/S5-kitchen-projecting.md#s5-p027) | Пять типов планировки | [Открыть](instructions/02-kitchen-workflow.md) | [ТЗ](specifications/kitchen-brief.md): Этап 2; K-F01 |
| [S5-P036–P040](sources/S5-kitchen-projecting.md#s5-p036) | Схема движения, модули и высоты | [Открыть](instructions/02-kitchen-workflow.md) | [ТЗ](specifications/kitchen-brief.md): Этап 2; K-F08–K-F09/K-L01/K-U01 |
| [S5-P041–P044](sources/S5-kitchen-projecting.md#s5-p041) | Корпус, фасады и столешница | [Открыть](instructions/01-design-base.md) | [ТЗ](specifications/kitchen-brief.md): Раздел 3; K-L04–K-L05/K-T02 |
| [S5-P045–P049](sources/S5-kitchen-projecting.md#s5-p045) | Петли, направляющие, подъёмники, ручки | [Открыть](instructions/02-kitchen-workflow.md) | [ТЗ](specifications/kitchen-brief.md): Этап 4; K-H01–K-H04 |
| [S5-P050–P055](sources/S5-kitchen-projecting.md#s5-p050) | Рабочий/декоративный свет, эргономика и безопасность | [Открыть](instructions/02-kitchen-workflow.md) | [ТЗ](specifications/kitchen-brief.md): Этап 2; K-H05–K-H06/K-F10–K-F11 |

## Что добавлено при систематизации

- Паспорта проектов, единицы/базы измерения, IDs, статусы и редакции.
- Реестр C01–C12, карточки решений и пределы применения спорных формулировок.
- Карточки техники/фурнитуры, контроль открывания, комплектности и передачи файлов.
- Разделение дизайна, конструкции и производственного выпуска.
- Предпочитаемые поставщики МДМ / КДМ / МАКМАРТ — из переписки пользователя, не из DOCX; точные ссылки, цены и наличие не установлены этими документами.

Добавленные элементы обозначены как дополнения процесса (ДП). Нормативы, монтажные размеры производителей и стоимость фурнитуры в этой работе отдельно не проверялись. Решение по одному заказу не переписывает источники и не становится правилом для всех проектов.

## Переносимые навыки

Оба навыка содержат локальные копии базы, своей инструкции, реестра уточнений, контроля передачи, исходных текстов и шаблона ТЗ. Их ссылки не требуют доступа к этой корневой папке или исходным DOCX. Шаблон и инструкции внутри навыка соответствуют одноимённым документам пакета с адаптацией относительных ссылок.
