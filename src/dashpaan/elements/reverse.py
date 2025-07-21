from src.dashpaan.actions.navigate import Navigate
from src.dashpaan.actions.prompt import Prompt
from src.dashpaan.actions.push import Push
from src.dashpaan.elements.button import Button
from src.dashpaan.elements.card import Card
from src.dashpaan.elements.chart_comparison import ChartComparison
from src.dashpaan.elements.circular_distribution import CircularDistribution
from src.dashpaan.elements.data_table import DataTable
from src.dashpaan.elements.donut_chart import DonutChart
from src.dashpaan.elements.flex import Flex
from src.dashpaan.elements.form import Form
from src.dashpaan.elements.form_element_upload_image import FormElementUploadImage
from src.dashpaan.elements.heading import Heading
from src.dashpaan.elements.information import Information
from src.dashpaan.elements.line_chart import LineChart
from src.dashpaan.elements.navigation import Navigation
from src.dashpaan.elements.page import Page
from src.dashpaan.elements.pie_chart import PieChart
from src.dashpaan.elements.qr_code import QrCode
from src.dashpaan.elements.select import Select
from src.dashpaan.elements.sticky_stat import StickyStat
from src.dashpaan.elements.sticky_target import StickyTarget
from src.dashpaan.elements.switch import Switch
from src.dashpaan.elements.tabular import Tabular
from src.dashpaan.elements.text_area_editor import TextAreaEditor
from src.dashpaan.elements.text_field import TextField
from src.dashpaan.elements.wave_chart import WaveChart
from src.dashpaan.elements.wysiwig_editor import WYSIWYGEditor


def convert(obj):
    if "kind" in obj:
        if obj["kind"] == "heading":
            return Heading.from_json(obj)

        if obj["kind"] == "button":
            return Button.from_json(obj)

        if obj["kind"] == "card":
            return Card.from_json(obj)

        if obj["kind"] == "flex":
            return Flex.from_json(obj)

        if obj["kind"] == "chart-comparison":
            return ChartComparison.from_json(obj)

        if obj["kind"] == "circular-distribution":
            return CircularDistribution.from_json(obj)

        if obj["kind"] == "data-table":
            return DataTable.from_json(obj)

        if obj["kind"] == "wysiwyg-editor":
            return WYSIWYGEditor.from_json(obj)

        if obj["kind"] == "text-area-editor":
            return TextAreaEditor.from_json(obj)

        if obj["kind"] == "page":
            return Page.from_json(obj)

        if obj["kind"] == "text-field":
            return TextField.from_json(obj)

        if obj["kind"] == "sticky-target":
            return StickyTarget.from_json(obj)

        if obj["kind"] == "sticky-stat":
            return StickyStat.from_json(obj)

        if obj["kind"] == "information":
            return Information.from_json(obj)

        if obj["kind"] == "tabular":
            return Tabular.from_json(obj)

        if obj["kind"] == "chart-line":
            return LineChart.from_json(obj)

        if obj["kind"] == "pie_chart":
            return PieChart.from_json(obj)

        if obj["kind"] == "form":
            return Form.from_json(obj)

        if obj["kind"] == "select":
            return Select.from_json(obj)

        if obj["kind"] == "qr-code":
            return QrCode.from_json(obj)

        if obj["kind"] == "donut-chart":
            return DonutChart.from_json(obj)

        if obj["kind"] == "switch":
            return Switch.from_json(obj)

        if obj["kind"] == "formElementUploadImage":
            return FormElementUploadImage.from_json(obj)

        if obj["kind"] == "wave-chart":
            return WaveChart.from_json(obj)

        if obj["kind"] == "navigation":
            return Navigation.from_json(obj)

        if obj["kind"] == "action":
            if obj["type"] == 'push':
                return Push.from_json(obj)

            if obj["type"] == 'prompt':
                return Prompt.from_json(obj)

            if obj["type"] == 'navigate':
                return Navigate.from_json(obj)

    raise ValueError("Not Valid Element")
