# importing the libraries
import flet as ft
import speedtest
from time import sleep
from TypeWriterEffectControl import TypeWriterControl

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
    line_01 = TypeWriterControl(value="> press start...", font_family="SourceCodePro-BlackItalic", color="#ffffff")
    line_02 = TypeWriterControl(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_03 = TypeWriterControl(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    progress_bar_01 = ft.ProgressBar(width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text_01 = TypeWriterControl(" ", font_family="SourceCodePro-BlackItalic", color="#1aff1a", transparency=False)
    progress_row_01 = ft.Row([progress_text_01,progress_bar_01])
    line_04 = TypeWriterControl(value="", font_family="SourceCodePro-Bold", color="#ffff00")
    line_05 = TypeWriterControl(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_06 = TypeWriterControl(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    progress_bar_02 = ft.ProgressBar(width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text_02 = TypeWriterControl(" ", font_family="SourceCodePro-BlackItalic", color="#1aff1a", transparency=False)
    progress_row_02 = ft.Row([progress_text_02,progress_bar_02])
    line_07 = TypeWriterControl(value="", font_family="SourceCodePro-BlackItalic", color="#ffff00")
    line_08 = TypeWriterControl(value="", font_family="SourceCodePro-Bold", color="#ffffff")
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
        line_01.text_to_print = ""
        line_01.update()
        line_02.text_to_print = ""
        line_02.update()
        line_03.text_to_print = ""
        line_03.update()
        line_04.text_to_print = ""
        line_04.update()
        line_05.text_to_print = ""
        line_05.update()
        line_06.text_to_print = ""
        line_06.update()
        line_07.text_to_print = ""
        line_07.update()
        line_08.text_to_print = ""
        line_08.update()
        getSpeedContainer.update()
        getSpeedContainer.width = 700
        getSpeedContainer.height = 400
        line_01.text_to_print = "> calculating download speed, please wait..."
        getSpeedContainer.update()
        sleep(1)
        line_01.update()
        ideal_server = st.get_best_server() # this will find out and connect to the best possible server
        city = ideal_server["name"] # for getting the city name
        country = ideal_server["country"] # for getting the country name
        cc = ideal_server["cc"] # for getting the country code
        line_02.text_to_print = f"> finding the best possible servers in {city}, {country} ({cc})"
        line_02.update()
        getSpeedContainer.update()
        sleep(2)
        line_03.text_to_print = "> connection established, status OK, fetching download speed"
        line_03.update()
        progress_row_01.opacity = 1
        progress_bar_01.opacity = 1
        getSpeedContainer.update()
        download_speed = st.download()/1024/1024 # bytes/sec to Mbps
        progress_bar_01.value = 1
        line_04.text_to_print = f"> the download speed is {str(round(download_speed,2))} Mbps"
        line_04.update()
        getSpeedContainer.update()
        line_05.text_to_print = "> calculating upload speed, please wait..."
        line_05.update()
        getSpeedContainer.update()
        sleep(1)
        line_06.text_to_print = "> executing upload script, hold on"
        line_06.update()
        progress_row_02.opacity = 1
        progress_bar_02.opacity = 1
        getSpeedContainer.update()
        upload_speed = st.upload()/1024/1024 # bytes/sec to Mbps
        progress_bar_02.value = 1
        line_07.text_to_print = f"> the upload speed is {str(round(upload_speed,2))} Mbps"
        line_07.update()
        getSpeedContainer.update()
        sleep(1)
        line_08.text_to_print = f"> task completed successfully\n\n>> app developer: kumar anurag (instagram: kmranrg)"
        line_08.update()
        getSpeedContainer.update()

    # page components
    page.add(
        appTitle,
        getSpeedContainer,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=animate_getSpeedContainer, icon_color="#1aff1a", icon_size=50),
    )

# executing the main function
ft.app(target=main, assets_dir="assets")