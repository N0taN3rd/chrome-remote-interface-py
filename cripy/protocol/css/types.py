from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM
from cripy.protocol.page import types as Page

StyleSheetId = str

StyleSheetOrigin = str


class PseudoElementMatches(ChromeTypeBase):

    def __init__(
        self, pseudoType: "DOM.PseudoType", matches: List["RuleMatch"]
    ) -> None:
        super().__init__()
        self.pseudoType: DOM.PseudoType = pseudoType
        self.matches: List[RuleMatch] = matches


class InheritedStyleEntry(ChromeTypeBase):

    def __init__(
        self,
        matchedCSSRules: List["RuleMatch"],
        inlineStyle: Optional["CSSStyle"] = None,
    ) -> None:
        super().__init__()
        self.inlineStyle: Optional[CSSStyle] = inlineStyle
        self.matchedCSSRules: List[RuleMatch] = matchedCSSRules


class RuleMatch(ChromeTypeBase):

    def __init__(self, rule: "CSSRule", matchingSelectors: List["int"]) -> None:
        super().__init__()
        self.rule: CSSRule = rule
        self.matchingSelectors: List[int] = matchingSelectors


class Value(ChromeTypeBase):

    def __init__(self, text: str, range: Optional["SourceRange"] = None) -> None:
        super().__init__()
        self.text: str = text
        self.range: Optional[SourceRange] = range


class SelectorList(ChromeTypeBase):

    def __init__(self, selectors: List["Value"], text: str) -> None:
        super().__init__()
        self.selectors: List[Value] = selectors
        self.text: str = text


class CSSStyleSheetHeader(ChromeTypeBase):

    def __init__(
        self,
        styleSheetId: "StyleSheetId",
        frameId: "Page.FrameId",
        sourceURL: str,
        origin: "StyleSheetOrigin",
        title: str,
        disabled: bool,
        isInline: bool,
        startLine: float,
        startColumn: float,
        length: float,
        sourceMapURL: Optional[str] = None,
        ownerNode: Optional["DOM.BackendNodeId"] = None,
        hasSourceURL: Optional[bool] = None,
    ) -> None:
        super().__init__()
        self.styleSheetId: StyleSheetId = styleSheetId
        self.frameId: Page.FrameId = frameId
        self.sourceURL: str = sourceURL
        self.sourceMapURL: Optional[str] = sourceMapURL
        self.origin: StyleSheetOrigin = origin
        self.title: str = title
        self.ownerNode: Optional[DOM.BackendNodeId] = ownerNode
        self.disabled: bool = disabled
        self.hasSourceURL: Optional[bool] = hasSourceURL
        self.isInline: bool = isInline
        self.startLine: float = startLine
        self.startColumn: float = startColumn
        self.length: float = length


class CSSRule(ChromeTypeBase):

    def __init__(
        self,
        selectorList: "SelectorList",
        origin: "StyleSheetOrigin",
        style: "CSSStyle",
        styleSheetId: Optional["StyleSheetId"] = None,
        media: Optional[List["CSSMedia"]] = None,
    ) -> None:
        super().__init__()
        self.styleSheetId: Optional[StyleSheetId] = styleSheetId
        self.selectorList: SelectorList = selectorList
        self.origin: StyleSheetOrigin = origin
        self.style: CSSStyle = style
        self.media: Optional[List[CSSMedia]] = media


class RuleUsage(ChromeTypeBase):

    def __init__(
        self,
        styleSheetId: "StyleSheetId",
        startOffset: float,
        endOffset: float,
        used: bool,
    ) -> None:
        super().__init__()
        self.styleSheetId: StyleSheetId = styleSheetId
        self.startOffset: float = startOffset
        self.endOffset: float = endOffset
        self.used: bool = used


class SourceRange(ChromeTypeBase):

    def __init__(
        self, startLine: int, startColumn: int, endLine: int, endColumn: int
    ) -> None:
        super().__init__()
        self.startLine: int = startLine
        self.startColumn: int = startColumn
        self.endLine: int = endLine
        self.endColumn: int = endColumn


class ShorthandEntry(ChromeTypeBase):

    def __init__(self, name: str, value: str, important: Optional[bool] = None) -> None:
        super().__init__()
        self.name: str = name
        self.value: str = value
        self.important: Optional[bool] = important


class CSSComputedStyleProperty(ChromeTypeBase):

    def __init__(self, name: str, value: str) -> None:
        super().__init__()
        self.name: str = name
        self.value: str = value


class CSSStyle(ChromeTypeBase):

    def __init__(
        self,
        cssProperties: List["CSSProperty"],
        shorthandEntries: List["ShorthandEntry"],
        styleSheetId: Optional["StyleSheetId"] = None,
        cssText: Optional[str] = None,
        range: Optional["SourceRange"] = None,
    ) -> None:
        super().__init__()
        self.styleSheetId: Optional[StyleSheetId] = styleSheetId
        self.cssProperties: List[CSSProperty] = cssProperties
        self.shorthandEntries: List[ShorthandEntry] = shorthandEntries
        self.cssText: Optional[str] = cssText
        self.range: Optional[SourceRange] = range


class CSSProperty(ChromeTypeBase):

    def __init__(
        self,
        name: str,
        value: str,
        important: Optional[bool] = None,
        implicit: Optional[bool] = None,
        text: Optional[str] = None,
        parsedOk: Optional[bool] = None,
        disabled: Optional[bool] = None,
        range: Optional["SourceRange"] = None,
    ) -> None:
        super().__init__()
        self.name: str = name
        self.value: str = value
        self.important: Optional[bool] = important
        self.implicit: Optional[bool] = implicit
        self.text: Optional[str] = text
        self.parsedOk: Optional[bool] = parsedOk
        self.disabled: Optional[bool] = disabled
        self.range: Optional[SourceRange] = range


class CSSMedia(ChromeTypeBase):

    def __init__(
        self,
        text: str,
        source: str,
        sourceURL: Optional[str] = None,
        range: Optional["SourceRange"] = None,
        styleSheetId: Optional["StyleSheetId"] = None,
        mediaList: Optional[List["MediaQuery"]] = None,
    ) -> None:
        super().__init__()
        self.text: str = text
        self.source: str = source
        self.sourceURL: Optional[str] = sourceURL
        self.range: Optional[SourceRange] = range
        self.styleSheetId: Optional[StyleSheetId] = styleSheetId
        self.mediaList: Optional[List[MediaQuery]] = mediaList


class MediaQuery(ChromeTypeBase):

    def __init__(self, expressions: List["MediaQueryExpression"], active: bool) -> None:
        super().__init__()
        self.expressions: List[MediaQueryExpression] = expressions
        self.active: bool = active


class MediaQueryExpression(ChromeTypeBase):

    def __init__(
        self,
        value: float,
        unit: str,
        feature: str,
        valueRange: Optional["SourceRange"] = None,
        computedLength: Optional[float] = None,
    ) -> None:
        super().__init__()
        self.value: float = value
        self.unit: str = unit
        self.feature: str = feature
        self.valueRange: Optional[SourceRange] = valueRange
        self.computedLength: Optional[float] = computedLength


class PlatformFontUsage(ChromeTypeBase):

    def __init__(self, familyName: str, isCustomFont: bool, glyphCount: float) -> None:
        super().__init__()
        self.familyName: str = familyName
        self.isCustomFont: bool = isCustomFont
        self.glyphCount: float = glyphCount


class FontFace(ChromeTypeBase):

    def __init__(
        self,
        fontFamily: str,
        fontStyle: str,
        fontVariant: str,
        fontWeight: str,
        fontStretch: str,
        unicodeRange: str,
        src: str,
        platformFontFamily: str,
    ) -> None:
        super().__init__()
        self.fontFamily: str = fontFamily
        self.fontStyle: str = fontStyle
        self.fontVariant: str = fontVariant
        self.fontWeight: str = fontWeight
        self.fontStretch: str = fontStretch
        self.unicodeRange: str = unicodeRange
        self.src: str = src
        self.platformFontFamily: str = platformFontFamily


class CSSKeyframesRule(ChromeTypeBase):

    def __init__(
        self, animationName: "Value", keyframes: List["CSSKeyframeRule"]
    ) -> None:
        super().__init__()
        self.animationName: Value = animationName
        self.keyframes: List[CSSKeyframeRule] = keyframes


class CSSKeyframeRule(ChromeTypeBase):

    def __init__(
        self,
        origin: "StyleSheetOrigin",
        keyText: "Value",
        style: "CSSStyle",
        styleSheetId: Optional["StyleSheetId"] = None,
    ) -> None:
        super().__init__()
        self.styleSheetId: Optional[StyleSheetId] = styleSheetId
        self.origin: StyleSheetOrigin = origin
        self.keyText: Value = keyText
        self.style: CSSStyle = style


class StyleDeclarationEdit(ChromeTypeBase):

    def __init__(
        self, styleSheetId: "StyleSheetId", range: "SourceRange", text: str
    ) -> None:
        super().__init__()
        self.styleSheetId: StyleSheetId = styleSheetId
        self.range: SourceRange = range
        self.text: str = text
