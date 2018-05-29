from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.dom import types as DOM
from cripy.protocol.page import types as Page

StyleSheetOrigin = TypeVar("StyleSheetOrigin", str, str)
"""Stylesheet type: "injected" for stylesheets injected via extension, "user-agent" for user-agent stylesheets, "inspector" for stylesheets created by the inspector (i.e. those holding the "via inspector" rules), "regular" for regular stylesheets."""

StyleSheetId = TypeVar("StyleSheetId", str, str)
""""""


class Value(ProtocolType):
    """Data for a simple selector (these are delimited by commas in a selector list)."""

    def __init__(self, text: str, range: Optional["SourceRange"] = None) -> None:
        """
        :param text: Value text.
        :type text: str
        :param range: Value range in the underlying resource (if available).
        :type range: SourceRange
        """
        super().__init__()
        self.text: str = text
        self.range: Optional[SourceRange] = range


class StyleDeclarationEdit(ProtocolType):
    """A descriptor of operation to mutate style declaration text."""

    def __init__(
        self, styleSheetId: "StyleSheetId", range: "SourceRange", text: str
    ) -> None:
        """
        :param styleSheetId: The css style sheet identifier.
        :type styleSheetId: StyleSheetId
        :param range: The range of the style text in the enclosing stylesheet.
        :type range: SourceRange
        :param text: New style text.
        :type text: str
        """
        super().__init__()
        self.styleSheetId: StyleSheetId = styleSheetId
        self.range: SourceRange = range
        self.text: str = text


class SourceRange(ProtocolType):
    """Text range within a resource. All numbers are zero-based."""

    def __init__(
        self, startLine: int, startColumn: int, endLine: int, endColumn: int
    ) -> None:
        """
        :param startLine: Start line of range.
        :type startLine: int
        :param startColumn: Start column of range (inclusive).
        :type startColumn: int
        :param endLine: End line of range
        :type endLine: int
        :param endColumn: End column of range (exclusive).
        :type endColumn: int
        """
        super().__init__()
        self.startLine: int = startLine
        self.startColumn: int = startColumn
        self.endLine: int = endLine
        self.endColumn: int = endColumn


class ShorthandEntry(ProtocolType):

    def __init__(self, name: str, value: str, important: Optional[bool] = None) -> None:
        """
        :param name: Shorthand name.
        :type name: str
        :param value: Shorthand value.
        :type value: str
        :param important: Whether the property has "!important" annotation (implies `false` if absent).
        :type important: bool
        """
        super().__init__()
        self.name: str = name
        self.value: str = value
        self.important: Optional[bool] = important


class SelectorList(ProtocolType):
    """Selector list data."""

    def __init__(self, selectors: List[Union["Value", dict]], text: str) -> None:
        """
        :param selectors: Selectors in the list.
        :type selectors: array
        :param text: Rule selector text.
        :type text: str
        """
        super().__init__()
        self.selectors: List[Value] = selectors
        self.text: str = text


class RuleUsage(ProtocolType):
    """CSS coverage information."""

    def __init__(
        self,
        styleSheetId: "StyleSheetId",
        startOffset: float,
        endOffset: float,
        used: bool,
    ) -> None:
        """
        :param styleSheetId: The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        :type styleSheetId: StyleSheetId
        :param startOffset: Offset of the start of the rule (including selector) from the beginning of the stylesheet.
        :type startOffset: float
        :param endOffset: Offset of the end of the rule body from the beginning of the stylesheet.
        :type endOffset: float
        :param used: Indicates whether the rule was actually used by some element in the page.
        :type used: bool
        """
        super().__init__()
        self.styleSheetId: StyleSheetId = styleSheetId
        self.startOffset: float = startOffset
        self.endOffset: float = endOffset
        self.used: bool = used


class RuleMatch(ProtocolType):
    """Match data for a CSS rule."""

    def __init__(self, rule: "CSSRule", matchingSelectors: List[int]) -> None:
        """
        :param rule: CSS rule in the match.
        :type rule: CSSRule
        :param matchingSelectors: Matching selector indices in the rule's selectorList selectors (0-based).
        :type matchingSelectors: array
        """
        super().__init__()
        self.rule: CSSRule = rule
        self.matchingSelectors: List[int] = matchingSelectors


class PseudoElementMatches(ProtocolType):
    """CSS rule collection for a single pseudo style."""

    def __init__(
        self, pseudoType: "DOM.PseudoType", matches: List[Union["RuleMatch", dict]]
    ) -> None:
        """
        :param pseudoType: Pseudo element type.
        :type pseudoType: DOM.PseudoType
        :param matches: Matches of CSS rules applicable to the pseudo style.
        :type matches: array
        """
        super().__init__()
        self.pseudoType: DOM.PseudoType = pseudoType
        self.matches: List[RuleMatch] = matches


class PlatformFontUsage(ProtocolType):
    """Information about amount of glyphs that were rendered with given font."""

    def __init__(self, familyName: str, isCustomFont: bool, glyphCount: float) -> None:
        """
        :param familyName: Font's family name reported by platform.
        :type familyName: str
        :param isCustomFont: Indicates if the font was downloaded or resolved locally.
        :type isCustomFont: bool
        :param glyphCount: Amount of glyphs that were rendered with this font.
        :type glyphCount: float
        """
        super().__init__()
        self.familyName: str = familyName
        self.isCustomFont: bool = isCustomFont
        self.glyphCount: float = glyphCount


class MediaQueryExpression(ProtocolType):
    """Media query expression descriptor."""

    def __init__(
        self,
        value: float,
        unit: str,
        feature: str,
        valueRange: Optional["SourceRange"] = None,
        computedLength: Optional[float] = None,
    ) -> None:
        """
        :param value: Media query expression value.
        :type value: float
        :param unit: Media query expression units.
        :type unit: str
        :param feature: Media query expression feature.
        :type feature: str
        :param valueRange: The associated range of the value text in the enclosing stylesheet (if available).
        :type valueRange: SourceRange
        :param computedLength: Computed length of media query expression (if applicable).
        :type computedLength: float
        """
        super().__init__()
        self.value: float = value
        self.unit: str = unit
        self.feature: str = feature
        self.valueRange: Optional[SourceRange] = valueRange
        self.computedLength: Optional[float] = computedLength


class MediaQuery(ProtocolType):
    """Media query descriptor."""

    def __init__(
        self, expressions: List[Union["MediaQueryExpression", dict]], active: bool
    ) -> None:
        """
        :param expressions: Array of media query expressions.
        :type expressions: array
        :param active: Whether the media query condition is satisfied.
        :type active: bool
        """
        super().__init__()
        self.expressions: List[MediaQueryExpression] = expressions
        self.active: bool = active


class InheritedStyleEntry(ProtocolType):
    """Inherited CSS rule collection from ancestor node."""

    def __init__(
        self,
        matchedCSSRules: List[Union["RuleMatch", dict]],
        inlineStyle: Optional["CSSStyle"] = None,
    ) -> None:
        """
        :param inlineStyle: The ancestor node's inline style, if any, in the style inheritance chain.
        :type inlineStyle: CSSStyle
        :param matchedCSSRules: Matches of CSS rules matching the ancestor node in the style inheritance chain.
        :type matchedCSSRules: array
        """
        super().__init__()
        self.inlineStyle: Optional[CSSStyle] = inlineStyle
        self.matchedCSSRules: List[RuleMatch] = matchedCSSRules


class FontFace(ProtocolType):
    """Properties of a web font: https://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#font-descriptions"""

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
        """
        :param fontFamily: The font-family.
        :type fontFamily: str
        :param fontStyle: The font-style.
        :type fontStyle: str
        :param fontVariant: The font-variant.
        :type fontVariant: str
        :param fontWeight: The font-weight.
        :type fontWeight: str
        :param fontStretch: The font-stretch.
        :type fontStretch: str
        :param unicodeRange: The unicode-range.
        :type unicodeRange: str
        :param src: The src.
        :type src: str
        :param platformFontFamily: The resolved platform font family
        :type platformFontFamily: str
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


class CSSStyleSheetHeader(ProtocolType):
    """CSS stylesheet metainformation."""

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
        """
        :param styleSheetId: The stylesheet identifier.
        :type styleSheetId: StyleSheetId
        :param frameId: Owner frame identifier.
        :type frameId: Page.FrameId
        :param sourceURL: Stylesheet resource URL.
        :type sourceURL: str
        :param sourceMapURL: URL of source map associated with the stylesheet (if any).
        :type sourceMapURL: str
        :param origin: Stylesheet origin.
        :type origin: StyleSheetOrigin
        :param title: Stylesheet title.
        :type title: str
        :param ownerNode: The backend id for the owner node of the stylesheet.
        :type ownerNode: DOM.BackendNodeId
        :param disabled: Denotes whether the stylesheet is disabled.
        :type disabled: bool
        :param hasSourceURL: Whether the sourceURL field value comes from the sourceURL comment.
        :type hasSourceURL: bool
        :param isInline: Whether this stylesheet is created for STYLE tag by parser. This flag is not set for document.written STYLE tags.
        :type isInline: bool
        :param startLine: Line offset of the stylesheet within the resource (zero based).
        :type startLine: float
        :param startColumn: Column offset of the stylesheet within the resource (zero based).
        :type startColumn: float
        :param length: Size of the content (in characters).
        :type length: float
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


class CSSStyle(ProtocolType):
    """CSS style representation."""

    def __init__(
        self,
        cssProperties: List[Union["CSSProperty", dict]],
        shorthandEntries: List[Union["ShorthandEntry", dict]],
        styleSheetId: Optional["StyleSheetId"] = None,
        cssText: Optional[str] = None,
        range: Optional["SourceRange"] = None,
    ) -> None:
        """
        :param styleSheetId: The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        :type styleSheetId: StyleSheetId
        :param cssProperties: CSS properties in the style.
        :type cssProperties: array
        :param shorthandEntries: Computed values for all shorthands found in the style.
        :type shorthandEntries: array
        :param cssText: Style declaration text (if available).
        :type cssText: str
        :param range: Style declaration range in the enclosing stylesheet (if available).
        :type range: SourceRange
        """
        super().__init__()
        self.styleSheetId: Optional[StyleSheetId] = styleSheetId
        self.cssProperties: List[CSSProperty] = cssProperties
        self.shorthandEntries: List[ShorthandEntry] = shorthandEntries
        self.cssText: Optional[str] = cssText
        self.range: Optional[SourceRange] = range


class CSSRule(ProtocolType):
    """CSS rule representation."""

    def __init__(
        self,
        selectorList: "SelectorList",
        origin: "StyleSheetOrigin",
        style: "CSSStyle",
        styleSheetId: Optional["StyleSheetId"] = None,
        media: Optional[List[Union["CSSMedia", dict]]] = None,
    ) -> None:
        """
        :param styleSheetId: The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        :type styleSheetId: StyleSheetId
        :param selectorList: Rule selector data.
        :type selectorList: SelectorList
        :param origin: Parent stylesheet's origin.
        :type origin: StyleSheetOrigin
        :param style: Associated style declaration.
        :type style: CSSStyle
        :param media: Media list array (for rules involving media queries). The array enumerates media queries starting with the innermost one, going outwards.
        :type media: array
        """
        super().__init__()
        self.styleSheetId: Optional[StyleSheetId] = styleSheetId
        self.selectorList: SelectorList = selectorList
        self.origin: StyleSheetOrigin = origin
        self.style: CSSStyle = style
        self.media: Optional[List[CSSMedia]] = media


class CSSProperty(ProtocolType):
    """CSS property declaration data."""

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
        """
        :param name: The property name.
        :type name: str
        :param value: The property value.
        :type value: str
        :param important: Whether the property has "!important" annotation (implies `false` if absent).
        :type important: bool
        :param implicit: Whether the property is implicit (implies `false` if absent).
        :type implicit: bool
        :param text: The full property text as specified in the style.
        :type text: str
        :param parsedOk: Whether the property is understood by the browser (implies `true` if absent).
        :type parsedOk: bool
        :param disabled: Whether the property is disabled by the user (present for source-based properties only).
        :type disabled: bool
        :param range: The entire property range in the enclosing style declaration (if available).
        :type range: SourceRange
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


class CSSMedia(ProtocolType):
    """CSS media rule descriptor."""

    def __init__(
        self,
        text: str,
        source: str,
        sourceURL: Optional[str] = None,
        range: Optional["SourceRange"] = None,
        styleSheetId: Optional["StyleSheetId"] = None,
        mediaList: Optional[List[Union["MediaQuery", dict]]] = None,
    ) -> None:
        """
        :param text: Media query text.
        :type text: str
        :param source: Source of the media query: "mediaRule" if specified by a @media rule, "importRule" if specified by an @import rule, "linkedSheet" if specified by a "media" attribute in a linked stylesheet's LINK tag, "inlineSheet" if specified by a "media" attribute in an inline stylesheet's STYLE tag.
        :type source: str
        :param sourceURL: URL of the document containing the media query description.
        :type sourceURL: str
        :param range: The associated rule (@media or @import) header range in the enclosing stylesheet (if available).
        :type range: SourceRange
        :param styleSheetId: Identifier of the stylesheet containing this object (if exists).
        :type styleSheetId: StyleSheetId
        :param mediaList: Array of media queries.
        :type mediaList: array
        """
        super().__init__()
        self.text: str = text
        self.source: str = source
        self.sourceURL: Optional[str] = sourceURL
        self.range: Optional[SourceRange] = range
        self.styleSheetId: Optional[StyleSheetId] = styleSheetId
        self.mediaList: Optional[List[MediaQuery]] = mediaList


class CSSKeyframesRule(ProtocolType):
    """CSS keyframes rule representation."""

    def __init__(
        self, animationName: "Value", keyframes: List[Union["CSSKeyframeRule", dict]]
    ) -> None:
        """
        :param animationName: Animation name.
        :type animationName: Value
        :param keyframes: List of keyframes.
        :type keyframes: array
        """
        super().__init__()
        self.animationName: Value = animationName
        self.keyframes: List[CSSKeyframeRule] = keyframes


class CSSKeyframeRule(ProtocolType):
    """CSS keyframe rule representation."""

    def __init__(
        self,
        origin: "StyleSheetOrigin",
        keyText: "Value",
        style: "CSSStyle",
        styleSheetId: Optional["StyleSheetId"] = None,
    ) -> None:
        """
        :param styleSheetId: The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        :type styleSheetId: StyleSheetId
        :param origin: Parent stylesheet's origin.
        :type origin: StyleSheetOrigin
        :param keyText: Associated key text.
        :type keyText: Value
        :param style: Associated style declaration.
        :type style: CSSStyle
        """
        super().__init__()
        self.styleSheetId: Optional[StyleSheetId] = styleSheetId
        self.origin: StyleSheetOrigin = origin
        self.keyText: Value = keyText
        self.style: CSSStyle = style


class CSSComputedStyleProperty(ProtocolType):

    def __init__(self, name: str, value: str) -> None:
        """
        :param name: Computed style property name.
        :type name: str
        :param value: Computed style property value.
        :type value: str
        """
        super().__init__()
        self.name: str = name
        self.value: str = value


OBJECT_LIST = {
    "Value": Value,
    "StyleDeclarationEdit": StyleDeclarationEdit,
    "SourceRange": SourceRange,
    "ShorthandEntry": ShorthandEntry,
    "SelectorList": SelectorList,
    "RuleUsage": RuleUsage,
    "RuleMatch": RuleMatch,
    "PseudoElementMatches": PseudoElementMatches,
    "PlatformFontUsage": PlatformFontUsage,
    "MediaQueryExpression": MediaQueryExpression,
    "MediaQuery": MediaQuery,
    "InheritedStyleEntry": InheritedStyleEntry,
    "FontFace": FontFace,
    "CSSStyleSheetHeader": CSSStyleSheetHeader,
    "CSSStyle": CSSStyle,
    "CSSRule": CSSRule,
    "CSSProperty": CSSProperty,
    "CSSMedia": CSSMedia,
    "CSSKeyframesRule": CSSKeyframesRule,
    "CSSKeyframeRule": CSSKeyframeRule,
    "CSSComputedStyleProperty": CSSComputedStyleProperty,
}
