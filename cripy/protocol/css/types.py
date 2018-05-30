from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.dom import types as DOM
from cripy.protocol.page import types as Page

StyleSheetOrigin = TypeVar("StyleSheetOrigin", str, str) # Stylesheet type: "injected" for stylesheets injected via extension, "user-agent" for user-agent stylesheets, "inspector" for stylesheets created by the inspector (i.e. those holding the "via inspector" rules), "regular" for regular stylesheets.

StyleSheetId = TypeVar("StyleSheetId", str, str) # 


class Value(ProtocolType):
    """
    Data for a simple selector (these are delimited by commas in a selector list).
    """

    def __init__(self, text: str, range: Optional[Union['SourceRange', dict]] = None) -> None:
        """
        :param text: Value text.
        :type text: str
        :param range: Value range in the underlying resource (if available).
        :type range: Optional[dict]
        """
        super().__init__()
        self.text = text
        self.range = SourceRange.safe_create(range)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Value']:
        if init is not None:
            return Value(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Value']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Value(**it))
            return list_of_self
        else:
            return init


class StyleDeclarationEdit(ProtocolType):
    """
    A descriptor of operation to mutate style declaration text.
    """

    def __init__(self, styleSheetId: StyleSheetId, range: Union['SourceRange', dict], text: str) -> None:
        """
        :param styleSheetId: The css style sheet identifier.
        :type styleSheetId: str
        :param range: The range of the style text in the enclosing stylesheet.
        :type range: dict
        :param text: New style text.
        :type text: str
        """
        super().__init__()
        self.styleSheetId = styleSheetId
        self.range = SourceRange.safe_create(range)
        self.text = text

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['StyleDeclarationEdit']:
        if init is not None:
            return StyleDeclarationEdit(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['StyleDeclarationEdit']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StyleDeclarationEdit(**it))
            return list_of_self
        else:
            return init


class SourceRange(ProtocolType):
    """
    Text range within a resource. All numbers are zero-based.
    """

    def __init__(self, startLine: int, startColumn: int, endLine: int, endColumn: int) -> None:
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
        self.startLine = startLine
        self.startColumn = startColumn
        self.endLine = endLine
        self.endColumn = endColumn

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['SourceRange']:
        if init is not None:
            return SourceRange(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['SourceRange']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SourceRange(**it))
            return list_of_self
        else:
            return init


class ShorthandEntry(ProtocolType):
    def __init__(self, name: str, value: str, important: Optional[bool] = None) -> None:
        """
        :param name: Shorthand name.
        :type name: str
        :param value: Shorthand value.
        :type value: str
        :param important: Whether the property has "!important" annotation (implies `false` if absent).
        :type important: Optional[bool]
        """
        super().__init__()
        self.name = name
        self.value = value
        self.important = important

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ShorthandEntry']:
        if init is not None:
            return ShorthandEntry(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ShorthandEntry']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ShorthandEntry(**it))
            return list_of_self
        else:
            return init


class SelectorList(ProtocolType):
    """
    Selector list data.
    """

    def __init__(self, selectors: List[Union['Value', dict]], text: str) -> None:
        """
        :param selectors: Selectors in the list.
        :type selectors: List[dict]
        :param text: Rule selector text.
        :type text: str
        """
        super().__init__()
        self.selectors = Value.safe_create_from_list(selectors)
        self.text = text

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['SelectorList']:
        if init is not None:
            return SelectorList(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['SelectorList']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SelectorList(**it))
            return list_of_self
        else:
            return init


class RuleUsage(ProtocolType):
    """
    CSS coverage information.
    """

    def __init__(self, styleSheetId: StyleSheetId, startOffset: float, endOffset: float, used: bool) -> None:
        """
        :param styleSheetId: The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        :type styleSheetId: str
        :param startOffset: Offset of the start of the rule (including selector) from the beginning of the stylesheet.
        :type startOffset: float
        :param endOffset: Offset of the end of the rule body from the beginning of the stylesheet.
        :type endOffset: float
        :param used: Indicates whether the rule was actually used by some element in the page.
        :type used: bool
        """
        super().__init__()
        self.styleSheetId = styleSheetId
        self.startOffset = startOffset
        self.endOffset = endOffset
        self.used = used

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['RuleUsage']:
        if init is not None:
            return RuleUsage(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['RuleUsage']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RuleUsage(**it))
            return list_of_self
        else:
            return init


class RuleMatch(ProtocolType):
    """
    Match data for a CSS rule.
    """

    def __init__(self, rule: Union['CSSRule', dict], matchingSelectors: List[int]) -> None:
        """
        :param rule: CSS rule in the match.
        :type rule: dict
        :param matchingSelectors: Matching selector indices in the rule's selectorList selectors (0-based).
        :type matchingSelectors: List[int]
        """
        super().__init__()
        self.rule = CSSRule.safe_create(rule)
        self.matchingSelectors = matchingSelectors

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['RuleMatch']:
        if init is not None:
            return RuleMatch(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['RuleMatch']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RuleMatch(**it))
            return list_of_self
        else:
            return init


class PseudoElementMatches(ProtocolType):
    """
    CSS rule collection for a single pseudo style.
    """

    def __init__(self, pseudoType: DOM.PseudoType, matches: List[Union['RuleMatch', dict]]) -> None:
        """
        :param pseudoType: Pseudo element type.
        :type pseudoType: str
        :param matches: Matches of CSS rules applicable to the pseudo style.
        :type matches: List[dict]
        """
        super().__init__()
        self.pseudoType = pseudoType
        self.matches = RuleMatch.safe_create_from_list(matches)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['PseudoElementMatches']:
        if init is not None:
            return PseudoElementMatches(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['PseudoElementMatches']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PseudoElementMatches(**it))
            return list_of_self
        else:
            return init


class PlatformFontUsage(ProtocolType):
    """
    Information about amount of glyphs that were rendered with given font.
    """

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
        self.familyName = familyName
        self.isCustomFont = isCustomFont
        self.glyphCount = glyphCount

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['PlatformFontUsage']:
        if init is not None:
            return PlatformFontUsage(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['PlatformFontUsage']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PlatformFontUsage(**it))
            return list_of_self
        else:
            return init


class MediaQueryExpression(ProtocolType):
    """
    Media query expression descriptor.
    """

    def __init__(self, value: float, unit: str, feature: str, valueRange: Optional[Union['SourceRange', dict]] = None, computedLength: Optional[float] = None) -> None:
        """
        :param value: Media query expression value.
        :type value: float
        :param unit: Media query expression units.
        :type unit: str
        :param feature: Media query expression feature.
        :type feature: str
        :param valueRange: The associated range of the value text in the enclosing stylesheet (if available).
        :type valueRange: Optional[dict]
        :param computedLength: Computed length of media query expression (if applicable).
        :type computedLength: Optional[float]
        """
        super().__init__()
        self.value = value
        self.unit = unit
        self.feature = feature
        self.valueRange = SourceRange.safe_create(valueRange)
        self.computedLength = computedLength

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['MediaQueryExpression']:
        if init is not None:
            return MediaQueryExpression(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['MediaQueryExpression']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MediaQueryExpression(**it))
            return list_of_self
        else:
            return init


class MediaQuery(ProtocolType):
    """
    Media query descriptor.
    """

    def __init__(self, expressions: List[Union['MediaQueryExpression', dict]], active: bool) -> None:
        """
        :param expressions: Array of media query expressions.
        :type expressions: List[dict]
        :param active: Whether the media query condition is satisfied.
        :type active: bool
        """
        super().__init__()
        self.expressions = MediaQueryExpression.safe_create_from_list(expressions)
        self.active = active

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['MediaQuery']:
        if init is not None:
            return MediaQuery(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['MediaQuery']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MediaQuery(**it))
            return list_of_self
        else:
            return init


class InheritedStyleEntry(ProtocolType):
    """
    Inherited CSS rule collection from ancestor node.
    """

    def __init__(self, matchedCSSRules: List[Union['RuleMatch', dict]], inlineStyle: Optional[Union['CSSStyle', dict]] = None) -> None:
        """
        :param inlineStyle: The ancestor node's inline style, if any, in the style inheritance chain.
        :type inlineStyle: Optional[dict]
        :param matchedCSSRules: Matches of CSS rules matching the ancestor node in the style inheritance chain.
        :type matchedCSSRules: List[dict]
        """
        super().__init__()
        self.inlineStyle = CSSStyle.safe_create(inlineStyle)
        self.matchedCSSRules = RuleMatch.safe_create_from_list(matchedCSSRules)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['InheritedStyleEntry']:
        if init is not None:
            return InheritedStyleEntry(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['InheritedStyleEntry']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InheritedStyleEntry(**it))
            return list_of_self
        else:
            return init


class FontFace(ProtocolType):
    """
    Properties of a web font: https://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#font-descriptions
    """

    def __init__(self, fontFamily: str, fontStyle: str, fontVariant: str, fontWeight: str, fontStretch: str, unicodeRange: str, src: str, platformFontFamily: str) -> None:
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
        self.fontFamily = fontFamily
        self.fontStyle = fontStyle
        self.fontVariant = fontVariant
        self.fontWeight = fontWeight
        self.fontStretch = fontStretch
        self.unicodeRange = unicodeRange
        self.src = src
        self.platformFontFamily = platformFontFamily

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['FontFace']:
        if init is not None:
            return FontFace(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FontFace']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FontFace(**it))
            return list_of_self
        else:
            return init


class CSSStyleSheetHeader(ProtocolType):
    """
    CSS stylesheet metainformation.
    """

    def __init__(self, styleSheetId: StyleSheetId, frameId: Page.FrameId, sourceURL: str, origin: StyleSheetOrigin, title: str, disabled: bool, isInline: bool, startLine: float, startColumn: float, length: float, sourceMapURL: Optional[str] = None, ownerNode: Optional[DOM.BackendNodeId] = None, hasSourceURL: Optional[bool] = None) -> None:
        """
        :param styleSheetId: The stylesheet identifier.
        :type styleSheetId: str
        :param frameId: Owner frame identifier.
        :type frameId: str
        :param sourceURL: Stylesheet resource URL.
        :type sourceURL: str
        :param sourceMapURL: URL of source map associated with the stylesheet (if any).
        :type sourceMapURL: Optional[str]
        :param origin: Stylesheet origin.
        :type origin: str
        :param title: Stylesheet title.
        :type title: str
        :param ownerNode: The backend id for the owner node of the stylesheet.
        :type ownerNode: Optional[int]
        :param disabled: Denotes whether the stylesheet is disabled.
        :type disabled: bool
        :param hasSourceURL: Whether the sourceURL field value comes from the sourceURL comment.
        :type hasSourceURL: Optional[bool]
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
        self.styleSheetId = styleSheetId
        self.frameId = frameId
        self.sourceURL = sourceURL
        self.sourceMapURL = sourceMapURL
        self.origin = origin
        self.title = title
        self.ownerNode = ownerNode
        self.disabled = disabled
        self.hasSourceURL = hasSourceURL
        self.isInline = isInline
        self.startLine = startLine
        self.startColumn = startColumn
        self.length = length

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CSSStyleSheetHeader']:
        if init is not None:
            return CSSStyleSheetHeader(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CSSStyleSheetHeader']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSStyleSheetHeader(**it))
            return list_of_self
        else:
            return init


class CSSStyle(ProtocolType):
    """
    CSS style representation.
    """

    def __init__(self, cssProperties: List[Union['CSSProperty', dict]], shorthandEntries: List[Union['ShorthandEntry', dict]], styleSheetId: Optional[StyleSheetId] = None, cssText: Optional[str] = None, range: Optional[Union['SourceRange', dict]] = None) -> None:
        """
        :param styleSheetId: The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        :type styleSheetId: Optional[str]
        :param cssProperties: CSS properties in the style.
        :type cssProperties: List[dict]
        :param shorthandEntries: Computed values for all shorthands found in the style.
        :type shorthandEntries: List[dict]
        :param cssText: Style declaration text (if available).
        :type cssText: Optional[str]
        :param range: Style declaration range in the enclosing stylesheet (if available).
        :type range: Optional[dict]
        """
        super().__init__()
        self.styleSheetId = styleSheetId
        self.cssProperties = CSSProperty.safe_create_from_list(cssProperties)
        self.shorthandEntries = ShorthandEntry.safe_create_from_list(shorthandEntries)
        self.cssText = cssText
        self.range = SourceRange.safe_create(range)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CSSStyle']:
        if init is not None:
            return CSSStyle(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CSSStyle']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSStyle(**it))
            return list_of_self
        else:
            return init


class CSSRule(ProtocolType):
    """
    CSS rule representation.
    """

    def __init__(self, selectorList: Union['SelectorList', dict], origin: StyleSheetOrigin, style: Union['CSSStyle', dict], styleSheetId: Optional[StyleSheetId] = None, media: Optional[List[Union['CSSMedia', dict]]] = None) -> None:
        """
        :param styleSheetId: The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        :type styleSheetId: Optional[str]
        :param selectorList: Rule selector data.
        :type selectorList: dict
        :param origin: Parent stylesheet's origin.
        :type origin: str
        :param style: Associated style declaration.
        :type style: dict
        :param media: Media list array (for rules involving media queries). The array enumerates media queries starting with the innermost one, going outwards.
        :type media: Optional[List[dict]]
        """
        super().__init__()
        self.styleSheetId = styleSheetId
        self.selectorList = SelectorList.safe_create(selectorList)
        self.origin = origin
        self.style = CSSStyle.safe_create(style)
        self.media = CSSMedia.safe_create_from_list(media)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CSSRule']:
        if init is not None:
            return CSSRule(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CSSRule']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSRule(**it))
            return list_of_self
        else:
            return init


class CSSProperty(ProtocolType):
    """
    CSS property declaration data.
    """

    def __init__(self, name: str, value: str, important: Optional[bool] = None, implicit: Optional[bool] = None, text: Optional[str] = None, parsedOk: Optional[bool] = None, disabled: Optional[bool] = None, range: Optional[Union['SourceRange', dict]] = None) -> None:
        """
        :param name: The property name.
        :type name: str
        :param value: The property value.
        :type value: str
        :param important: Whether the property has "!important" annotation (implies `false` if absent).
        :type important: Optional[bool]
        :param implicit: Whether the property is implicit (implies `false` if absent).
        :type implicit: Optional[bool]
        :param text: The full property text as specified in the style.
        :type text: Optional[str]
        :param parsedOk: Whether the property is understood by the browser (implies `true` if absent).
        :type parsedOk: Optional[bool]
        :param disabled: Whether the property is disabled by the user (present for source-based properties only).
        :type disabled: Optional[bool]
        :param range: The entire property range in the enclosing style declaration (if available).
        :type range: Optional[dict]
        """
        super().__init__()
        self.name = name
        self.value = value
        self.important = important
        self.implicit = implicit
        self.text = text
        self.parsedOk = parsedOk
        self.disabled = disabled
        self.range = SourceRange.safe_create(range)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CSSProperty']:
        if init is not None:
            return CSSProperty(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CSSProperty']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSProperty(**it))
            return list_of_self
        else:
            return init


class CSSMedia(ProtocolType):
    """
    CSS media rule descriptor.
    """

    def __init__(self, text: str, source: str, sourceURL: Optional[str] = None, range: Optional[Union['SourceRange', dict]] = None, styleSheetId: Optional[StyleSheetId] = None, mediaList: Optional[List[Union['MediaQuery', dict]]] = None) -> None:
        """
        :param text: Media query text.
        :type text: str
        :param source: Source of the media query: "mediaRule" if specified by a @media rule, "importRule" if specified by an @import rule, "linkedSheet" if specified by a "media" attribute in a linked stylesheet's LINK tag, "inlineSheet" if specified by a "media" attribute in an inline stylesheet's STYLE tag.
        :type source: str
        :param sourceURL: URL of the document containing the media query description.
        :type sourceURL: Optional[str]
        :param range: The associated rule (@media or @import) header range in the enclosing stylesheet (if available).
        :type range: Optional[dict]
        :param styleSheetId: Identifier of the stylesheet containing this object (if exists).
        :type styleSheetId: Optional[str]
        :param mediaList: Array of media queries.
        :type mediaList: Optional[List[dict]]
        """
        super().__init__()
        self.text = text
        self.source = source
        self.sourceURL = sourceURL
        self.range = SourceRange.safe_create(range)
        self.styleSheetId = styleSheetId
        self.mediaList = MediaQuery.safe_create_from_list(mediaList)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CSSMedia']:
        if init is not None:
            return CSSMedia(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CSSMedia']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSMedia(**it))
            return list_of_self
        else:
            return init


class CSSKeyframesRule(ProtocolType):
    """
    CSS keyframes rule representation.
    """

    def __init__(self, animationName: Union['Value', dict], keyframes: List[Union['CSSKeyframeRule', dict]]) -> None:
        """
        :param animationName: Animation name.
        :type animationName: dict
        :param keyframes: List of keyframes.
        :type keyframes: List[dict]
        """
        super().__init__()
        self.animationName = Value.safe_create(animationName)
        self.keyframes = CSSKeyframeRule.safe_create_from_list(keyframes)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CSSKeyframesRule']:
        if init is not None:
            return CSSKeyframesRule(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CSSKeyframesRule']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSKeyframesRule(**it))
            return list_of_self
        else:
            return init


class CSSKeyframeRule(ProtocolType):
    """
    CSS keyframe rule representation.
    """

    def __init__(self, origin: StyleSheetOrigin, keyText: Union['Value', dict], style: Union['CSSStyle', dict], styleSheetId: Optional[StyleSheetId] = None) -> None:
        """
        :param styleSheetId: The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        :type styleSheetId: Optional[str]
        :param origin: Parent stylesheet's origin.
        :type origin: str
        :param keyText: Associated key text.
        :type keyText: dict
        :param style: Associated style declaration.
        :type style: dict
        """
        super().__init__()
        self.styleSheetId = styleSheetId
        self.origin = origin
        self.keyText = Value.safe_create(keyText)
        self.style = CSSStyle.safe_create(style)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CSSKeyframeRule']:
        if init is not None:
            return CSSKeyframeRule(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CSSKeyframeRule']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSKeyframeRule(**it))
            return list_of_self
        else:
            return init


class CSSComputedStyleProperty(ProtocolType):
    def __init__(self, name: str, value: str) -> None:
        """
        :param name: Computed style property name.
        :type name: str
        :param value: Computed style property value.
        :type value: str
        """
        super().__init__()
        self.name = name
        self.value = value

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CSSComputedStyleProperty']:
        if init is not None:
            return CSSComputedStyleProperty(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CSSComputedStyleProperty']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSComputedStyleProperty(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
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
