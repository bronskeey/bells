# bells
Software for managing school bells.

v 0.01
uploaded 12.08.2021
changelog: 

added base functions: 

- two frames: 'D E F A U L T' and 'P R A Z D N I K': 

1) 'D E F A U L T' has 4 options:
	- 'Select MP3', 'Bind file', 'Delete task', 'Clear tasks' 
2) 'P R A Z D N I K' currently has 3 option:
	- 'Select playlist', 
	- 'LET THE FUN BEGIN' - NOT YET IMPLEMENTED 12.08.2021
	- 'Clear playlist'    - NOT YET IMPLEMENTED 12.08.2021

- status labels in the footer can be configured:

1) left one displaying selected task next and last run. 

2) right one displaying selected file or folder. - NOT YET IMPLEMENTED


TODO 12.08.2021: 
- let music be interrupted by bells ringing, turn music off, shuffle(?)
- full english description

=======================================================================

v 0.01: добавлены базовые функции:

- в программе есть два раздела 'D E F A U L T' и 'P R A Z D N I K':

1) 'D E F A U L T' имеет 4 кнопки:
	- 'Select MP3', 'Bind file', 'Delete task', 'Clear tasks'

   В этом разделе можно выбрать mp3 файл для звонка, прикрепить его к распианию, удалить выбранный звонок или очистить все. После выбора файла, его имя файла появляется в нижнем правом лейбле и появляется возможность прикрепить его к стандартному расписанию - начало в 08:30, уроки по 45 минут, перемены по 15. 
   Функция удаления звонка удаляет выбранный мышкой, функция очистки удаляет все звонки из сегодняшнего расписания.

2) 'P R A Z D N I K' на данный момент в разработке и пока имеет только 1 рабочую кнопку:
	- 'Select playlist' выбирает папку с музыкой
    - 'LET THE FUN BEGIN' будет включать музыку из папки  - NOT YET IMPLEMENTED 12.08.2021

	- 'Clear playlist'    будет очищать очередь с музыкой   - NOT YET IMPLEMENTED 12.08.2021

	Этот раздел предназначен для режима праздничного дня, когда на переменах играет музыка из папки. Необходимо реализовать прерывание музыки звонками и последующее включение музыки после звонка с урока.

 - статусная строка отображает информацию:

 1)левая часть показывает предыдущий и следующий запуск выбранного звонка из расписания

 2)правая часть показывает выбранные файл и папку         - NOT YET IMPLEMENTED 12.08.2021

TODO 12.08.2021: 
- добавить создание нового расписания в последнюю секунду дня.
- выяснить, появятся ли новые звонки в конце дня после 'Clear tasks'
- все NOT YET IMPLEMENTED

