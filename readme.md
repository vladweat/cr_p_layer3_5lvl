## Требования к Layer3

1. Подключен twitter
   - Подписка на layer3
   - Ретвит (https://twitter.com/layer3xyz/status/1562084669193068545)
2. Подключен discord
   - Вход в дискорд (https://discord.com/invite/bzktXw3gE)
3. Установлен аватар

## Требования 

1. Установлен Microsoft Visual C++ 14.0 и выше. [Сюда](https://learn.microsoft.com/en-us/answers/questions/136595/error-microsoft-visual-c-140-or-greater-is-require.html) если нет

## Требования по балансу


- eth: минималка
- polygon: ~3.9 matic
- avax: ~0.2
- optimism: ~1.8 usd
- arbitrum: ~0.8 usd

## Настройка

1. Создать виртуальное окружение 

```python
python -m vevn .
```

2. Активировать виртуальное окружение

- linux/macos
```python
source Scripts/activate
```

 - windows
```python
Scripts\activate.bat   
```

3. Установить библиотеки

```python
(venv) pip install -r requirements.txt
```

Можно было бы сразу начать писать в виртуалке и не устанавливать тонну библиотек потом, но мне как то было и есть похуй.

4. Подготовить wallets.txt
В файл wallets.txt построчно поместить данные в формате` ''{address} {private_key}''`.


## Функционал

1. Запуск модуля

```python
(venv) python app.py module_5
```

2. Запуск подмодуля

```python
(venv) python app.py module_13_a
```

Модули брать [здесь](https://docs.google.com/spreadsheets/d/1U0CubbqlY9wJOeBR4no558GtPqBOsmiDZub_YwMIWz8/edit#gid=0)

P.S. Это первая версия, ограниченное время и прочее, крч учится с этого скрипта точно не нужно
