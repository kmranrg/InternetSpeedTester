import flet as ft
import speedtest
from time import sleep

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

    appTitle = ft.Row(
        controls = [
            ft.Text("Internet", font_family="RoosterPersonalUse", style="displayLarge", color="#ff3300"),
            ft.Text("Speed", font_family="RoosterPersonalUse", style="displayLarge", color="#ffff00")
        ],
        alignment="center"
    )

    line_01 = ft.Text(value="> press start...", font_family="SourceCodePro-BlackItalic", color="#ffffff")
    line_02 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_03 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_04 = ft.Text(value="", font_family="SourceCodePro-Bold", color="#ffff00")
    line_05 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_06 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_07 = ft.Text(value="", font_family="SourceCodePro-BlackItalic", color="#ffff00")
    line_08 = ft.Text(value="", font_family="SourceCodePro-Bold", color="#ffffff")
    terminalText = ft.Column([line_01, line_02, line_03, line_04, line_05, line_06, line_07, line_08])

    getSpeedContainer = ft.Container(
        content = terminalText,
        width=200,
        height=100,
        bgcolor="#4d4d4d",
        border_radius=30,
        padding=20,
        animate=ft.animation.Animation(1000, "bounceOut"),
    )

    def animate_getSpeedContainer(e):
        line_01.value = ""
        line_02.value = ""
        line_03.value = ""
        line_04.value = ""
        line_05.value = ""
        line_06.value = ""
        line_07.value = ""
        line_08.value = ""
        getSpeedContainer.update()
        getSpeedContainer.width = 700 if getSpeedContainer.width == 200 else 700
        getSpeedContainer.height = 400 if getSpeedContainer.height == 100 else 400
        line_01.value = "> calculating download speed, please wait..."
        getSpeedContainer.update()
        sleep(1)
        ideal_server = st.get_best_server()
        city = ideal_server["name"]
        country = ideal_server["country"]
        cc = ideal_server["cc"]
        line_02.value = f"> finding the best possible servers in {city}, {country} ({cc})"
        getSpeedContainer.update()
        sleep(2)
        line_03.value = "> connection established, status OK, fetching download speed"
        getSpeedContainer.update()
        download_speed = st.download()/1024/1024 # bytes/sec to Mbps
        line_04.value = f"> the download speed is {str(round(download_speed,2))} Mbps"
        getSpeedContainer.update()
        line_05.value = "> calculating upload speed, please wait..."
        getSpeedContainer.update()
        sleep(1)
        line_06.value = "> executing upload script, hold on"
        getSpeedContainer.update()
        upload_speed = st.upload()/1024/1024 # bytes/sec to Mbps
        line_07.value = f"> the upload speed is {str(round(upload_speed,2))} Mbps"
        getSpeedContainer.update()
        sleep(1)
        line_08.value = f"> task completed successfully\n\n>> app developer: kumar anurag (instagram: kmranrg)"
        getSpeedContainer.update()

    page.add(
        appTitle,
        getSpeedContainer,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=animate_getSpeedContainer, icon_color="#1aff1a", icon_size=50),
    )

ft.app(target=main, assets_dir="assets")