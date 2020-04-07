import requests, json
import urllib.parse
from typing import Dict, Union, Optional

from ._setting import BASE_URL

class BoardContents():

    def __init__(self, access_token: str, board_id: str=""):
        self.access_token = access_token
        self.board_id = board_id

    def reset_access_token(access_token: str) -> self:
        self.access_token = access_token
        return self
    
    def create_sticker(
        self, 
        x: Optional(int)=None, 
        y: Optional(int)=None,
        scale: Optional(float)=None,
        height: Optional(float)=None,
        width: Optional(float)=None,
        background_color: Optional(str)=None,
        font_family: Optional(str)=None,
        font_size: Optional(int)=None,
        text_align: Optional(str)=None,
        text_align_vertical: Optional(str)=None,
        text: Optional(str)=None
    ) -> Dict[str, Union[str, int, float]]:
        widget_params = {
            "type": "sticker",
            "x": x,
            "y": y,
            "scale": scale,
            "height": height,
            "width": width,
            "style": {
                "backgroundColor": background_color,
                "fontFamily": font_family,
                "fontSize": font_size,
                "textAlign": text_align,
                "textAlignVertical": text_align_vertical
            },
            "text": text
        }
        widget_params = {k: v for k, v in widget_params.items() if v is not None}

        return self.create_widget(
            board_id=self.board_id,
            access_token = self.access_token,
            widget_params = widget_params
        )
    
    def create_shape(
        self,
        x: Optional(int)=None, 
        y: Optional(int)=None,
        rotation: Optional(float)=None,
        width: Optional(float)=None,
        height: Optional(float)=None,
        background_color: Optional(str)=None,
        background_opacity: Optional(float)=None,
        border_color: Optional(str)=None,
        border_opacity: Optional(float)=None,
        border_style: Optional(str)=None,
        border_width: Optional(float)=None,
        font_family: Optional(str)=None,
        font_size: Optional(int)=None,
        shape_type: Optional(str)=None,
        text_align: Optional(str)=None,
        text_align_vertical: Optional(str)=None,
        text: Optional(str)=None
    ):
        widget_params = {
            "type": "shape",
            "x": x,
            "y": y,
            "rotation": rotation,
            "width": width,
            "height": height,
            "style": {
                "backgroundColor": background_color,
                "backgroundOpacity": background_opacity,
                "borderColor": border_color,
                "borderOpacity": border_opacity,
                "borderStyle": border_style,
                "borderWidth": border_width,
                "fontFamily": font_family,
                "fontSize": font_size,
                "shapeType": shape_type,
                "textAlign": text_align,
                "textAlignVertical": text_align_vertical
            },
            "text": text
        }
        widget_params = {k: v for k, v in widget_params.items() if v is not None}
        return self.create_widget(
            board_id=self.board_id,
            access_token = self.access_token,
            widget_params = widget_params
        )
    
    def create_text(
        self, 
        x: Optional(int)=None, 
        y: Optional(int)=None,
        width: Optional(float)=None,
        rotation: Optional(float)=None,
        scale: Optional(float)=None,
        background_color: Optional(str)=None,
        background_opacity: Optional(float)=None,
        border_color: Optional(str)=None,
        border_opacity: Optional(float)=None,
        border_style: Optional(str)=None,
        border_width: Optional(float)=None,
        font_family: Optional(str)=None,
        font_size: Optional(int)=None,
        text_align: Optional(str)=None,
        text_align_vertical: Optional(str)=None,
        text: Optional(str)=None
    ):
        widget_params = {
            "type": "text",
            "x": x,
            "y": y,
            "width": width,
            "rotation": rotation,
            "scale": scale,
            "style": {
                "backgroundColor": background_color,
                "backgroundOpacity": background_opacity,
                "borderColor": border_color,
                "borderOpacity": border_opacity,
                "borderStyle": border_style,
                "borderWidth": border_width,
                "fontFamily": font_family,
                "fontSize": font_size,
                "textAlign": text_align,
                "textAlignVertical": text_align_vertical
            },
            "text": text
        }
        widget_params = {k: v for k, v in widget_params.items() if v is not None}
        return self.create_widget(
            board_id=self.board_id,
            access_token = self.access_token,
            widget_params = widget_params
        )

    @staticmethod
    def create_widget(
        board_id: str, access_token: str, widget_params: Dict[str, Union[str, int, float]]
    ) -> Dict[str, Union[str, int, float]]:
        """
        args:
            params: 
        return:
            wedget_id: 
        """
        url = urllib.parse.urljoin(BASE_URL, f"{board_id}/widgets")
        headers = {
            'authorization': access_token,
            'Content-Type': 'application/json'
        }
        res = requests.post(url, json.dumps(widget_params), headers=headers)
        if res.status_code == 201:
            return res.json()