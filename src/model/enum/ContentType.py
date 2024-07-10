from enum import Enum


class ContentInputType(Enum):

    UPLOAD = 'upload'
    TEXT = 'text'

    @staticmethod
    def is_editable(value: Enum) -> bool:
        if value == ContentInputType.UPLOAD:
            return False
        elif value == ContentInputType.TEXT:
            return True


class ContentType(Enum):

    URL = 'url'
    YOUTUBE = 'youtube'
    PICTURE = 'picture'
    VIDEO = 'video'

    @staticmethod
    def get_input(value: Enum) -> ContentInputType:
        if value == ContentType.PICTURE:
            return ContentInputType.UPLOAD
        elif value == ContentType.VIDEO:
            return ContentInputType.UPLOAD
        elif value == ContentType.YOUTUBE:
            return ContentInputType.TEXT
        elif value == ContentType.URL:
            return ContentInputType.TEXT

    @staticmethod
    def get_fa_icon(value: Enum) -> ContentInputType:
        if value == ContentType.PICTURE:
            return 'fa-regular fa-image'
        elif value == ContentType.VIDEO:
            return 'fa-video-camera'
        elif value == ContentType.YOUTUBE:
            return 'fa-brands fa-youtube'
        elif value == ContentType.URL:
            return 'fa-link'

        return 'fa-file'
