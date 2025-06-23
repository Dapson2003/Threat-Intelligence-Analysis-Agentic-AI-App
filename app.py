from ui.streamlit_app import main as streamlit_main

if __name__ == "__main__":
    open("log.txt", "a").write("")
    streamlit_main()