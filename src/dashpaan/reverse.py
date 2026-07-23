# top-level classes
from .page import Page
from .navigation import Navigation
from .authentication import Authentication

# elements
from .elements.heading import Heading
from .elements.block import Block
from .elements.button import Button
from .elements.data_table import DataTable
from .elements.form import Form
from .elements.form_element_upload_image import FormElementUploadImage
from .elements.text_field import TextField
from .elements.wave_chart import WaveChart
from .elements.circular_distribution import CircularDistribution
from .elements.chart_comparison import ChartComparison
from .elements.switch import Switch
from .elements.flex import Flex
from .elements.information import Information
from .elements.card import Card
from .elements.record import Record
from .elements.cta import CTA
from .elements.select import Select
from .elements.donut_chart import DonutChart
from .elements.line_chart import LineChart
from .elements.sticky_stat import StickyStat
from .elements.sticky_target import StickyTarget
from .elements.tabular import Tabular
from .elements.text_area_editor import TextAreaEditor
from .elements.wysiwig_editor import WYSIWYGEditor
from .elements.qr_code import QrCode
from .elements.pie_chart import PieChart

# actions
from .actions.prompt import Prompt
from .actions.navigate import Navigate
from .actions.push import Push
from .actions.external import External
from .actions.reaction import Reaction


def convert(obj):
    if "kind" not in obj:
        raise ValueError("Not Valid Element")

    if "Top-Level classes":
        if obj["kind"] == "page":
            return Page.from_json(obj)

        if obj["kind"] == "navigation":
            return Navigation.from_json(obj)

        if obj["kind"] == "authentication":
            return Authentication.from_json(obj)

    if "Elements":
        if obj["kind"] == "heading":
            return Heading.from_json(obj)

        if obj["kind"] == "button":
            return Button.from_json(obj)

        if obj["kind"] == "cta":
            return CTA.from_json(obj)

        if obj["kind"] == "card":
            return Card.from_json(obj)

        if obj["kind"] == "record":
            return Record.from_json(obj)

        if obj["kind"] == "flex":
            return Flex.from_json(obj)

        if obj["kind"] == "block":
            return Block.from_json(obj)

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

        if obj["kind"] == "pie-chart":
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

    if "Actions":
        if obj["kind"] == "reaction":
            return Reaction.from_json(obj)

        if obj["kind"] == "action":
            if obj["type"] == 'push':
                return Push.from_json(obj)

            if obj["type"] == 'prompt':
                return Prompt.from_json(obj)

            if obj["type"] == 'navigate':
                return Navigate.from_json(obj)

            if obj["type"] == 'external':
                return External.from_json(obj)

    raise ValueError("Not Valid Element")
