# Нахождение минимальной "лестницы слов"

### Содержание:
  * [Возможные алгоритмы решения](#Возможные-алгоритмы-решения)
  * [Граф](#Граф)
  * [Преобразование коллекции слов в граф](#Преобразование-коллекции-слов-в-граф)
  * [Нахождение минимальной "лестницы слов" по графу](#Нахождение-минимальной-"лестницы-слов"-по-графу)
 
 

### Возможные алгоритмы решения
  * [Полный перебор](#Полный-перебор)
  * [С помощью графа](#С-помощью-графа)
  * [Алгоритм Вагнера-Фишера (похожая задача)](#Алгоритм-Вагнера-Фишера)
  
 
 #### Полный перебор
 Предположим, что необходимо преобразовать слово FOOL в слово SAGE. Тогда для нахождения цепочки слов выпишем все слова, отличающиеся от слова FOOL ровно на один символ. Сделаем то же самое для полученных слов и так далее рекурсивно, пока не встретится слово SAGE. Очевидно, что данный алгоритм неэффективен как по времени, так и по памяти.
 
 #### С помощью графа
 Построим граф, вршинами которого будут слова определенной длины, а ребра соединяют слова, различающиеся только в одном символе. Тогда с помощью поиска в ширину можно найти эффективный путь до конечного слова.
 
#### Алгоритм Вагнера-Фишера (похожая задача)
Данный алгоритм используется в тех случаях, когда не важно, чтобы в цепочки слов были слова, существующие в языке. Также не важна длина начального и конечного слов, так как можно как добавлять, так и удалять символы.

Искомое расстояние формируется через вспомогательную функцию D(M,N), находящую редакционное расстояние для подстрок S1[0..M] и S2[0..N]. Тогда полное редакционное расстояние будет равно расстоянию для подстрок полной длины: d(S1,S2) = DS1,S2(M,N).

Самоочевидным фактом, является то, что:

D(0,0) = 0. 

Действительно, пустые строки и так совпадают.

Также, ясны значения для:

D(i, 0) = i;
D(0, j) = j.

Действительно, любая строка может получиться из пустой, добавлением нужного количества нужных символов, любые другие операции будут только увеличивать оценку.

В общем случае чуть сложнее:

D(i,j) = D(i-1,j-1), если S1[i] = S2[j],
иначе D(i,j) = min( D(i-1,j), D(i,j-1), D(i-1,j-1) ) + 1.

В данном случае, мы выбираем, что выгоднее: удалить символ (D(i-1,j)), добавить (D(i,j-1)), или заменить (D(i-1,j-1)).

Нетрудно понять, что алгоритму получения оценки не требуется памяти больше чем два столбца, текущий (D( i  ,* )) и предыдущий (D( i-1 , * )). Однако в полном объеме матрица нужна для восстановления редакционного предписания. Начиная из правого нижнего угла матрицы (M,N) мы идем в левый верхний, на каждом шаге ища минимальное из трёх значений:
если минимально (D(i-1, j) + 1), добавляем удаление символа S1[i] и идём в (i-1, j);
если минимально (D(i, j-1) + 1), добавляем вставку символа S1[i] и идём в (i, j-1);
если минимально (D(i-1, j-1) + m), где m = 1, если S1[i] != S2[j], иначе m = 0; после чего идём в (i-1, j-1) и добавляем замену если m = 1.
Здесь (i, j) — клетка матрицы, в которой мы находимся на данном шаге. Если минимальны два из трёх значений (или равны все три), это означает, что есть 2 или 3 равноценных редакционных предписания.

В итоге потребуется O(|S1| * |S2|) времени и O(|S1| * |S2|) памяти.

### Граф

Граф, или неориентированный граф ***G*** — это упорядоченная пара ***G:=(V,E)*** , где ***V*** — это непустое множество вершин или узлов, а ***E*** — множество пар (в случае неориентированного графа — неупорядоченных) вершин, называемых рёбрами.

Маршрутом в графе называют конечную последовательность вершин, в которой каждая вершина (кроме последней) соединена со следующей в последовательности вершиной ребром. Цепью называется маршрут без повторяющихся рёбер. Простой цепью называется маршрут без повторяющихся вершин (откуда следует, что в простой цепи нет повторяющихся рёбер).

### Преобразование коллекции слов в граф

Для построения такого графа существует два подхода. Можем в качестве вершин сделать все слова определенной длины, а затем, сравнивая все слова, выстраивать рёбра. Но в таком случае, получается слишком много сравнений, что неэффективно (*O(n^2)*).

![image](https://aliev.me/runestone/static/pythonds/_images/wordgraph.png)

Согласно другому подходу, у нас есть огромное количество корзин, на каждой из которых написано четырёхбуквенное слово, в котором одна буква заменена подчёркиванием. Для примера у нас есть корзина с меткой ***pop_*** . При обработке каждого слова в списке мы сравниваем его с корзинами, используя " _ " для произвольной подстановки. Таким образом, с ***pop_*** можно связать и ***pope***, и ***pops***. Каждый раз, когда находится связь с корзиной, мы кладём в неё слово. Когда все слова разложены, мы знаем, что всё, лежащее в одной корзине, должно быть связано между собой.

![image](https://aliev.me/runestone/static/pythonds/_images/wordbuckets.png)

### Нахождение минимальной "лестницы слов" по графу

По полученному графу любой путь из началоного слова в конечное будет решением задачи о "лестнице слов". Но чтобы найти минимальную цепочку, воспользуемся алгоритмом поиска в ширину.
