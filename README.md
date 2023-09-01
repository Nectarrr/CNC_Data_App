# CNC_Data_App
Приложение для просмотра данных с СУБД MySQL, ранее полученных со станка с ЧПУ.

Оборудование, установленное в станке, представляет собой систему, основанную на наборе модулей Bosch Rexroth CNC MTX15VRS, которая состоит 
из ПЛК Bosch IndraControl XM42, сервоприводов IndraDrive, работающих в связке с сервомоторами IndraDrive MS2N, электродвигателей IndraDrive Mi, 
двумя типами модулей входов-выходов. Этот набор оборудования дополнен промышленным ПК и сенсорной панелью, выступающей в роли HMI (Human
Machine Interface) интерфейса для оператора станка
![image](https://github.com/Nectarrr/CNC_Data_App/assets/70803673/84994e41-eff5-40a7-b8b7-544c8a059607)

Ниже представлена архитектура ПАКа
![image](https://github.com/Nectarrr/CNC_Data_App/assets/70803673/a931c48d-4e55-4b10-888b-cfa0c8b8278c)

Для хранения данных была спроектирована физическая модель и разработана база данных MySQL
![image](https://github.com/Nectarrr/CNC_Data_App/assets/70803673/0ed45669-3d28-4261-91be-9dede8a3a672)



Из дополнительных функций: построение графика для выбранного параметра, сохранение выбранных данных в формате .xlsx

![image](https://user-images.githubusercontent.com/70803673/234520155-298541ce-3854-481a-93ff-7c8522987afe.png)
![image](https://user-images.githubusercontent.com/70803673/235749685-135dccb7-de8f-4469-8c99-1d99936ca611.png)

