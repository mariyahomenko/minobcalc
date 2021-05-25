# minobcalc
Отчетник

Программа является простым одноядерным калькулятором и нужна для оптимизации составления отчета результатов трудовой деятельности работника за отчетный период. Результаты отчетов по требованиям в текстовый документ не сохраняются. 
Первое окно:
![image](https://user-images.githubusercontent.com/73564203/119570944-6b327380-bdb9-11eb-91e1-3c4324e36679.png)
Первый виджет qlineedit принимает любые строковые значения, которые далее по требованиям не используются, а только записываются программой в переменную. Второй такой виджет транслирует результат ввода в дальнейшем в четвертом окне. 
Второе окно:
![image](https://user-images.githubusercontent.com/73564203/119570988-7b4a5300-bdb9-11eb-8d92-e458c9c5b1e3.png)
На все поля ввода установлены плейсхолдеры. Последнее поле доступно лишь для чтения и транслирует результат сложения значений из остальных полей. Что касается виджетов слагаемых, при обработке в функцию они поступают в виде строковых типов, а затем очищаются от лишних символов при помощи модуля «re», если таковые присутствуют. На следующий этап проходит строка, содержащая цифры от 0 до 9, точку и запятую, если присутствуют. Далее при помощи того же модуля в строке запятые заменяются на точки. Обработанные строки выводятся в интерфейс. Таким образом, если пользователь захочет ввести символы, не соответствующие функции, отображаться в поле они не будут (если точнее, то за доли секунд заменятся пустыми строками. Невозможен ввод не только букв или отрицательных чисел, но и чисел больше значения 0.2. Введенное значение преобразуется в формат десятичных при помощи модуля «decimal» и, если это значение больше, чем 0.2, заменяются на 0.2 как в интерфейсе, так и в последующих бэкендовых операциях. Если какая-либо строка осталась пустой, в операциях вместо нее используется значение 0. Если итоговая сумма чисел соответствует максимальному значению или меньше него, то сумма принимается в глобальную переменную и отображается пользователю с единственными изменениями — преобразование в строковый тип и перед тем округлением до двух знаков запятой по требованиям. В связи с этим требованием, если после хранения информации в двоичном виде и математических операций число в какой-либо промежуток времени занимало более двух знаков после запятой, пользователь может увидеть один или два лишних нуля, что, однако, математически неверным считаться не может.  
Третье окно:
![image](https://user-images.githubusercontent.com/73564203/119571089-9a48e500-bdb9-11eb-8ac8-ba905ae3ec7c.png)
Активация того или иного чекбокса делает остальные неактивными и проставляет соответствующее значение в итоговое поле, на которое доступно только для чтения. Чтобы поменять итоговое значение, необходимо снять установленную галочку, — что в свою очередь вызывает замену значения на 0 в поле вывода, — и кликнуть на новый чекбокс. 
Окно четыре:
![image](https://user-images.githubusercontent.com/73564203/119571120-a5037a00-bdb9-11eb-9add-5e8242c6c548.png)
При вызове четвертого окна первым делом происходит умножение глобальных переменных — коэффициента 1 на коэффициент 2. Далее значения первых двух текстовых полей преобразуются практически так же, как преобразуются значения во втором окне. В третье поле выводится результат операции: значение из первого поля делится на значение из второго поля и умножается на произведение коэффициентов, округляется до двух знаков после запятой. Это поле является редактируемым, чтобы результат можно было выделять и копировать. Если необходимо сделать поле доступным только для чтения и добавить кнопку быстрого копирования, обратитесь за редактурой. 
Касательно всех полей ввода — если что-либо пойдет не так, как задумано, программа не упадет, а соответствующие итоговые поля просто отобразят многоточия. Появление многоточий в полях означает, что нужно изменить значение в каких-то полях (например, если введено два десятичных разделителя в числе). 
Кнопка «Новый отчет» четвертого окна обнуляет переменные и возвращает пользователя на первое окно, а также снимает галочки с чекбоксов (данное действие вызывает функцию, проставляющую 0 в соответствующее итоговое поле).
Редирект по окнам осуществляются нажатиями на кнопки с галочками и является односторонним. Чтобы добавить возможность в любой момент переключаться между окнами, обратитесь за редактурой. На всех окнах виджеты после корректировок были собраны в выравнивающие сетки, поэтому они подстраиваются под размер окна, но всегда стремятся к центру как по вертикали, так и по горизонтали.
