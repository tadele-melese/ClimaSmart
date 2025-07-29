import argparse
import sys

from climasmart.indices import compute_spi, compute_spei
from climasmart.geospatial.region import Region
from climasmart.visualization import run_dashboard
from climasmart.anomaly.detect_anomaly import detect_anomaly
from climasmart.anomaly.forecast import forecast_lstm
from climasmart.anomaly.drought_event_detector import detect_drought_events
from climasmart.anomaly.explainability import explain_forecast


def main():
    parser = argparse.ArgumentParser(
        prog="climasmart",
        description="ClimaSmart: A Climate Monitoring Toolkit"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 📈 SPI
    spi_parser = subparsers.add_parser("spi", help="Compute SPI index")
    spi_parser.add_argument("--input", required=True, help="Path to precipitation data (CSV or NetCDF)")
    spi_parser.add_argument("--scale", type=int, default=3, help="Time scale in months (default: 3)")

    # 📉 SPEI
    spei_parser = subparsers.add_parser("spei", help="Compute SPEI index")
    spei_parser.add_argument("--precip", required=True, help="Precipitation data path")
    spei_parser.add_argument("--pet", required=True, help="Potential Evapotranspiration data path")
    spei_parser.add_argument("--scale", type=int, default=3, help="Time scale (default: 3)")

    # 🌍 Batch Processing
    batch_parser = subparsers.add_parser("batch-process", help="Run batch zonal processing")
    batch_parser.add_argument("--shapefile", required=True, help="Path to shapefile")
    batch_parser.add_argument("--start", required=True, help="Start date (YYYY-MM)")
    batch_parser.add_argument("--end", required=True, help="End date (YYYY-MM)")

    # 🧪 Dashboard
    dash_parser = subparsers.add_parser("dashboard", help="Launch Streamlit dashboard")

    # 🔎 Anomaly Detection
    anomaly_parser = subparsers.add_parser("anomaly", help="Detect anomalies in climate data")
    anomaly_parser.add_argument("--input", required=True, help="Path to input CSV or NetCDF")
    anomaly_parser.add_argument("--method", default="zscore", choices=["zscore", "threshold"], help="Detection method")

    # 🔮 Forecast
    forecast_parser = subparsers.add_parser("forecast", help="Run LSTM-based forecasting")
    forecast_parser.add_argument("--input", required=True, help="Path to time series data (CSV)")
    forecast_parser.add_argument("--steps", type=int, default=12, help="Forecast steps into future")

    # 🏜️ Drought Events
    drought_parser = subparsers.add_parser("drought-events", help="Detect drought periods from index")
    drought_parser.add_argument("--index", required=True, help="SPI/SPEI time series CSV")
    drought_parser.add_argument("--threshold", type=float, default=-1.0, help="Threshold for drought")

    # 🧠 Explainability
    explain_parser = subparsers.add_parser("explain", help="Explain LSTM predictions using SHAP")
    explain_parser.add_argument("--model", required=True, help="Path to trained model")
    explain_parser.add_argument("--data", required=True, help="Input features for explanation")

    args = parser.parse_args()

    if args.command == "spi":
        print(f"Computing SPI from {args.input} with scale {args.scale}...")
        compute_spi(args.input, scale=args.scale)

    elif args.command == "spei":
        print(f"Computing SPEI from {args.precip} & {args.pet} with scale {args.scale}...")
        compute_spei(args.precip, args.pet, scale=args.scale)

    elif args.command == "batch-process":
        print(f"Processing {args.shapefile} from {args.start} to {args.end}...")
        region = Region.from_shapefile(args.shapefile)
        region.batch_process(start=args.start, end=args.end)

    elif args.command == "dashboard":
        print("Launching dashboard...")
        if run_dashboard:
            run_dashboard()
        else:
            print("Streamlit not installed. Dashboard cannot be launched.")

    elif args.command == "anomaly":
        print(f"Detecting anomalies in {args.input} using method {args.method}...")
        detect_anomaly(args.input, method=args.method)

    elif args.command == "forecast":
        print(f"Forecasting future {args.steps} steps using LSTM...")
        forecast_lstm(args.input, steps=args.steps)

    elif args.command == "drought-events":
        print(f"Detecting drought events in {args.index} using threshold {args.threshold}...")
        detect_drought_events(args.index, threshold=args.threshold)

    elif args.command == "explain":
        print(f"Explaining model {args.model} using input {args.data}...")
        explain_forecast(args.model, args.data)

    else:
        parser.print_help()


if __name__ == "__main__":
    sys.exit(main())
