# importing the libraries
import flet as ft
import speedtest
from time import sleep

# defining the main function
def main(page: ft.Page):

    # setting up the page
    page.title = "Internet Speed Test"
    page.theme_mode = "dark"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.padding = 30
    page.window_bgcolor = "blue"
    page.bgcolor = "#000000"

    # enabling scroll in the page
    page.auto_scroll = True

    # configuring the fonts
    page.fonts = {
        "SourceCodePro-BlackItalic": "fonts/SourceCodePro-BlackItalic.ttf",
        "SourceCodePro-Bold": "fonts/SourceCodePro-Bold.ttf",
        "RoosterPersonalUse": "fonts/RoosterPersonalUse-3z8d8.ttf"
    }

    # initializing the speedtest variable
    st = speedtest.Speedtest()

    # making the heading of the app
    appTitle = ft.Row(
        controls = [
            ft.Text("Internet", font_family="RoosterPersonalUse", style="displayLarge", color="#ff3300"),
            ft.Text("Speed", font_family="RoosterPersonalUse", style="displayLarge", color="#ffff00")
        ],
        alignment="center"
    )

    # defining terminal lines for printing text
    line_01 = ft.Text(value="> press start...", font_family="SourceCodePro-BlackItalic", color="#ffffff")
    line_02 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_03 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    progress_bar_01 = ft.ProgressBar(width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text_01 = ft.Text(" ", font_family="SourceCodePro-BlackItalic", color="#1aff1a", opacity=0)
    progress_row_01 = ft.Row([progress_text_01,progress_bar_01])
    line_04 = ft.Text(value="", font_family="SourceCodePro-Bold", color="#ffff00")
    line_05 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_06 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    progress_bar_02 = ft.ProgressBar(width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text_02 = ft.Text(" ", font_family="SourceCodePro-BlackItalic", color="#1aff1a", opacity=0)
    progress_row_02 = ft.Row([progress_text_02,progress_bar_02])
    line_07 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#ffff00")
    line_08 = ft.Text(value="", font_family="SourceCodePro-Bold", color="#ffffff")
    terminalText = ft.Column([line_01, line_02, line_03, progress_row_01, line_04, line_05, line_06, progress_row_02, line_07, line_08])

    # terminal container
    getSpeedContainer = ft.Container(
        content = terminalText,
        width=200,
        height=100,
        bgcolor="#4d4d4d",
        border_radius=30,
        padding=20,
        animate=ft.animation.Animation(1000, "bounceOut"),
    )

    # terminal animation
    def animate_getSpeedContainer(e):
        progress_row_01.opacity = 0
        progress_bar_01.opacity = 0
        progress_bar_01.value = None
        progress_row_02.opacity = 0
        progress_bar_02.opacity = 0
        progress_bar_02.value = None
        line_01.value = ""
        line_02.value = ""
        line_03.value = ""
        line_04.value = ""
        line_05.value = ""
        line_06.value = ""
        line_07.value = ""
        line_08.value = ""
        getSpeedContainer.update()
        getSpeedContainer.width = 700
        getSpeedContainer.height = 400
        line_01.value = "> calculating download speed, please wait..."
        getSpeedContainer.update()
        sleep(1)
        ideal_server = st.get_best_server() # this will find out and connect to the best possible server
        city = ideal_server["name"] # for getting the city name
        country = ideal_server["country"] # for getting the country name
        cc = ideal_server["cc"] # for getting the country code
        line_02.value = f"> finding the best possible servers in {city}, {country} ({cc})"
        getSpeedContainer.update()
        sleep(2)
        line_03.value = "> connection established, status OK, fetching download speed"
        progress_row_01.opacity = 1
        progress_bar_01.opacity = 1
        getSpeedContainer.update()
        download_speed = st.download()/1024/1024 # bytes/sec to Mbps
        progress_bar_01.value = 1
        line_04.value = f"> the download speed is {str(round(download_speed,2))} Mbps"
        getSpeedContainer.update()
        line_05.value = "> calculating upload speed, please wait..."
        getSpeedContainer.update()
        sleep(1)
        line_06.value = "> executing upload script, hold on"
        progress_row_02.opacity = 1
        progress_bar_02.opacity = 1
        getSpeedContainer.update()
        upload_speed = st.upload()/1024/1024 # bytes/sec to Mbps
        progress_bar_02.value = 1
        line_07.value = f"> the upload speed is {str(round(upload_speed,2))} Mbps"
        getSpeedContainer.update()
        sleep(1)
        line_08.value = f"> task completed successfully\n\n>> app developer: kumar anurag (instagram: kmranrg)"
        getSpeedContainer.update()

    # page components
    page.add(
        appTitle,
        getSpeedContainer,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=animate_getSpeedContainer, icon_color="#1aff1a", icon_size=50),
    )

# executing the main function
ft.app(target=main, assets_dir="assets")