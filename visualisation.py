import matplotlib.pyplot as plt
import pandas as pd


def generate_charts(df):
    """Generate the four air quality charts from a DataFrame df with date, station, hour, pm25, and temperature_c."""
    # PM2.5 trend for one station
    one = df[df["station"] == "Adyar"].groupby("date")["pm25"].mean()
    one.plot(kind="line", marker="o", title="Daily PM2.5 Trend - Adyar")
    plt.xlabel("Date")
    plt.ylabel("PM2.5")
    plt.tight_layout()
    plt.savefig("trend.png")
    plt.close()

    # Compare station means
    df.groupby("station")["pm25"].mean().plot(kind="bar", title="Mean PM2.5 by Station")
    plt.xlabel("Station")
    plt.ylabel("Mean PM2.5")
    plt.tight_layout()
    plt.savefig("stations.png")
    plt.close()

    # Temperature relationship
    plt.scatter(df["temperature_c"], df["pm25"])
    plt.title("Temperature vs PM2.5")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("PM2.5")
    plt.tight_layout()
    plt.savefig("temperature_scatter.png")
    plt.close()

    # Worst hours
    df.groupby("hour")["pm25"].mean().plot(kind="bar", title="Mean PM2.5 by Hour")
    plt.xlabel("Hour of day")
    plt.ylabel("Mean PM2.5")
    plt.tight_layout()
    plt.savefig("worst_hours.png")
    plt.close()


if __name__ == "__main__":
    sample_data = pd.DataFrame({
        "station": ["Adyar", "Adyar", "Guindy", "Guindy"],
        "date": ["2026-10-01", "2026-10-02", "2026-10-01", "2026-10-02"],
        "hour": [8, 18, 9, 20],
        "pm25": [48.0, 60.0, 95.0, 121.0],
        "temperature_c": [29.5, 31.0, 32.0, 33.5]
    })
    generate_charts(sample_data)
