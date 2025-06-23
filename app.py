from ui.streamlit_app import main as streamlit_main
from datetime import datetime

if __name__ == "__main__":
    current_datetime = datetime.now()
    open("log.txt", "w").write(f"log from {current_datetime}")
    streamlit_main()