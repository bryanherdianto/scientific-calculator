from flet import *
import math
from math import *
import re


class CalculatorApp(UserControl):
    def build(self):
        self.temp_calculation = ""
        self.menu_hyp = False
        self.menu_setup = False
        self.history_track = -1
        self.calculation_history = []
        self.result_history = []
        self.cursor_pos = 0
        self.real_calculation = ""
        self.calculation = Text(value="", color=colors.WHITE, size=20)
        self.result = Text(value="", color=colors.WHITE, size=20)
        self.extra = Text(value="", color=colors.WHITE, size=20)
        self.new_calculation = True
        self.prev_ans = ""
        self.is_calculator_on = False
        self.off = colors.BLACK
        self.inactive = colors.with_opacity(0.1, colors.WHITE)
        self.active = colors.WHITE
        self.shift = Text(value="S", color=self.off, size=10)
        self.alpha = Text(value="A", color=self.off, size=10)
        self.m = Text(value="M", color=self.off, size=10)
        self.sto = Text(value="STO", color=self.off, size=10)
        self.rcl = Text(value="RCL", color=self.off, size=10)
        self.stat = Text(value="STAT", color=self.off, size=10)
        self.cmplx = Text(value="CMPLX", color=self.off, size=10)
        self.mat = Text(value="MAT", color=self.off, size=10)
        self.vct = Text(value="VCT", color=self.off, size=10)
        self.d = Text(value="D", color=self.off, size=10)
        self.r = Text(value="R", color=self.off, size=10)
        self.g = Text(value="G", color=self.off, size=10)
        self.fix = Text(value="FIX", color=self.off, size=10)
        self.sci = Text(value="SCI", color=self.off, size=10)
        self.math = Text(value="Math", color=self.off, size=10)
        self.down = Text(value="▼", color=self.off, size=10)
        self.up = Text(value="▲", color=self.off, size=10)
        self.disp = Text(value="Disp", color=self.off, size=10)
        self.text_box_1 = Row(
            controls=[self.calculation],
            alignment=MainAxisAlignment.START,
        )
        self.text_box_2 = Row(
            controls=[self.extra],
            alignment=MainAxisAlignment.START,
        )
        self.text_box_3 = Row(controls=[self.result], alignment=MainAxisAlignment.END)

        # application's root control (i.e. "view") containing all other controls
        return Container(
            width=500,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                controls=[
                    Row(
                        controls=[
                            self.shift,
                            self.alpha,
                            self.m,
                            self.sto,
                            self.rcl,
                            self.stat,
                            self.cmplx,
                            self.mat,
                            self.vct,
                            self.d,
                            self.r,
                            self.g,
                            self.fix,
                            self.sci,
                            self.math,
                            self.down,
                            self.up,
                            self.disp,
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    self.text_box_1,
                    self.text_box_2,
                    self.text_box_3,
                    Row(
                        controls=[
                            ElevatedButton(
                                content=Text(value="SHIFT", size=12),
                                bgcolor=colors.DEEP_ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="SHIFT",
                            ),
                            ElevatedButton(
                                content=Text(value="ALPHA", size=11),
                                bgcolor=colors.RED,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="ALPHA",
                            ),
                            ElevatedButton(
                                text="▲",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="up",
                            ),
                            ElevatedButton(
                                content=Text(value="MODE", size=12),
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="MODE",
                            ),
                            ElevatedButton(
                                text="ON",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="ON",
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                bgcolor=colors.BLACK,
                                expand=2,
                            ),
                            ElevatedButton(
                                text="◀",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="left",
                            ),
                            ElevatedButton(
                                text="▶",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="right",
                            ),
                            ElevatedButton(
                                bgcolor=colors.BLACK,
                                expand=2,
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="Abs",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="abs(",
                            ),
                            ElevatedButton(
                                text="x³",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="^3",
                            ),
                            ElevatedButton(
                                text="▼",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="down",
                            ),
                            ElevatedButton(
                                text="x⁻¹",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="^-1",
                            ),
                            ElevatedButton(
                                text="x!",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="!",
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="√",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="√(",
                            ),
                            ElevatedButton(
                                text="x²",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="^2",
                            ),
                            ElevatedButton(
                                text="xⁿ",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="^(",
                            ),
                            ElevatedButton(
                                content=Text(value="log", size=12),
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="log(",
                            ),
                            ElevatedButton(
                                text="ln",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="ln(",
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="°’”",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="°’”",
                            ),
                            ElevatedButton(
                                content=Text(value="hyp", size=11),
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="hyp",
                            ),
                            ElevatedButton(
                                content=Text(value="sin", size=12),
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="sin(",
                            ),
                            ElevatedButton(
                                content=Text(value="cos", size=12),
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="cos(",
                            ),
                            ElevatedButton(
                                content=Text(value="tan", size=12),
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="tan(",
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                content=Text(value="RCL", size=11),
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="",
                            ),
                            ElevatedButton(
                                content=Text(value="ENG", size=10),
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="",
                            ),
                            ElevatedButton(
                                text="(",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="(",
                            ),
                            ElevatedButton(
                                text=")",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data=")",
                            ),
                            ElevatedButton(
                                content=Text(value="M+", size=12),
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="",
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="7",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="7",
                            ),
                            ElevatedButton(
                                text="8",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="8",
                            ),
                            ElevatedButton(
                                text="9",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="9",
                            ),
                            ElevatedButton(
                                text="DEL",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="DEL",
                            ),
                            ElevatedButton(
                                text="AC",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="AC",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="4",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="4",
                            ),
                            ElevatedButton(
                                text="5",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="5",
                            ),
                            ElevatedButton(
                                text="6",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="6",
                            ),
                            ElevatedButton(
                                text="×",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="×",
                            ),
                            ElevatedButton(
                                text="÷",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="÷",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="1",
                            ),
                            ElevatedButton(
                                text="2",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="2",
                            ),
                            ElevatedButton(
                                text="3",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="3",
                            ),
                            ElevatedButton(
                                text="+",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="+",
                            ),
                            ElevatedButton(
                                text="-",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="-",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="0",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="0",
                            ),
                            ElevatedButton(
                                text=".",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data=".",
                            ),
                            ElevatedButton(
                                text="×10\u207f",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="×10^",
                            ),
                            ElevatedButton(
                                text="Ans",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="Ans",
                            ),
                            ElevatedButton(
                                text="=",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="=",
                            ),
                        ]
                    ),
                ],
            ),
        )

    def make_factorial(self):
        while self.real_calculation.find("!") != -1:
            index = self.real_calculation.find("!") - 1
            while index > 0:
                if self.real_calculation[index] in (
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                ):
                    index -= 1
                else:
                    break
            if index == 0:
                self.real_calculation = (
                    self.real_calculation[:index]
                    + "math.factorial("
                    + self.real_calculation[index + 1 :]
                )
            else:
                self.real_calculation = (
                    self.real_calculation[: index + 1]
                    + "math.factorial("
                    + self.real_calculation[index + 1 :]
                )
            self.real_calculation = self.real_calculation.replace("!", ")", 1)

    def type_text(self, data):
        if self.new_calculation == True:
            self.prev_ans = self.result.value
            self.result.value = ""
            self.calculation.value = "|"
        self.calculation.value = self.calculation.value.replace("|", "")
        self.calculation.value = (
            self.calculation.value[: self.cursor_pos]
            + data
            + self.calculation.value[self.cursor_pos :]
        )
        self.cursor_pos += len(data)
        self.calculation.value = (
            self.calculation.value[: self.cursor_pos]
            + "|"
            + self.calculation.value[self.cursor_pos :]
        )
        self.new_calculation = False

    def delete_string(self):
        index_string = len(self.calculation.value) - 1
        if (
            index_string == self.calculation.value.rfind("×10^") + len("×10^") - 1
            and self.calculation.value.find("×10^") != -1
        ):
            self.calculation.value = "".join(self.calculation.value.rsplit("×10^", 1))
            self.cursor_pos -= len("×10^")
        elif (
            index_string == self.calculation.value.rfind("sin(") + len("sin(") - 1
            and self.calculation.value.find("sin(") != -1
        ):
            self.calculation.value = "".join(self.calculation.value.rsplit("sin(", 1))
            self.cursor_pos -= len("sin(")
        elif (
            index_string == self.calculation.value.rfind("cos(") + len("cos(") - 1
            and self.calculation.value.find("cos(") != -1
        ):
            self.calculation.value = "".join(self.calculation.value.rsplit("cos(", 1))
            self.cursor_pos -= len("cos(")
        elif (
            index_string == self.calculation.value.rfind("tan(") + len("tan(") - 1
            and self.calculation.value.find("tan(") != -1
        ):
            self.calculation.value = "".join(self.calculation.value.rsplit("tan(", 1))
            self.cursor_pos -= len("tan(")
        elif (
            index_string == self.calculation.value.rfind("sin⁻¹(") + len("sin⁻¹(") - 1
            and self.calculation.value.find("sin⁻¹(") != -1
        ):
            self.calculation.value = "".join(self.calculation.value.rsplit("sin⁻¹(", 1))
            self.cursor_pos -= len("sin⁻¹(")
        elif (
            index_string == self.calculation.value.rfind("cos⁻¹(") + len("cos⁻¹(") - 1
            and self.calculation.value.find("cos⁻¹(") != -1
        ):
            self.calculation.value = "".join(self.calculation.value.rsplit("cos⁻¹(", 1))
            self.cursor_pos -= len("cos⁻¹(")
        elif (
            index_string == self.calculation.value.rfind("tan⁻¹(") + len("tan⁻¹(") - 1
            and self.calculation.value.find("tan⁻¹(") != -1
        ):
            self.calculation.value = "".join(self.calculation.value.rsplit("tan⁻¹(", 1))
            self.cursor_pos -= len("tan⁻¹(")
        elif (
            index_string == self.calculation.value.rfind("Ans") + len("Ans") - 1
            and self.calculation.value.find("Ans") != -1
        ):
            self.calculation.value = "".join(self.calculation.value.rsplit("Ans", 1))
            self.cursor_pos -= len("Ans")
        elif (
            index_string == self.calculation.value.rfind("^(") + len("^(") - 1
            and self.calculation.value.find("^(") != -1
        ):
            self.calculation.value = "".join(self.calculation.value.rsplit("^(", 1))
            self.cursor_pos -= len("^(")
        elif (
            index_string == self.calculation.value.rfind("log(") + len("log(") - 1
            and self.calculation.value.find("log(") != -1
        ):
            self.calculation.value = "".join(self.calculation.value.rsplit("log(", 1))
            self.cursor_pos -= len("log(")
        elif (
            index_string == self.calculation.value.rfind("ln(") + len("ln(") - 1
            and self.calculation.value.find("ln(") != -1
        ):
            self.calculation.value = "".join(self.calculation.value.rsplit("ln(", 1))
            self.cursor_pos -= len("ln(")
        elif (
            index_string == self.calculation.value.rfind("abs(") + len("abs(") - 1
            and self.calculation.value.find("abs(") != -1
        ):
            self.calculation.value = "".join(self.calculation.value.rsplit("abs(", 1))
            self.cursor_pos -= len("abs(")
        else:
            self.calculation.value = (
                self.calculation.value[: self.cursor_pos - 1]
                + self.calculation.value[self.cursor_pos :]
            )
            self.cursor_pos -= 1

    def times_10_precedence(self):
        start_index = 0

        while start_index != -1:
            try:
                start_index = self.real_calculation.index("×10^") - 1
                while start_index >= 0:
                    if start_index == 0:
                        self.real_calculation = (
                            self.real_calculation[:start_index]
                            + "("
                            + self.real_calculation[start_index:]
                        )
                        break
                    elif self.real_calculation[start_index] not in (
                        "1",
                        "2",
                        "3",
                        "4",
                        "5",
                        "6",
                        "7",
                        "8",
                        "9",
                        "0",
                        ".",
                    ):
                        self.real_calculation = (
                            self.real_calculation[: start_index + 1]
                            + "("
                            + self.real_calculation[start_index + 1 :]
                        )
                        break
                    start_index -= 1

                end_index = self.real_calculation.index("×10^") + len("×10^")
                if self.real_calculation[end_index] == "-":
                    end_index += 1
                while end_index < len(self.real_calculation):
                    if end_index == len(self.real_calculation) - 1:
                        self.real_calculation = (
                            self.real_calculation[: end_index + 1]
                            + ")"
                            + self.real_calculation[end_index + 1 :]
                        )
                        break
                    elif self.real_calculation[end_index] not in (
                        "1",
                        "2",
                        "3",
                        "4",
                        "5",
                        "6",
                        "7",
                        "8",
                        "9",
                        "0",
                        ".",
                    ):
                        self.real_calculation = (
                            self.real_calculation[:end_index]
                            + ")"
                            + self.real_calculation[end_index:]
                        )
                        break
                    end_index += 1

                self.real_calculation = self.real_calculation.replace(
                    "×10^", "*10**", 1
                )
            except:
                start_index = -1

        return self.real_calculation

    def button_clicked(self, e):
        data = e.control.data

        if data == "ON":
            self.shift.color = self.inactive
            self.alpha.color = self.inactive
            self.m.color = self.active
            self.sto.color = self.inactive
            self.rcl.color = self.inactive
            self.stat.color = self.inactive
            self.cmplx.color = self.inactive
            self.mat.color = self.inactive
            self.vct.color = self.inactive
            self.d.color = self.active
            self.r.color = self.inactive
            self.g.color = self.inactive
            self.fix.color = self.inactive
            self.sci.color = self.inactive
            self.math.color = self.active
            self.down.color = self.inactive
            self.up.color = self.inactive
            self.disp.color = self.inactive
            self.is_calculator_on = True
            self.calculation.value = "|"
            self.cursor_pos = 0

        elif data == "AC" and self.is_calculator_on == True:
            if self.shift.color == self.active:
                self.is_calculator_on = False
                self.result.value = ""
                self.calculation.value = ""
                self.shift.color = self.off
                self.alpha.color = self.off
                self.m.color = self.off
                self.sto.color = self.off
                self.rcl.color = self.off
                self.stat.color = self.off
                self.cmplx.color = self.off
                self.mat.color = self.off
                self.vct.color = self.off
                self.d.color = self.off
                self.r.color = self.off
                self.g.color = self.off
                self.fix.color = self.off
                self.sci.color = self.off
                self.math.color = self.off
                self.down.color = self.off
                self.up.color = self.off
                self.disp.color = self.off
            else:
                self.cursor_pos = 0
                self.result.value = ""
                self.calculation.value = "|"

        elif (
            data == "MODE"
            and self.is_calculator_on == True
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            if self.shift.color == self.active:
                self.temp_calculation = self.calculation.value
                self.shift.color = self.inactive
                self.calculation.value = "1) Deg, 2) Rad"
                self.extra.value = ""
                self.result.value = ""
                self.menu_setup = True

        elif (
            data == "SHIFT"
            and self.is_calculator_on == True
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            self.shift.color = self.active
            self.alpha.color = self.inactive

        elif (
            data == "ALPHA"
            and self.is_calculator_on == True
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            self.alpha.color = self.active
            self.shift.color = self.inactive

        elif (
            data == "DEL"
            and self.is_calculator_on == True
            and self.new_calculation == False
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            self.calculation.value = self.calculation.value.replace("|", "")
            self.delete_string()
            self.calculation.value = (
                self.calculation.value[: self.cursor_pos]
                + "|"
                + self.calculation.value[self.cursor_pos :]
            )

        elif (
            data in ("up", "down")
            and self.is_calculator_on == True
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            if data == "up" and self.history_track != 0:
                self.history_track -= 1
                self.calculation.value = self.calculation_history[self.history_track]
                self.result.value = self.result_history[self.history_track]
            elif (
                data == "down"
                and self.history_track != len(self.calculation_history) - 1
            ):
                self.history_track += 1
                self.calculation.value = self.calculation_history[self.history_track]
                self.result.value = self.result_history[self.history_track]

        elif (
            data == "hyp"
            and self.is_calculator_on == True
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            self.temp_calculation = self.calculation.value
            self.calculation.value = "1) sinh, 2) cosh"
            self.extra.value = "3) tanh, 4) sinh⁻¹"
            self.result.value = "5) cosh⁻¹, 6) tanh⁻¹"
            self.text_box_3.alignment = MainAxisAlignment.START
            self.menu_hyp = True

        elif (
            data == "°’”"
            and self.is_calculator_on == True
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            if self.new_calculation == True:
                degree = int(self.result.value)
                arcmin = int((self.result.value - degree) * 60)
                arcsec = round(((self.result.value - degree) * 60 - arcmin) * 60, 2)
                self.result.value = (
                    str(degree) + "°" + str(arcmin) + "’" + str(arcsec) + "”"
                )
            else:
                self.type_text("°")

        elif (
            data in ("right", "left")
            and self.is_calculator_on == True
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            if self.calculation.value.find("|") == -1:
                self.result.value = ""
                self.calculation.value = self.calculation.value + "|"
                self.cursor_pos = len(self.calculation_history[self.history_track])
                self.new_calculation = False
            else:
                self.calculation.value = self.calculation.value.replace("|", "")
                if data == "right":
                    if self.cursor_pos < len(self.calculation.value):
                        self.cursor_pos += 1
                    else:
                        self.cursor_pos = 0
                elif data == "left":
                    if self.cursor_pos > 0:
                        self.cursor_pos -= 1
                    else:
                        self.cursor_pos = len(self.calculation.value)
                self.calculation.value = (
                    self.calculation.value[: self.cursor_pos]
                    + "|"
                    + self.calculation.value[self.cursor_pos :]
                )

        elif (
            data
            in (
                "(",
                ")",
                "0",
                ".",
                "Ans",
                "√(",
                "^-1",
                "^2",
                "^3",
                "^(",
                "log(",
                "ln(",
                "abs(",
                "!",
            )
            and self.is_calculator_on == True
        ):
            self.type_text(data)

        elif (
            data in ("1", "2", "3", "4", "5", "6", "7", "8", "9")
            and self.is_calculator_on == True
        ):
            if self.menu_hyp == True:
                if data == "1":
                    data = "sinh("
                elif data == "2":
                    data = "cosh("
                elif data == "3":
                    data = "tanh("
                elif data == "4":
                    data = "sinh⁻¹("
                elif data == "5":
                    data = "cosh⁻¹("
                elif data == "6":
                    data = "tanh⁻¹("
                self.calculation.value = self.temp_calculation
                self.extra.value = ""
                self.result.value = ""
                self.text_box_3.alignment = MainAxisAlignment.END
                self.menu_hyp = False
            elif self.menu_setup == True:
                if data == "1":
                    self.d.color = self.active
                    self.r.color = self.inactive
                elif data == "2":
                    self.r.color = self.active
                    self.d.color = self.inactive
                self.calculation.value = self.temp_calculation
                self.menu_setup = False
                data = ""
            self.type_text(data)

        elif (
            data == "×10^"
            and self.is_calculator_on == True
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            if self.shift.color == self.active:
                data = "π"
                self.shift.color = self.inactive
            elif self.alpha.color == self.active:
                data = "e"
                self.alpha.color = self.inactive
            self.type_text(data)

        elif (
            data == "sin("
            and self.is_calculator_on == True
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            if self.shift.color == self.active:
                data = "sin⁻¹("
                self.shift.color = self.inactive
            self.type_text(data)

        elif (
            data == "cos("
            and self.is_calculator_on == True
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            if self.shift.color == self.active:
                data = "cos⁻¹("
                self.shift.color = self.inactive
            self.type_text(data)

        elif (
            data == "tan("
            and self.is_calculator_on == True
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            if self.shift.color == self.active:
                data = "tan⁻¹("
                self.shift.color = self.inactive
            self.type_text(data)

        elif (
            data in ("+", "-", "×", "÷")
            and self.is_calculator_on == True
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            if self.new_calculation == True:
                self.prev_ans = self.result.value
                self.result.value = ""
                self.calculation.value = "|"

            if self.calculation.value == "|":
                self.calculation.value = self.calculation.value.replace("|", "")
                self.calculation.value = "Ans" + data
                self.cursor_pos = len(self.calculation.value)
                self.calculation.value = self.calculation.value + "|"
                self.new_calculation = False
            else:
                self.calculation.value = self.calculation.value.replace("|", "")
                self.calculation.value = (
                    self.calculation.value[: self.cursor_pos]
                    + data
                    + self.calculation.value[self.cursor_pos :]
                )
                self.cursor_pos += 1
                self.calculation.value = (
                    self.calculation.value[: self.cursor_pos]
                    + "|"
                    + self.calculation.value[self.cursor_pos :]
                )
                self.new_calculation = False

        elif (
            data == "="
            and self.is_calculator_on == True
            and self.menu_hyp == False
            and self.menu_setup == False
        ):
            self.calculation.value = self.calculation.value.replace("|", "")
            self.calculation_history.append(self.calculation.value)
            self.real_calculation = self.calculation.value
            self.real_calculation = self.times_10_precedence()
            self.real_calculation = self.real_calculation.replace("×", "*")
            self.real_calculation = self.real_calculation.replace("÷", "/")
            self.real_calculation = self.real_calculation.replace("π", str(pi))
            self.real_calculation = self.real_calculation.replace("e", str(math.e))
            self.real_calculation = self.real_calculation.replace("√(", "math.sqrt(")
            self.real_calculation = self.real_calculation.replace("^-1", "**-1")
            self.real_calculation = self.real_calculation.replace("^2", "**2")
            self.real_calculation = self.real_calculation.replace("^3", "**3")
            self.real_calculation = self.real_calculation.replace("^(", "**(")
            self.real_calculation = self.real_calculation.replace("log(", "math.log10(")
            self.real_calculation = self.real_calculation.replace("ln(", "math.log(")
            self.make_factorial()
            index = 0
            degree_found = False
            if self.real_calculation.find("°") != -1:
                degree_found = True
                while index < len(re.findall("([0-9]+)°", self.real_calculation)) - 1:
                    degree_str = re.findall("([0-9]+)°", self.real_calculation)[index]
                    arcmin_str = re.findall("([0-9]+)°", self.real_calculation)[
                        index + 1
                    ]
                    arcsec_str = re.findall("([0-9]+)°", self.real_calculation)[
                        index + 2
                    ]
                    degree = float(degree_str)
                    arcmin = float(arcmin_str) / 60.0
                    arcsec = float(arcsec_str) / 3600.0
                    conversion = degree + arcmin + arcsec
                    self.real_calculation = self.real_calculation.replace(
                        degree_str + "°" + arcmin_str + "°" + arcsec_str + "°",
                        str(conversion),
                    )
                    index += 3
            if self.r.color == self.active:
                for i in range(len(re.findall("sin\(([^\)]*)", self.real_calculation))):
                    self.real_calculation = self.real_calculation.replace(
                        "sin("
                        + re.findall("sin\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            sin(
                                float(
                                    eval(
                                        re.findall(
                                            "sin\(([^\)]*)", self.real_calculation
                                        )[i]
                                    )
                                )
                            )
                        ),
                    )
                for i in range(len(re.findall("cos\(([^\)]*)", self.real_calculation))):
                    self.real_calculation = self.real_calculation.replace(
                        "cos("
                        + re.findall("cos\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            cos(
                                float(
                                    eval(
                                        re.findall(
                                            "cos\(([^\)]*)", self.real_calculation
                                        )[i]
                                    )
                                )
                            )
                        ),
                    )
                for i in range(len(re.findall("tan\(([^\)]*)", self.real_calculation))):
                    self.real_calculation = self.real_calculation.replace(
                        "tan("
                        + re.findall("tan\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            tan(
                                float(
                                    eval(
                                        re.findall(
                                            "tan\(([^\)]*)", self.real_calculation
                                        )[i]
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("sin⁻¹\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "sin⁻¹("
                        + re.findall("sin⁻¹\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            asin(
                                float(
                                    eval(
                                        re.findall(
                                            "sin⁻¹\(([^\)]*)", self.real_calculation
                                        )[i]
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("cos⁻¹\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "cos⁻¹("
                        + re.findall("cos⁻¹\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            acos(
                                float(
                                    eval(
                                        re.findall(
                                            "cos⁻¹\(([^\)]*)", self.real_calculation
                                        )[i]
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("tan⁻¹\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "tan⁻¹("
                        + re.findall("tan⁻¹\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            atan(
                                float(
                                    eval(
                                        re.findall(
                                            "tan⁻¹\(([^\)]*)", self.real_calculation
                                        )[i]
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("sinh\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "sinh("
                        + re.findall("sinh\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            sinh(
                                float(
                                    eval(
                                        re.findall(
                                            "sinh\(([^\)]*)", self.real_calculation
                                        )[i]
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("cosh\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "cosh("
                        + re.findall("cosh\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            cosh(
                                float(
                                    eval(
                                        re.findall(
                                            "cosh\(([^\)]*)", self.real_calculation
                                        )[i]
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("tanh\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "tanh("
                        + re.findall("tanh\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            tanh(
                                float(
                                    eval(
                                        re.findall(
                                            "tanh\(([^\)]*)", self.real_calculation
                                        )[i]
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("sinh⁻¹\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "sinh⁻¹("
                        + re.findall("sinh⁻¹\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            asinh(
                                float(
                                    eval(
                                        re.findall(
                                            "sinh⁻¹\(([^\)]*)", self.real_calculation
                                        )[i]
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("cosh⁻¹\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "cosh⁻¹("
                        + re.findall("cosh⁻¹\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            acosh(
                                float(
                                    eval(
                                        re.findall(
                                            "cosh⁻¹\(([^\)]*)", self.real_calculation
                                        )[i]
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("tanh⁻¹\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "tanh⁻¹("
                        + re.findall("tanh⁻¹\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            atanh(
                                float(
                                    eval(
                                        re.findall(
                                            "tanh⁻¹\(([^\)]*)", self.real_calculation
                                        )[i]
                                    )
                                )
                            )
                        ),
                    )
            elif self.d.color == self.active:
                for i in range(len(re.findall("sin\(([^\)]*)", self.real_calculation))):
                    self.real_calculation = self.real_calculation.replace(
                        "sin("
                        + re.findall("sin\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            sin(
                                radians(
                                    float(
                                        eval(
                                            re.findall(
                                                "sin\(([^\)]*)", self.real_calculation
                                            )[i]
                                        )
                                    )
                                )
                            )
                        ),
                    )
                for i in range(len(re.findall("cos\(([^\)]*)", self.real_calculation))):
                    self.real_calculation = self.real_calculation.replace(
                        "cos("
                        + re.findall("cos\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            cos(
                                radians(
                                    float(
                                        eval(
                                            re.findall(
                                                "cos\(([^\)]*)", self.real_calculation
                                            )[i]
                                        )
                                    )
                                )
                            )
                        ),
                    )
                for i in range(len(re.findall("tan\(([^\)]*)", self.real_calculation))):
                    self.real_calculation = self.real_calculation.replace(
                        "tan("
                        + re.findall("tan\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            tan(
                                radians(
                                    float(
                                        eval(
                                            re.findall(
                                                "tan\(([^\)]*)", self.real_calculation
                                            )[i]
                                        )
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("sin⁻¹\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "sin⁻¹("
                        + re.findall("sin⁻¹\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            degrees(
                                asin(
                                    float(
                                        eval(
                                            re.findall(
                                                "sin⁻¹\(([^\)]*)", self.real_calculation
                                            )[i]
                                        )
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("cos⁻¹\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "cos⁻¹("
                        + re.findall("cos⁻¹\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            degrees(
                                acos(
                                    float(
                                        eval(
                                            re.findall(
                                                "cos⁻¹\(([^\)]*)", self.real_calculation
                                            )[i]
                                        )
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("tan⁻¹\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "tan⁻¹("
                        + re.findall("tan⁻¹\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            degrees(
                                atan(
                                    float(
                                        eval(
                                            re.findall(
                                                "tan⁻¹\(([^\)]*)", self.real_calculation
                                            )[i]
                                        )
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("sinh\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "sinh("
                        + re.findall("sinh\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            sinh(
                                radians(
                                    float(
                                        eval(
                                            re.findall(
                                                "sinh\(([^\)]*)", self.real_calculation
                                            )[i]
                                        )
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("cosh\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "cosh("
                        + re.findall("cosh\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            cosh(
                                radians(
                                    float(
                                        eval(
                                            re.findall(
                                                "cosh\(([^\)]*)", self.real_calculation
                                            )[i]
                                        )
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("tanh\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "tanh("
                        + re.findall("tanh\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            tanh(
                                radians(
                                    float(
                                        eval(
                                            re.findall(
                                                "tanh\(([^\)]*)", self.real_calculation
                                            )[i]
                                        )
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("sinh⁻¹\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "sinh⁻¹("
                        + re.findall("sinh⁻¹\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            degrees(
                                asinh(
                                    float(
                                        eval(
                                            re.findall(
                                                "sinh⁻¹\(([^\)]*)",
                                                self.real_calculation,
                                            )[i]
                                        )
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("cosh⁻¹\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "cosh⁻¹("
                        + re.findall("cosh⁻¹\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            degrees(
                                acosh(
                                    float(
                                        eval(
                                            re.findall(
                                                "cosh⁻¹\(([^\)]*)",
                                                self.real_calculation,
                                            )[i]
                                        )
                                    )
                                )
                            )
                        ),
                    )
                for i in range(
                    len(re.findall("tanh⁻¹\(([^\)]*)", self.real_calculation))
                ):
                    self.real_calculation = self.real_calculation.replace(
                        "tanh⁻¹("
                        + re.findall("tanh⁻¹\(([^\)]*)", self.real_calculation)[i]
                        + ")",
                        str(
                            degrees(
                                atanh(
                                    float(
                                        eval(
                                            re.findall(
                                                "tanh⁻¹\(([^\)]*)",
                                                self.real_calculation,
                                            )[i]
                                        )
                                    )
                                )
                            )
                        ),
                    )
            self.result.value = eval(
                self.real_calculation.replace("Ans", str(self.prev_ans))
            )
            if degree_found == True:
                degree = int(self.result.value)
                arcmin = int((self.result.value - degree) * 60)
                arcsec = round(((self.result.value - degree) * 60 - arcmin) * 60, 2)
                self.result.value = (
                    str(degree) + "°" + str(arcmin) + "’" + str(arcsec) + "”"
                )
            self.result_history.append(self.result.value)
            self.history_track += 1
            self.new_calculation = True

        self.update()


def main(page: Page):
    page.title = "Scientific Calculator"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)


app(target=main)
