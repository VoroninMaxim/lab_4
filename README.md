# Пример DVC: Управление версиями 

В этом примере демонстрируется использование DVC для реализации базового рабочего процесса обучения модели. В частности, он используется для достижения следующих целей:

- Передача данных на удаленные серверы для обучения модели
- Сохранение сериализованных моделей после обучения


## 1. Загрузка, извлечение и преобразование обучающих данных 
```bash
mkdir datasets
python preprocessing.py
python preprocessing_one_hot.py
python preproccessing_null_values.py
```
## 2. Инициализация, аутентификация и отправка данных в DVC:

Когда наши данные готовы к распространению, мы инициализируем DVC:
```bash
dvc init
```
DVC может использовать несколько бэкендов для хранения данных, таких как корзины S3, корзины GCS, NFS, Google Drive. Для простоты мы будем использовать последнее.

Создайте папку на диске и переместите в нее. URL-адрес в вашем браузере должен быть примерно таким:
```bash
https://drive.google.com/drive/folders/1CUWjhnRnxFJQe1eN8FCLoyHXE4Fvd5rD?hl=ru
```
Нас интересует идентификатор папки, который является последней частью URL-адреса. Мы используем его для создания пульта дистанционного управления DVC Google Drive:
```bash
dvc remote add -d storage gdrive://1CUWjhnRnxFJQe1eN8FCLoyHXE4Fvd5rD
git add .dvc/config
git commit -m "updated DVC config"
```
Теперь мы пробуем отслеживать наши в git-репозитории с помощью DVC, а затем отправляем их на удаленный репозиторий для подготовки к обучению:
```bash
dvc add datasets
git add datasets/titanic_train.dvc datasets/.gitignore
git commit -m "added DVC metadata for titanic_train"
dvc push 
git push 
```