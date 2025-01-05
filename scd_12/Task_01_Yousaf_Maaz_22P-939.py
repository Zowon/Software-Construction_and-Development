import tkinter as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict

API_KEY = "9f24d4e758977bb0966fedcf76e0b1ee"

# Fetch current weather data for a city
def get_current_weather(city_name):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        return {
            "lat": lat,
            "lon": lon,
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "description": data["weather"][0]["description"].capitalize()
        }
    else:
        return None

# Fetch 5-day weather forecast
def get_weather_data(lat, lon):
    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
    url = f"{BASE_URL}lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        daily_temps = defaultdict(list)
        for entry in data["list"]:
            date = entry["dt_txt"].split(" ")[0]
            temp = entry["main"]["temp"]
            daily_temps[date].append(temp)
        averaged_temps = {date: sum(temps) / len(temps) for date, temps in daily_temps.items()}
        return list(averaged_temps.keys()), list(averaged_temps.values())
    else:
        return None, None

# Fetch 10 coldest cities in Pakistan
def get_coldest_cities():
    cities = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta", "Multan", "Faisalabad", "Rawalpindi", "Sialkot", "Gujranwala"]
    temperatures = {}
    for city in cities:
        weather = get_current_weather(city)
        if weather:
            temperatures[city] = weather["temp"]
    sorted_cities = sorted(temperatures.items(), key=lambda x: x[1])[:10]
    return sorted_cities

# Update plot style for dark theme
def update_plot_style(ax, title, xlabel, ylabel):
    ax.set_facecolor("#333333")  # Dark background
    ax.figure.set_facecolor("#222222")  # Overall figure background
    ax.spines["top"].set_color("#ffffff")
    ax.spines["right"].set_color("#ffffff")
    ax.spines["left"].set_color("#ffffff")
    ax.spines["bottom"].set_color("#ffffff")
    ax.tick_params(colors="#ffffff")
    ax.xaxis.label.set_color("#ffffff")
    ax.yaxis.label.set_color("#ffffff")
    ax.title.set_color("#ffffff")
    ax.grid(color="#444444", linestyle="--", linewidth=0.5)
    ax.set_title(title, fontsize=14)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)

# Fetch and display weather details for a city
def fetch_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return

    weather_details = get_current_weather(city)
    if not weather_details:
        messagebox.showerror("Error", f"Weather data for '{city}' not found.")
        return

    lat, lon = weather_details["lat"], weather_details["lon"]
    dates, temperatures = get_weather_data(lat, lon)
    if not dates or not temperatures:
        messagebox.showerror("Error", f"5-day forecast for '{city}' not found.")
        return

    current_weather_text.set(
        f"Current Weather in {city.capitalize()}:\n"
        f"Temperature: {weather_details['temp']}°C\n"
        f"Humidity: {weather_details['humidity']}%\n"
        f"Pressure: {weather_details['pressure']} hPa\n"
        f"Description: {weather_details['description']}"
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dates, temperatures, marker='o', linestyle='-', color='cyan')
    update_plot_style(ax, f"5-Day Average Temperature Trend for {city.capitalize()}", "Date", "Average Temperature (°C)")
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Display the 10 coldest cities in Pakistan
def fetch_coldest_cities():
    coldest_cities = get_coldest_cities()
    if not coldest_cities:
        messagebox.showerror("Error", "Failed to fetch data for the coldest cities.")
        return

    cities, temps = zip(*coldest_cities)
    coldest_cities_text.set(
        "10 Coldest Cities in Pakistan:\n" +
        "\n".join([f"{city}: {temp}°C" for city, temp in coldest_cities])
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(cities, temps, color="lightblue")
    update_plot_style(ax, "10 Coldest Cities in Pakistan", "City", "Temperature (°C)")
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# GUI Setup
root = tk.Tk()
root.title("Weather Application")
root.geometry("800x600")
root.configure(bg="#333333")  # Dark background

input_frame = ttk.Frame(root, padding=10, style="TFrame")
input_frame.pack(side=tk.TOP, fill=tk.X, padx=20)

ttk.Label(input_frame, text="Enter City Name:", font=("Arial", 12), foreground="#ffffff", background="#333333").pack(side=tk.LEFT, padx=10)
city_entry = ttk.Entry(input_frame, font=("Arial", 12), width=30)
city_entry.pack(side=tk.LEFT, padx=10)

fetch_button = ttk.Button(input_frame, text="Fetch Data", command=fetch_weather, style="Dark.TButton")
fetch_button.pack(side=tk.LEFT, padx=10)

coldest_button = ttk.Button(input_frame, text="Coldest Cities", command=fetch_coldest_cities, style="Dark.TButton")
coldest_button.pack(side=tk.LEFT, padx=10)

current_weather_text = tk.StringVar()
weather_label = ttk.Label(root, textvariable=current_weather_text, font=("Arial", 14), wraplength=700, foreground="#ffffff", background="#333333", anchor="w")
weather_label.pack(pady=10)

coldest_cities_text = tk.StringVar()
coldest_label = ttk.Label(root, textvariable=coldest_cities_text, font=("Arial", 14), wraplength=700, foreground="#ffffff", background="#333333", anchor="w")
coldest_label.pack(pady=10)

chart_frame = ttk.Frame(root, style="TFrame")
chart_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

style = ttk.Style()
style.configure("TButton", padding=10, font=("Arial", 12, "bold"))
style.configure("Dark.TButton", background="#444444", foreground="#ffffff", font=("Arial", 12, "bold"))
style.map("Dark.TButton", background=[("active", "#555555")])
style.configure("TFrame", background="#333333")

root.mainloop()
