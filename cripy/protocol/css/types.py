from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM
from cripy.protocol.page import types as Page

# 
StyleSheetId = str

# Stylesheet type: "injected" for stylesheets injected via extension, "user-agent" for user-agent stylesheets, "inspector" for stylesheets created by the inspector (i.e. those holding the "via inspector" rules), "regular" for regular stylesheets.
StyleSheetOrigin = str


class PseudoElementMatches(ChromeTypeBase):
    """CSS rule collection for a single pseudo style."""
    def __init__(self, pseudoType: 'DOM.PseudoType', matches: List['RuleMatch']) -> None:
        """
        :param DOM.PseudoType pseudoType: Pseudo element type.
        :param array matches: Matches of CSS rules applicable to the pseudo style.
        """
        super().__init__()
        self.pseudoType: DOM.PseudoType = pseudoType
        self.matches: List[RuleMatch] = matches


class InheritedStyleEntry(ChromeTypeBase):
    """Inherited CSS rule collection from ancestor node."""
    def __init__(self, matchedCSSRules: List['RuleMatch'], inlineStyle: Optional['CSSStyle'] = None) -> None:
        """
        :param CSSStyle inlineStyle: The ancestor node's inline style, if any, in the style inheritance chain.
        :param array matchedCSSRules: Matches of CSS rules matching the ancestor node in the style inheritance chain.
        """
        super().__init__()
        self.inlineStyle: Optional[CSSStyle] = inlineStyle
        self.matchedCSSRules: List[RuleMatch] = matchedCSSRules


class RuleMatch(ChromeTypeBase):
    """Match data for a CSS rule."""
    def __init__(self, rule: 'CSSRule', matchingSelectors: List['int']) -> None:
        """
        :param CSSRule rule: CSS rule in the match.
        :param array matchingSelectors: Matching selector indices in the rule's selectorList selectors (0-based).
        """
        super().__init__()
        self.rule: CSSRule = rule
        self.matchingSelectors: List[int] = matchingSelectors


class Value(ChromeTypeBase):
    """Data for a simple selector (these are delimited by commas in a selector list)."""
    def __init__(self, text: str, range: Optional['SourceRange'] = None) -> None:
        """
        :param str text: Value text.
        :param SourceRange range: Value range in the underlying resource (if available).
        """
        super().__init__()
        self.text: str = text
        self.range: Optional[SourceRange] = range


class SelectorList(ChromeTypeBase):
    """Selector list data."""
    def __init__(self, selectors: List['Value'], text: str) -> None:
        """
        :param array selectors: Selectors in the list.
        :param str text: Rule selector text.
        """
        super().__init__()
        self.selectors: List[Value] = selectors
        self.text: str = text


class CSSStyleSheetHeader(ChromeTypeBase):
    """CSS stylesheet metainformation."""
    def __init__(self, styleSheetId: 'StyleSheetId', frameId: 'Page.FrameId', sourceURL: str, origin: 'StyleSheetOrigin', title: str, disabled: bool, isInline: bool, startLine: float, startColumn: float, length: float, sourceMapURL: Optional[str] = None, ownerNode: Optional['DOM.BackendNodeId'] = None, hasSourceURL: Optional[bool] = None) -> None:
        """
        :param StyleSheetId styleSheetId: The stylesheet identifier.
        :param Page.FrameId frameId: Owner frame identifier.
        :param str sourceURL: Stylesheet resource URL.
        :param str sourceMapURL: URL of source map associated with the stylesheet (if any).
        :param StyleSheetOrigin origin: Stylesheet origin.
        :param str title: Stylesheet title.
        :param DOM.BackendNodeId ownerNode: The backend id for the owner node of the stylesheet.
        :param bool disabled: Denotes whether the stylesheet is disabled.
        :param bool hasSourceURL: Whether the sourceURL field value comes from the sourceURL comment.
        :param bool isInline: Whether this stylesheet is created for STYLE tag by parser. This flag is not set for document.written STYLE tags.
        :param float startLine: Line offset of the stylesheet within the resource (zero based).
        :param float startColumn: Column offset of the stylesheet within the resource (zero based).
        :param float length: Size of the content (in characters).
        """
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
    """CSS rule representation."""
    def __init__(self, selectorList: 'SelectorList', origin: 'StyleSheetOrigin', style: 'CSSStyle', styleSheetId: Optional['StyleSheetId'] = None, media: Optional[List['CSSMedia']] = None) -> None:
        """
        :param StyleSheetId styleSheetId: The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        :param SelectorList selectorList: Rule selector data.
        :param StyleSheetOrigin origin: Parent stylesheet's origin.
        :param CSSStyle style: Associated style declaration.
        :param array media: Media list array (for rules involving media queries). The array enumerates media queries starting with the innermost one, going outwards.
        """
        super().__init__()
        self.styleSheetId: Optional[StyleSheetId] = styleSheetId
        self.selectorList: SelectorList = selectorList
        self.origin: StyleSheetOrigin = origin
        self.style: CSSStyle = style
        self.media: Optional[List[CSSMedia]] = media


class RuleUsage(ChromeTypeBase):
    """CSS coverage information."""
    def __init__(self, styleSheetId: 'StyleSheetId', startOffset: float, endOffset: float, used: bool) -> None:
        """
        :param StyleSheetId styleSheetId: The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        :param float startOffset: Offset of the start of the rule (including selector) from the beginning of the stylesheet.
        :param float endOffset: Offset of the end of the rule body from the beginning of the stylesheet.
        :param bool used: Indicates whether the rule was actually used by some element in the page.
        """
        super().__init__()
        self.styleSheetId: StyleSheetId = styleSheetId
        self.startOffset: float = startOffset
        self.endOffset: float = endOffset
        self.used: bool = used


class SourceRange(ChromeTypeBase):
    """Text range within a resource. All numbers are zero-based."""
    def __init__(self, startLine: int, startColumn: int, endLine: int, endColumn: int) -> None:
        """
        :param int startLine: Start line of range.
        :param int startColumn: Start column of range (inclusive).
        :param int endLine: End line of range
        :param int endColumn: End column of range (exclusive).
        """
        super().__init__()
        self.startLine: int = startLine
        self.startColumn: int = startColumn
        self.endLine: int = endLine
        self.endColumn: int = endColumn


class ShorthandEntry(ChromeTypeBase):
    pass
    def __init__(self, name: str, value: str, important: Optional[bool] = None) -> None:
        """
        :param str name: Shorthand name.
        :param str value: Shorthand value.
        :param bool important: Whether the property has "!important" annotation (implies `false` if absent).
        """
        super().__init__()
        self.name: str = name
        self.value: str = value
        self.important: Optional[bool] = important


class CSSComputedStyleProperty(ChromeTypeBase):
    pass
    def __init__(self, name: str, value: str) -> None:
        """
        :param str name: Computed style property name.
        :param str value: Computed style property value.
        """
        super().__init__()
        self.name: str = name
        self.value: str = value


class CSSStyle(ChromeTypeBase):
    """CSS style representation."""
    def __init__(self, cssProperties: List['CSSProperty'], shorthandEntries: List['ShorthandEntry'], styleSheetId: Optional['StyleSheetId'] = None, cssText: Optional[str] = None, range: Optional['SourceRange'] = None) -> None:
        """
        :param StyleSheetId styleSheetId: The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        :param array cssProperties: CSS properties in the style.
        :param array shorthandEntries: Computed values for all shorthands found in the style.
        :param str cssText: Style declaration text (if available).
        :param SourceRange range: Style declaration range in the enclosing stylesheet (if available).
        """
        super().__init__()
        self.styleSheetId: Optional[StyleSheetId] = styleSheetId
        self.cssProperties: List[CSSProperty] = cssProperties
        self.shorthandEntries: List[ShorthandEntry] = shorthandEntries
        self.cssText: Optional[str] = cssText
        self.range: Optional[SourceRange] = range


class CSSProperty(ChromeTypeBase):
    """CSS property declaration data."""
    def __init__(self, name: str, value: str, important: Optional[bool] = None, implicit: Optional[bool] = None, text: Optional[str] = None, parsedOk: Optional[bool] = None, disabled: Optional[bool] = None, range: Optional['SourceRange'] = None) -> None:
        """
        :param str name: The property name.
        :param str value: The property value.
        :param bool important: Whether the property has "!important" annotation (implies `false` if absent).
        :param bool implicit: Whether the property is implicit (implies `false` if absent).
        :param str text: The full property text as specified in the style.
        :param bool parsedOk: Whether the property is understood by the browser (implies `true` if absent).
        :param bool disabled: Whether the property is disabled by the user (present for source-based properties only).
        :param SourceRange range: The entire property range in the enclosing style declaration (if available).
        """
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
    """CSS media rule descriptor."""
    def __init__(self, text: str, source: str, sourceURL: Optional[str] = None, range: Optional['SourceRange'] = None, styleSheetId: Optional['StyleSheetId'] = None, mediaList: Optional[List['MediaQuery']] = None) -> None:
        """
        :param str text: Media query text.
        :param str source: Source of the media query: "mediaRule" if specified by a @media rule, "importRule" if specified by an @import rule, "linkedSheet" if specified by a "media" attribute in a linked stylesheet's LINK tag, "inlineSheet" if specified by a "media" attribute in an inline stylesheet's STYLE tag.
        :param str sourceURL: URL of the document containing the media query description.
        :param SourceRange range: The associated rule (@media or @import) header range in the enclosing stylesheet (if available).
        :param StyleSheetId styleSheetId: Identifier of the stylesheet containing this object (if exists).
        :param array mediaList: Array of media queries.
        """
        super().__init__()
        self.text: str = text
        self.source: str = source
        self.sourceURL: Optional[str] = sourceURL
        self.range: Optional[SourceRange] = range
        self.styleSheetId: Optional[StyleSheetId] = styleSheetId
        self.mediaList: Optional[List[MediaQuery]] = mediaList


class MediaQuery(ChromeTypeBase):
    """Media query descriptor."""
    def __init__(self, expressions: List['MediaQueryExpression'], active: bool) -> None:
        """
        :param array expressions: Array of media query expressions.
        :param bool active: Whether the media query condition is satisfied.
        """
        super().__init__()
        self.expressions: List[MediaQueryExpression] = expressions
        self.active: bool = active


class MediaQueryExpression(ChromeTypeBase):
    """Media query expression descriptor."""
    def __init__(self, value: float, unit: str, feature: str, valueRange: Optional['SourceRange'] = None, computedLength: Optional[float] = None) -> None:
        """
        :param float value: Media query expression value.
        :param str unit: Media query expression units.
        :param str feature: Media query expression feature.
        :param SourceRange valueRange: The associated range of the value text in the enclosing stylesheet (if available).
        :param float computedLength: Computed length of media query expression (if applicable).
        """
        super().__init__()
        self.value: float = value
        self.unit: str = unit
        self.feature: str = feature
        self.valueRange: Optional[SourceRange] = valueRange
        self.computedLength: Optional[float] = computedLength


class PlatformFontUsage(ChromeTypeBase):
    """Information about amount of glyphs that were rendered with given font."""
    def __init__(self, familyName: str, isCustomFont: bool, glyphCount: float) -> None:
        """
        :param str familyName: Font's family name reported by platform.
        :param bool isCustomFont: Indicates if the font was downloaded or resolved locally.
        :param float glyphCount: Amount of glyphs that were rendered with this font.
        """
        super().__init__()
        self.familyName: str = familyName
        self.isCustomFont: bool = isCustomFont
        self.glyphCount: float = glyphCount


class FontFace(ChromeTypeBase):
    """Properties of a web font: https://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#font-descriptions"""
    def __init__(self, fontFamily: str, fontStyle: str, fontVariant: str, fontWeight: str, fontStretch: str, unicodeRange: str, src: str, platformFontFamily: str) -> None:
        """
        :param str fontFamily: The font-family.
        :param str fontStyle: The font-style.
        :param str fontVariant: The font-variant.
        :param str fontWeight: The font-weight.
        :param str fontStretch: The font-stretch.
        :param str unicodeRange: The unicode-range.
        :param str src: The src.
        :param str platformFontFamily: The resolved platform font family
        """
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
    """CSS keyframes rule representation."""
    def __init__(self, animationName: 'Value', keyframes: List['CSSKeyframeRule']) -> None:
        """
        :param Value animationName: Animation name.
        :param array keyframes: List of keyframes.
        """
        super().__init__()
        self.animationName: Value = animationName
        self.keyframes: List[CSSKeyframeRule] = keyframes


class CSSKeyframeRule(ChromeTypeBase):
    """CSS keyframe rule representation."""
    def __init__(self, origin: 'StyleSheetOrigin', keyText: 'Value', style: 'CSSStyle', styleSheetId: Optional['StyleSheetId'] = None) -> None:
        """
        :param StyleSheetId styleSheetId: The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        :param StyleSheetOrigin origin: Parent stylesheet's origin.
        :param Value keyText: Associated key text.
        :param CSSStyle style: Associated style declaration.
        """
        super().__init__()
        self.styleSheetId: Optional[StyleSheetId] = styleSheetId
        self.origin: StyleSheetOrigin = origin
        self.keyText: Value = keyText
        self.style: CSSStyle = style


class StyleDeclarationEdit(ChromeTypeBase):
    """A descriptor of operation to mutate style declaration text."""
    def __init__(self, styleSheetId: 'StyleSheetId', range: 'SourceRange', text: str) -> None:
        """
        :param StyleSheetId styleSheetId: The css style sheet identifier.
        :param SourceRange range: The range of the style text in the enclosing stylesheet.
        :param str text: New style text.
        """
        super().__init__()
        self.styleSheetId: StyleSheetId = styleSheetId
        self.range: SourceRange = range
        self.text: str = text


