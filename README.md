# Budget Tracker

A desktop application for budget tracking. Allows you to record spending by price and category. The amount of spending by category is conveniently displayed in a graph in the Graph menu.

## Demo
### Start Window
![login_window](https://github.com/ArtemKhov/Budget-Tracker/assets/107346597/ebc86cb5-2a0b-4296-a87c-b8cb176fe0ca)

### Home Window
![home_window](https://github.com/ArtemKhov/Budget-Tracker/assets/107346597/2677a1a3-a757-4ce1-a6f7-42c7f161ecff)

### Graph Window
![graph_window](https://github.com/ArtemKhov/Budget-Tracker/assets/107346597/29cbaf03-af16-43fa-88df-44fd180f12be)

## Technologies

**Tech Stack:**

- Python
- Pandas
- Plotly
- SQLite3
- tkinter
- ttkbootstrap

## Features

- Add records to the table (data is stored in a SQLite3 database)
- View all records
- Search for records by Title / Price / Category
- Delete one record or all records at once
- In the Graph menu you can see the amount of your expenses by category as a graph (implemented with Pandas and Plotly)
- Shows the error window when leaving blank fields, incorrect text length, etc.

## Run it locally (written for Windows)
1) Create a directory and clone the repo in it:
```sh
   git clone https://github.com/ArtemKhov/Budget-Tracker
   ```
2) Create your virtual environment:
```
python -m venv env
```
3) Activate your virtual environment:
```
env\Scripts\activate
```
4) Install the requirements.txt:
```
pip install -r requirements.txt
```

## License

Each file included in this repository is licensed under the [MIT Licence](https://github.com/ArtemKhov/Budget-Tracker/blob/master/LICENSE).
