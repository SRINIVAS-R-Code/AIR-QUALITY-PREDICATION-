# Air Quality Analytics Dashboard

A real-time, gesture-controlled air quality monitoring system.

## Features
*   **Live Dashboard**: Real-time AQI monitoring with auto-refreshing charts.
*   **All-India Coverage**: Search and view data for any city.
*   **Global Heatmap**: Interactive map showing pollution levels worldwide.
*   **Health Insights**: Automated health recommendations based on air quality.

## Setup & Run

1.  **Activate Environment**:
    ```bash
    .\env\Scripts\activate
    ```

2.  **Run Server**:
    ```bash
    python manage.py runserver
    ```
    Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Technology Stack
*   **Backend**: Django, Django REST Framework
*   **Frontend**: HTML5, CSS3 (Glassmorphism), D3.js
*   **API**: WAQI (World Air Quality Index)
