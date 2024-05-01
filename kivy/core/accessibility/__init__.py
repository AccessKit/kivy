'''
Accessibility
=============

'''

__all__ = ('AccessibilityBase', 'AccessibilityEventType', 'AccessibilityEvent',
           'AccessibilityInterfaceBase')


from kivy.core.window import WindowBase
from kivy.uix.widget import Widget
from enum import Enum, auto


class AccessibilityEventType(Enum):
    NEW = auto()
    DESTROYED = auto()


class AccessibilityInterfaceBase:

    def __init__(self, widget: Widget):
        self.widget = widget


class AccessibilityEvent:

    def __init__(self, event_type: AccessibilityEventType,
                 interface: AccessibilityInterfaceBase):
        self.event_type = event_type
        self.interface = interface


class AccessibilityBase:

    def install(self, window: WindowBase):
        '''Called only once when `kivy.core.Window` is ready but not yet shown,
        so the accessibility provider can attach flawlessly.'''
        pass

    def update(self, event: AccessibilityEvent):
        '''Called every time a widget (or another entity) needs to let know the
        accessibility provider that something has changed, created or deleted.
        '''
        pass
