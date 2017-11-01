# Нахождение минимальной цепочки преобразований одной строки в другую

Для решения поставленной задачи существует 2 распространненых алгоритма

  - Алгоритм Вагнера — Фишера
  - Алгоритм Хиршберга

Произвдем обзор существующих решений для выбора оптимального алгоритма.

## Алгоритм Вагнера — Фишера

Состоит из двух этапов:
  - Нахождение редакционного расстояния двух строк
  - Нахождение редакционного предписания

Для нахождения редакционного расстояния вводится вспомогательная функция *D(M, N)*, которая находит редакционное расстояние для подстрок *S1[0..M]* и *S2[0..N]*. Тогда полное редакционное расстояние будет равно расстоянию для подстрок полной длины: d(S1,S2) = DS1,S2(M,N).

Очевидно, что *D(0, 0) = 0*, *D(i, 0) = i*, *D(0, j) = j*.

В общем случае: *D(i,j) = min( D(i-1,j) + 1, D(i,j-1) + 1, D(i-1,j-1) + m(S1[i], S2[j])*,
где *m(S1[i], S2[j]) = 0*, если символы S1[i] и S2[j] совпадают, иначе *m(S1[i], S2[j]) = 1*.

  - *D(i-1,j-1) + m(S1[i], S2[j])* соответствует замене i-го символа первой строки на j-ый символ второй строки.
  - *D(i-1,j) + 1* соответствует удалению i-го символа первой строки и получению из S1[1..i-1] строки S2[1..j].
  - *D(i,j-1) + 1* соответствует получению из строки S1[1..i] строки S2[1..j-1] и добавлению S2[j].

Для восстановления редакционного предписания начиная из правого нижнего угла матрицы (M,N) мы идем в левый верхний, на каждом шаге выбирая минимальное из трёх значений:
  - если минимально *(D(i-1, j) + 1)*, добавляем удаление символа S1[i] и идём в (i-1, j);
  - если минимально *(D(i, j-1) + 1)*, добавляем вставку символа S1[i] и идём в (i, j-1);
  - если минимально *(D(i-1, j-1) + m)*, где m = 1, если *S1[i] != S2[j]*, иначе m = 0; после чего идём в *(i-1, j-1)* и добавляем замену если *m = 1*.
  
![image](https://2.downloader.disk.yandex.ru/preview/219903665cb91be063e3f47d4253b5e64ad614e8b07867f4969ffb564a71ea3e/inf/4yXdB_wd41WeNNaT6AHvbH5RE78skz8_cgVrKTM5FQ2Aqh-OAHoomHksfEY8OrTpXL-42ZGFXOQW9mRL3ueB7g%3D%3D?uid=0&filename=2017-11-01_20-53-30.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&tknv=v2&size=XXL&crop=0)

Таким образом, алгоритм работает за *O(|S1| * |S2|)* времени и ***O(|S1| * |S2|)*** памяти, так как для восстановления предписания необходимо хранить всю матрицу целиком.

