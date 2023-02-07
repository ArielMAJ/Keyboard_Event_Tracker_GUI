"""
Floating (main) window implementation.
"""

import customtkinter as ctk  # type: ignore[import]
from utilities.im_processing import load_img  # type: ignore[import]
from utilities.paths import join_pr  # type: ignore[import]


class FloatingWindow(ctk.CTk):
    """
    Floating (main) window class.

    This window shows whether a button has been pressed.
    It will switch the light color whenever it's pressed.
    """

    def __init__(self):
        super().__init__()
        self.widgets: dict = {}
        self.settings: dict = {}
        self.images: dict = {}
        self._load_app()

    def _load_app(self) -> None:
        """
        This function will call subfunctions to load the app.
        """
        self._basic_configs()
        self._place_widgets()
        self._place_window_on_screen()

    def _basic_configs(self):
        """
        This function should contain most basic configs.
        """
        self.withdraw()
        self.after(500, self.deiconify)

        self.title("")
        self.resizable(width=False, height=False)
        self.config(padx=5, pady=5)

        self.images["red_light"] = load_img(
            join_pr("images", "red_light.png"), (25, 25)
        )
        self.images["green_light"] = load_img(
            join_pr("images", "green_light.png"), (25, 25)
        )

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(10, weight=1)
        # self.grid_columnconfigure(1, weight=1)

        # self.overrideredirect(True)
        # self.attributes("-disabled", True)
        # self.attributes("-transparentcolor", "black")

        self.attributes("-alpha", 0.8)
        self.attributes("-topmost", True)

    def _place_window_on_screen(self) -> None:
        self.update()
        self.withdraw()

        window_size = {"x": self.winfo_reqwidth(), "y": self.winfo_reqheight()}
        offset = {
            "x": int(
                self.winfo_screenwidth()
                - window_size["x"]
                - 15
                - 40 * 200 / window_size["x"]
            ),
            "y": int(0.93 * self.winfo_screenheight() - window_size["y"] - 55),
        }
        self.geometry(f"+{offset['x']}+{offset['y']}")

    def _place_widgets(self) -> None:
        """
        This function should handle creating and placing most of the widgets.
        """

        row = 1
        self.widgets["lbl_F2"] = ctk.CTkLabel(
            self,
            text="F2",  # Folder
            # Set "bg" to "self.colors["app_bg_color"]" once all widgets are placed.
            # bg_color="green",  # self.colors["app_bg_color"],
            width=50,
            # anchor="w",
            # justify="left",
        )
        self.widgets["lbl_F2"].grid(
            row=row,
            column=0,
            # padx=self.settings["padx"],
            # pady=self.settings["pady"],
            sticky="NEWS",
        )
        self.widgets["lbl_F2_description"] = ctk.CTkLabel(
            self,
            text="(Discord Mic)",  # Folder
            # Set "bg" to "self.colors["app_bg_color"]" once all widgets are placed.
            # bg_color="green",  # self.colors["app_bg_color"],
            width=50,
            anchor="w",
            justify="left",
        )
        self.widgets["lbl_F2_description"].grid(
            row=row,
            column=1,
            # padx=self.settings["padx"],
            # pady=self.settings["pady"],
            sticky="NEWS",
        )
        self.widgets["lbl_F2_light"] = ctk.CTkLabel(
            self,
            text="",  # Folder
            image=self.images["red_light"],
            # Set "bg" to "self.colors["app_bg_color"]" once all widgets are placed.
            # bg_color="green",  # self.colors["app_bg_color"],
        )
        self.widgets["lbl_F2_light"].grid(
            row=row,
            column=2,
            padx=10,  # self.settings["padx"],
            # padx=self.settings["padx"],
            # pady=self.settings["pady"],
            sticky="NEWS",
        )
        self.widgets["lbl_F2_light"].is_red = True

        self.bind(
            "<F2>",
            lambda x: self.btn_pressed(self.widgets["lbl_F2_light"]),
        )

        row += 1
        self.widgets["lbl_F3"] = ctk.CTkLabel(
            self,
            text="F3",  # Folder
            # Set "bg" to "self.colors["app_bg_color"]" once all widgets are placed.
            # bg_color="green",  # self.colors["app_bg_color"],
            width=5,
            # anchor="w",
            # justify="left",
        )
        self.widgets["lbl_F3"].grid(
            row=row,
            column=0,
            # padx=self.settings["padx"],
            # pady=self.settings["pady"],
            sticky="NEWS",
        )
        self.widgets["lbl_F3_description"] = ctk.CTkLabel(
            self,
            text="(Discord Camera)",  # Folder
            # Set "bg" to "self.colors["app_bg_color"]" once all widgets are placed.
            # bg_color="green",  # self.colors["app_bg_color"],
            width=5,
            anchor="w",
            justify="left",
        )
        self.widgets["lbl_F3_description"].grid(
            row=row,
            column=1,
            # padx=self.settings["padx"],
            # pady=self.settings["pady"],
            sticky="NEWS",
        )
        self.widgets["lbl_F3_light"] = ctk.CTkLabel(
            self,
            text="",  # Folder
            image=self.images["green_light"],
            # Set "bg" to "self.colors["app_bg_color"]" once all widgets are placed.
            # bg_color="green",  # self.colors["app_bg_color"],
        )
        self.widgets["lbl_F3_light"].grid(
            row=row,
            column=2,
            padx=10,  # self.settings["padx"],
            # pady=self.settings["pady"],
            sticky="NEWS",
        )
        self.widgets["lbl_F3_light"].is_red = False

        self.bind(
            "<F3>",
            lambda x: self.btn_pressed(self.widgets["lbl_F3_light"]),
        )

    def btn_pressed(self, widget):
        """
        This function should be called on button presses.
        It should receive the light widget.
        It will switch the light's color.
        """
        if widget.is_red:
            widget.configure(image=self.images["green_light"])
            widget.is_red = False
        else:
            widget.configure(image=self.images["red_light"])
            widget.is_red = True
