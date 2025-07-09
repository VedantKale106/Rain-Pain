# ☔ RainRouteChecker: Don't Get Caught Drowning (Unless You Want To) 🚗

Ever planned a perfect road trip, only to find yourself navigating through a surprise monsoon? 🌧️ Or maybe you just enjoy a good downpour and want to ensure you hit every single one? Either way, **RainRouteChecker** is your new best friend (or worst enabler).

This Flask application meticulously plots your route and then, with a sinister chuckle, tells you precisely where and when you're likely to encounter rain. Because who needs sunshine when you can have a perpetually damp journey? 😈

-----

## 💀 Features That Will Make You Question Your Life Choices

  * **📍 Precision Location Pinpointing:** We use OpenRouteService to convert your vague destination ideas into precise coordinates. No more getting lost... unless you prefer that.
  * **🛣️ Route Mapping (The Path to Wetness):** Get a detailed route, broken down into segments, so you can track your inevitable soggy progress.
  * **☔ Real-Time Rain Forecasts (Prepare for the Inevitable):** Leveraging the OpenWeatherMap API, we pull 3-hour rain forecasts for various points along your journey. We'll tell you if it's "Light Rain," "Moderate Rain," or "Heavy Rain." Choose your own adventure\!
  * **⚠️ Rain Alerts (Because We Care, Kinda):** Get a heads-up if "Moderate" or "Heavy" rain is expected. This way, you can either prepare your ark or just embrace the aquatic experience.
  * **📊 Overall Rain Assessment:** A delightful percentage showing how much of your journey is predicted to be a watery wonderland. Aim for 100% for the true masochist's experience\!
  * **🕰️ Time-Based Forecasts:** We even estimate your arrival time at each sampled point, so you know exactly when to start building that sandcastle... or digging that grave.

-----

## 🛠️ Getting Your Boots Wet: Installation

To get this glorious monument to meteorological misery running, follow these simple steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/RainRouteChecker.git
    cd RainRouteChecker
    ```

2.  **Set up your virtual environment (highly recommended, unless you enjoy dependency hell):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install the necessary dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *(Don't forget to create a `requirements.txt` file from your current environment: `pip freeze > requirements.txt`)*

4.  **Obtain API Keys (The Keys to Your Drowning):**
    You'll need API keys from:

      * **OpenRouteService:** For routing and geocoding. Get yours [here](https://openrouteservice.org/).
      * **OpenWeatherMap:** For the delightful rain forecasts. Sign up [here](https://openweathermap.org/api).

5.  **Create your `.env` file (where secrets go to die):**
    In the root directory of your project, create a file named `.env` and add your API keys:

    ```
    ORS_API_KEY="your_openrouteservice_api_key_here"
    WEATHER_API_KEY="your_openweathermap_api_key_here"
    ```

    *Don't share this file with anyone unless you want them to track your every soggy move.*

6.  **Run the application (and face your destiny):**

    ```bash
    python app.py
    ```

    The app will typically run on `http://127.0.0.1:5000`. Open your browser and prepare to embrace the dampness.

-----

## 💡 How to Use (Before the Flood)

1.  Open your browser and navigate to the application.
2.  Enter your **starting location** (e.g., "Junnar").
3.  Enter your **destination** (e.g., "Pune").
4.  Specify your **departure time** (e.g., "09:00").
5.  Click "Check Rain."
6.  Observe the detailed breakdown of your route, complete with estimated times and the glorious rain forecast at each point. The `rain_level` (0-3) gives you a quick visual indicator of how wet you'll get.

-----

## 🤷‍♀️ Why Did I Build This?

Because life is too short for pleasant surprises. And sometimes, you just want to know if you need to pack an umbrella, a submarine, or just a good therapist for the journey ahead. Plus, who doesn't love a good excuse to cancel plans because "the forecast said so"?

-----

## 🤝 Contributing (If You Dare)

Feel free to fork this project and contribute. Whether it's adding more weather data, optimizing routes for *maximum* rain exposure, or just fixing a typo, all contributions are welcome. Just send a pull request, and we can discuss the best way to further our collective misery.


-----
## 🔫 Screenshots

<img width="1917" height="915" alt="Image" src="https://github.com/user-attachments/assets/5afabef0-ff52-4609-a84b-55fd966a33b2" />
<img width="1887" height="918" alt="Image" src="https://github.com/user-attachments/assets/2b5d08ab-bdee-41be-be1e-9d04eda3668f" />
<img width="1887" height="918" alt="Image" src="https://github.com/user-attachments/assets/abbe557a-55bf-498b-aae8-a19535f3accd" />




-----

Made with 💔 by Vedant

-----
