import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import ttk
from main_backend import WeatherApp


class WeatherAppUI:
    # Modern color scheme with gradient-like effect
    MAIN_BG = '#1e3c72'         # Deep blue
    CONTAINER_BG = '#2a5298'    # Medium blue
    SEARCH_BG = '#FFFFFF'       # Pure white for search
    TEXT_PRIMARY = '#FFFFFF'    # White text
    TEXT_SECONDARY = '#BDC3C7'  # Light gray text
    TEXT_DARK = '#2C3E50'       # Dark text for light backgrounds
    ACCENT_COLOR = '#3498DB'    # Bright blue accent
    BOX_BG = '#34495E'          # Dark gray-blue for boxes
    ERROR_COLOR = '#E74C3C'     # Red for errors
    SUCCESS_COLOR = '#27AE60'   # Green for success

    def __init__(self, backend: WeatherApp, root: tk.Tk):
        load_dotenv()
        self.__backend = backend
        self.__root = root

        # Window dimensions
        self.min_width = 400
        self.min_height = 650
        self.current_width = 500
        self.current_height = 700

        self.configure_window()
        self.create_widgets()
        self.__root.mainloop()

    def configure_window(self):
        self.__root.title('Weather App')
        self.__root.configure(bg=self.MAIN_BG)

        # Center window on screen
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        x = (screen_width - self.current_width) // 2
        y = (screen_height - self.current_height) // 2

        self.__root.geometry(
            f'{self.current_width}x{self.current_height}+{x}+{y}')
        self.__root.minsize(self.min_width, self.min_height)

        # Configure responsive grid
        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_rowconfigure(0, weight=1)

        # Bind resize event for responsive layout
        self.__root.bind('<Configure>', self.on_window_resize)
        self._resize_job = None

    def on_window_resize(self, event):
        # Only handle root window resize events
        if event.widget != self.__root:
            return

        # Cancel previous resize job
        if self._resize_job:
            self.__root.after_cancel(self._resize_job)

        # Schedule new resize job with delay
        self._resize_job = self.__root.after(
            100, lambda: self.delayed_resize(event.width, event.height))

    def delayed_resize(self, width, height):
        if width != self.current_width or height != self.current_height:
            self.current_width = width
            self.current_height = height
            self.update_responsive_layout()

    def update_responsive_layout(self):
        # Adjust font sizes based on window size
        base_size = min(self.current_width, self.current_height)

        # Scale factors for different screen sizes
        if base_size < 500:
            temp_size = 36
            city_size = 20
            condition_size = 14
            detail_size = 10
        elif base_size < 700:
            temp_size = 48
            city_size = 28
            condition_size = 18
            detail_size = 12
        else:
            temp_size = 64
            city_size = 36
            condition_size = 22
            detail_size = 14

        # Update fonts if widgets exist
        if hasattr(self, 'temp_label'):
            self.temp_label.configure(font=('Segoe UI', temp_size, 'bold'))
        if hasattr(self, 'city_label'):
            self.city_label.configure(font=('Segoe UI', city_size, 'bold'))
        if hasattr(self, 'condition_label'):
            self.condition_label.configure(
                font=('Segoe UI Light', condition_size))

    def create_widgets(self):
        # Create main scrollable frame
        main_frame = tk.Frame(self.__root, bg=self.MAIN_BG)
        main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Create scrollable canvas
        canvas = tk.Canvas(main_frame, bg=self.MAIN_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(
            main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.MAIN_BG)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Store references
        self.canvas = canvas
        self.scrollable_frame = scrollable_frame

        # Create the UI elements
        self.create_search_section()
        self.create_weather_display()
        self.create_details_section()

        # Bind mousewheel to canvas
        self.bind_mousewheel()

    def bind_mousewheel(self):
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        self.__root.bind("<MouseWheel>", _on_mousewheel)

    def create_search_section(self):
        # Search container
        search_frame = tk.Frame(
            self.scrollable_frame,
            bg=self.CONTAINER_BG,
            relief='ridge',
            bd=2
        )
        search_frame.pack(fill='x', padx=20, pady=(20, 10))

        # Search title
        search_title = tk.Label(
            search_frame,
            text="🌍 Weather Search",
            font=('Segoe UI', 14, 'bold'),
            bg=self.CONTAINER_BG,
            fg=self.TEXT_PRIMARY
        )
        search_title.pack(pady=(15, 10))

        # Search entry frame
        entry_frame = tk.Frame(search_frame, bg=self.CONTAINER_BG)
        entry_frame.pack(fill='x', padx=15, pady=(0, 15))

        self.search_entry = tk.Entry(
            entry_frame,
            font=('Segoe UI', 14),
            bg=self.SEARCH_BG,
            fg=self.TEXT_DARK,
            insertbackground=self.TEXT_DARK,
            relief='solid',
            bd=1,
            width=25
        )
        self.search_entry.pack(side='left', fill='x',
                               expand=True, padx=(0, 10), ipady=8)
        self.search_entry.bind('<Return>', lambda e: self.search_city())
        self.search_entry.bind('<FocusIn>', self.on_entry_focus_in)
        self.search_entry.bind('<FocusOut>', self.on_entry_focus_out)

        # Search button
        search_button = tk.Button(
            entry_frame,
            text='Search',
            command=self.search_city,
            font=('Segoe UI', 12, 'bold'),
            bg=self.ACCENT_COLOR,
            fg=self.TEXT_PRIMARY,
            relief='raised',
            bd=2,
            padx=20,
            pady=8,
            cursor='hand2',
            activebackground=self.SUCCESS_COLOR
        )
        search_button.pack(side='right')

        # Set placeholder text
        self.set_placeholder()

    def set_placeholder(self):
        if not self.search_entry.get():
            self.search_entry.insert(0, "Enter city name...")
            self.search_entry.configure(fg='#999999')

    def on_entry_focus_in(self, event):
        if self.search_entry.get() == "Enter city name...":
            self.search_entry.delete(0, tk.END)
            self.search_entry.configure(fg=self.TEXT_DARK)

    def on_entry_focus_out(self, event):
        if not self.search_entry.get():
            self.set_placeholder()

    def create_weather_display(self):
        # Main weather display container
        weather_frame = tk.Frame(
            self.scrollable_frame,
            bg=self.CONTAINER_BG,
            relief='ridge',
            bd=2
        )
        weather_frame.pack(fill='x', padx=20, pady=10)

        # City name
        self.city_label = tk.Label(
            weather_frame,
            text='Welcome to Weather App',
            font=('Segoe UI', 28, 'bold'),
            fg=self.TEXT_PRIMARY,
            bg=self.CONTAINER_BG
        )
        self.city_label.pack(pady=(20, 5))

        # Temperature display
        self.temp_label = tk.Label(
            weather_frame,
            text='--°',
            font=('Segoe UI', 48, 'bold'),
            fg=self.ACCENT_COLOR,
            bg=self.CONTAINER_BG
        )
        self.temp_label.pack(pady=10)

        # Weather condition
        self.condition_label = tk.Label(
            weather_frame,
            text='Search for a city to see weather information',
            font=('Segoe UI Light', 16),
            fg=self.TEXT_SECONDARY,
            bg=self.CONTAINER_BG
        )
        self.condition_label.pack(pady=(5, 20))

    def create_details_section(self):
        # Details container
        details_main = tk.Frame(
            self.scrollable_frame,
            bg=self.CONTAINER_BG,
            relief='ridge',
            bd=2
        )
        details_main.pack(fill='x', padx=20, pady=(10, 20))

        # Title for details section
        details_title = tk.Label(
            details_main,
            text="📊 Weather Details",
            font=('Segoe UI', 14, 'bold'),
            fg=self.TEXT_PRIMARY,
            bg=self.CONTAINER_BG
        )
        details_title.pack(pady=(15, 10))

        # Details grid container
        details_frame = tk.Frame(details_main, bg=self.CONTAINER_BG)
        details_frame.pack(fill='x', padx=15, pady=(0, 15))

        # Create detail boxes in a 2x2 grid
        details = [
            ("Feels Like", "feels_like", "🌡️", "--°"),
            ("Wind Speed", "wind", "💨", "-- km/h"),
            ("Humidity", "humidity", "💧", "--%"),
            ("Pressure", "pressure", "📊", "-- mb")
        ]

        for i, (title, key, icon, default) in enumerate(details):
            row = i // 2
            col = i % 2
            self.create_detail_box(details_frame, title,
                                   key, icon, default, row, col)

        # Configure grid weights for responsiveness
        details_frame.grid_columnconfigure(0, weight=1)
        details_frame.grid_columnconfigure(1, weight=1)

    def create_detail_box(self, parent, title, key, icon, default_value, row, col):
        # Create detail box
        box = tk.Frame(
            parent,
            bg=self.BOX_BG,
            relief='raised',
            bd=2
        )
        box.grid(row=row, column=col, padx=8, pady=8,
                 sticky='nsew', ipadx=15, ipady=10)

        # Icon
        icon_label = tk.Label(
            box,
            text=icon,
            font=('Segoe UI', 20),
            bg=self.BOX_BG,
            fg=self.TEXT_PRIMARY
        )
        icon_label.pack(pady=(8, 4))

        # Value
        value_label = tk.Label(
            box,
            text=default_value,
            font=('Segoe UI', 14, 'bold'),
            bg=self.BOX_BG,
            fg=self.TEXT_PRIMARY
        )
        value_label.pack(pady=2)

        # Title
        title_label = tk.Label(
            box,
            text=title,
            font=('Segoe UI', 10),
            bg=self.BOX_BG,
            fg=self.TEXT_SECONDARY
        )
        title_label.pack(pady=(2, 8))

        # Store reference to value label
        setattr(self, f'{key}_label', value_label)

    def search_city(self):
        city = self.search_entry.get().strip()
        if not city or city == "Enter city name...":
            self.show_error("Please enter a city name")
            return

        try:
            # Show loading state
            self.city_label.config(text="Searching...", fg=self.TEXT_PRIMARY)
            self.condition_label.config(text="Please wait...")
            self.__root.update()

            location_data, weather_data = self.__backend.current_weather(city)

            if location_data and weather_data:
                # Update main display
                self.city_label.config(
                    text=f"{location_data['name']}, {location_data['country']}",
                    fg=self.TEXT_PRIMARY
                )
                self.temp_label.config(text=f"{weather_data['temp_c']}°")
                self.condition_label.config(
                    text=f"{weather_data['condition']}")

                # Update detail boxes
                self.feels_like_label.config(
                    text=f"{weather_data['feelslike_c']}°")
                self.wind_label.config(
                    text=f"{weather_data['wind_speed(kph)']} km/h")
                self.humidity_label.config(text=f"{weather_data['humidity']}%")

                # Add pressure if available
                if 'pressure_mb' in weather_data:
                    self.pressure_label.config(
                        text=f"{weather_data['pressure_mb']} mb")
                else:
                    self.pressure_label.config(text="N/A")

            else:
                self.show_error("City not found. Please try another city.")

        except Exception as e:
            print(f"Error: {e}")  # For debugging
            self.show_error("Unable to fetch weather data. Please try again.")

    def show_error(self, message):
        """Show error message"""
        self.city_label.config(text="Error", fg=self.ERROR_COLOR)
        self.condition_label.config(text=message)
        self.reset_weather_display()

    def reset_weather_display(self):
        """Reset weather display to default values"""
        self.temp_label.config(text="--°")
        self.feels_like_label.config(text="--°")
        self.wind_label.config(text="-- km/h")
        self.humidity_label.config(text="--%")
        self.pressure_label.config(text="-- mb")


def main():
    backend = WeatherApp()
    root = tk.Tk()
    UI = WeatherAppUI(backend=backend, root=root)


if __name__ == "__main__":
    main()
