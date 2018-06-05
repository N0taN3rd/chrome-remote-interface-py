from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.dom import types as DOM
from cripy.protocol.page import types as Page


class Value(object):
    """
    Data for a simple selector (these are delimited by commas in a selector list).
    """

    def __init__(
        self, text: str, range: Optional[Union["SourceRange", dict]] = None
    ) -> None:
        """
        :param text: Value text.
        :type text: str
        :param range: Value range in the underlying resource (if available).
        :type range: Optional[dict]
        """
        super().__init__()
        self.text = text
        self.range = SourceRange.safe_create(range)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.text is not None:
            repr_args.append("text={!r}".format(self.text))
        if self.range is not None:
            repr_args.append("range={!r}".format(self.range))
        return "Value(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["Value", dict]]:
        if init is not None:
            try:
                ourselves = Value(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["Value", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Value.safe_create(it))
            return list_of_self
        else:
            return init


class StyleDeclarationEdit(object):
    """
    A descriptor of operation to mutate style declaration text.
    """

    def __init__(
        self, styleSheetId: str, range: Union["SourceRange", dict], text: str
    ) -> None:
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.styleSheetId is not None:
            repr_args.append("styleSheetId={!r}".format(self.styleSheetId))
        if self.range is not None:
            repr_args.append("range={!r}".format(self.range))
        if self.text is not None:
            repr_args.append("text={!r}".format(self.text))
        return "StyleDeclarationEdit(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["StyleDeclarationEdit", dict]]:
        if init is not None:
            try:
                ourselves = StyleDeclarationEdit(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["StyleDeclarationEdit", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StyleDeclarationEdit.safe_create(it))
            return list_of_self
        else:
            return init


class SourceRange(object):
    """
    Text range within a resource. All numbers are zero-based.
    """

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
        self.startLine = startLine
        self.startColumn = startColumn
        self.endLine = endLine
        self.endColumn = endColumn

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.startLine is not None:
            repr_args.append("startLine={!r}".format(self.startLine))
        if self.startColumn is not None:
            repr_args.append("startColumn={!r}".format(self.startColumn))
        if self.endLine is not None:
            repr_args.append("endLine={!r}".format(self.endLine))
        if self.endColumn is not None:
            repr_args.append("endColumn={!r}".format(self.endColumn))
        return "SourceRange(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["SourceRange", dict]]:
        if init is not None:
            try:
                ourselves = SourceRange(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["SourceRange", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SourceRange.safe_create(it))
            return list_of_self
        else:
            return init


class ShorthandEntry(object):

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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        if self.important is not None:
            repr_args.append("important={!r}".format(self.important))
        return "ShorthandEntry(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["ShorthandEntry", dict]]:
        if init is not None:
            try:
                ourselves = ShorthandEntry(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ShorthandEntry", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ShorthandEntry.safe_create(it))
            return list_of_self
        else:
            return init


class SelectorList(object):
    """
    Selector list data.
    """

    def __init__(self, selectors: List[Union["Value", dict]], text: str) -> None:
        """
        :param selectors: Selectors in the list.
        :type selectors: List[dict]
        :param text: Rule selector text.
        :type text: str
        """
        super().__init__()
        self.selectors = Value.safe_create_from_list(selectors)
        self.text = text

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.selectors is not None:
            repr_args.append("selectors={!r}".format(self.selectors))
        if self.text is not None:
            repr_args.append("text={!r}".format(self.text))
        return "SelectorList(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["SelectorList", dict]]:
        if init is not None:
            try:
                ourselves = SelectorList(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["SelectorList", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SelectorList.safe_create(it))
            return list_of_self
        else:
            return init


class RuleUsage(object):
    """
    CSS coverage information.
    """

    def __init__(
        self, styleSheetId: str, startOffset: float, endOffset: float, used: bool
    ) -> None:
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.styleSheetId is not None:
            repr_args.append("styleSheetId={!r}".format(self.styleSheetId))
        if self.startOffset is not None:
            repr_args.append("startOffset={!r}".format(self.startOffset))
        if self.endOffset is not None:
            repr_args.append("endOffset={!r}".format(self.endOffset))
        if self.used is not None:
            repr_args.append("used={!r}".format(self.used))
        return "RuleUsage(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["RuleUsage", dict]]:
        if init is not None:
            try:
                ourselves = RuleUsage(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["RuleUsage", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RuleUsage.safe_create(it))
            return list_of_self
        else:
            return init


class RuleMatch(object):
    """
    Match data for a CSS rule.
    """

    def __init__(
        self, rule: Union["CSSRule", dict], matchingSelectors: List[int]
    ) -> None:
        """
        :param rule: CSS rule in the match.
        :type rule: dict
        :param matchingSelectors: Matching selector indices in the rule's selectorList selectors (0-based).
        :type matchingSelectors: List[int]
        """
        super().__init__()
        self.rule = CSSRule.safe_create(rule)
        self.matchingSelectors = matchingSelectors

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.rule is not None:
            repr_args.append("rule={!r}".format(self.rule))
        if self.matchingSelectors is not None:
            repr_args.append("matchingSelectors={!r}".format(self.matchingSelectors))
        return "RuleMatch(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["RuleMatch", dict]]:
        if init is not None:
            try:
                ourselves = RuleMatch(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["RuleMatch", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RuleMatch.safe_create(it))
            return list_of_self
        else:
            return init


class PseudoElementMatches(object):
    """
    CSS rule collection for a single pseudo style.
    """

    def __init__(
        self, pseudoType: str, matches: List[Union["RuleMatch", dict]]
    ) -> None:
        """
        :param pseudoType: Pseudo element type.
        :type pseudoType: str
        :param matches: Matches of CSS rules applicable to the pseudo style.
        :type matches: List[dict]
        """
        super().__init__()
        self.pseudoType = pseudoType
        self.matches = RuleMatch.safe_create_from_list(matches)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.pseudoType is not None:
            repr_args.append("pseudoType={!r}".format(self.pseudoType))
        if self.matches is not None:
            repr_args.append("matches={!r}".format(self.matches))
        return "PseudoElementMatches(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["PseudoElementMatches", dict]]:
        if init is not None:
            try:
                ourselves = PseudoElementMatches(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["PseudoElementMatches", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PseudoElementMatches.safe_create(it))
            return list_of_self
        else:
            return init


class PlatformFontUsage(object):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.familyName is not None:
            repr_args.append("familyName={!r}".format(self.familyName))
        if self.isCustomFont is not None:
            repr_args.append("isCustomFont={!r}".format(self.isCustomFont))
        if self.glyphCount is not None:
            repr_args.append("glyphCount={!r}".format(self.glyphCount))
        return "PlatformFontUsage(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["PlatformFontUsage", dict]]:
        if init is not None:
            try:
                ourselves = PlatformFontUsage(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["PlatformFontUsage", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PlatformFontUsage.safe_create(it))
            return list_of_self
        else:
            return init


class MediaQueryExpression(object):
    """
    Media query expression descriptor.
    """

    def __init__(
        self,
        value: float,
        unit: str,
        feature: str,
        valueRange: Optional[Union["SourceRange", dict]] = None,
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        if self.unit is not None:
            repr_args.append("unit={!r}".format(self.unit))
        if self.feature is not None:
            repr_args.append("feature={!r}".format(self.feature))
        if self.valueRange is not None:
            repr_args.append("valueRange={!r}".format(self.valueRange))
        if self.computedLength is not None:
            repr_args.append("computedLength={!r}".format(self.computedLength))
        return "MediaQueryExpression(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["MediaQueryExpression", dict]]:
        if init is not None:
            try:
                ourselves = MediaQueryExpression(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["MediaQueryExpression", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MediaQueryExpression.safe_create(it))
            return list_of_self
        else:
            return init


class MediaQuery(object):
    """
    Media query descriptor.
    """

    def __init__(
        self, expressions: List[Union["MediaQueryExpression", dict]], active: bool
    ) -> None:
        """
        :param expressions: Array of media query expressions.
        :type expressions: List[dict]
        :param active: Whether the media query condition is satisfied.
        :type active: bool
        """
        super().__init__()
        self.expressions = MediaQueryExpression.safe_create_from_list(expressions)
        self.active = active

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.expressions is not None:
            repr_args.append("expressions={!r}".format(self.expressions))
        if self.active is not None:
            repr_args.append("active={!r}".format(self.active))
        return "MediaQuery(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["MediaQuery", dict]]:
        if init is not None:
            try:
                ourselves = MediaQuery(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["MediaQuery", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MediaQuery.safe_create(it))
            return list_of_self
        else:
            return init


class InheritedStyleEntry(object):
    """
    Inherited CSS rule collection from ancestor node.
    """

    def __init__(
        self,
        matchedCSSRules: List[Union["RuleMatch", dict]],
        inlineStyle: Optional[Union["CSSStyle", dict]] = None,
    ) -> None:
        """
        :param inlineStyle: The ancestor node's inline style, if any, in the style inheritance chain.
        :type inlineStyle: Optional[dict]
        :param matchedCSSRules: Matches of CSS rules matching the ancestor node in the style inheritance chain.
        :type matchedCSSRules: List[dict]
        """
        super().__init__()
        self.inlineStyle = CSSStyle.safe_create(inlineStyle)
        self.matchedCSSRules = RuleMatch.safe_create_from_list(matchedCSSRules)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.inlineStyle is not None:
            repr_args.append("inlineStyle={!r}".format(self.inlineStyle))
        if self.matchedCSSRules is not None:
            repr_args.append("matchedCSSRules={!r}".format(self.matchedCSSRules))
        return "InheritedStyleEntry(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["InheritedStyleEntry", dict]]:
        if init is not None:
            try:
                ourselves = InheritedStyleEntry(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["InheritedStyleEntry", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InheritedStyleEntry.safe_create(it))
            return list_of_self
        else:
            return init


class FontFace(object):
    """
    Properties of a web font: https://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#font-descriptions
    """

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
        self.fontFamily = fontFamily
        self.fontStyle = fontStyle
        self.fontVariant = fontVariant
        self.fontWeight = fontWeight
        self.fontStretch = fontStretch
        self.unicodeRange = unicodeRange
        self.src = src
        self.platformFontFamily = platformFontFamily

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.fontFamily is not None:
            repr_args.append("fontFamily={!r}".format(self.fontFamily))
        if self.fontStyle is not None:
            repr_args.append("fontStyle={!r}".format(self.fontStyle))
        if self.fontVariant is not None:
            repr_args.append("fontVariant={!r}".format(self.fontVariant))
        if self.fontWeight is not None:
            repr_args.append("fontWeight={!r}".format(self.fontWeight))
        if self.fontStretch is not None:
            repr_args.append("fontStretch={!r}".format(self.fontStretch))
        if self.unicodeRange is not None:
            repr_args.append("unicodeRange={!r}".format(self.unicodeRange))
        if self.src is not None:
            repr_args.append("src={!r}".format(self.src))
        if self.platformFontFamily is not None:
            repr_args.append("platformFontFamily={!r}".format(self.platformFontFamily))
        return "FontFace(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["FontFace", dict]]:
        if init is not None:
            try:
                ourselves = FontFace(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["FontFace", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FontFace.safe_create(it))
            return list_of_self
        else:
            return init


class CSSStyleSheetHeader(object):
    """
    CSS stylesheet metainformation.
    """

    def __init__(
        self,
        styleSheetId: str,
        frameId: str,
        sourceURL: str,
        origin: str,
        title: str,
        disabled: bool,
        isInline: bool,
        startLine: float,
        startColumn: float,
        length: float,
        sourceMapURL: Optional[str] = None,
        ownerNode: Optional[int] = None,
        hasSourceURL: Optional[bool] = None,
    ) -> None:
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.styleSheetId is not None:
            repr_args.append("styleSheetId={!r}".format(self.styleSheetId))
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.sourceURL is not None:
            repr_args.append("sourceURL={!r}".format(self.sourceURL))
        if self.sourceMapURL is not None:
            repr_args.append("sourceMapURL={!r}".format(self.sourceMapURL))
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        if self.title is not None:
            repr_args.append("title={!r}".format(self.title))
        if self.ownerNode is not None:
            repr_args.append("ownerNode={!r}".format(self.ownerNode))
        if self.disabled is not None:
            repr_args.append("disabled={!r}".format(self.disabled))
        if self.hasSourceURL is not None:
            repr_args.append("hasSourceURL={!r}".format(self.hasSourceURL))
        if self.isInline is not None:
            repr_args.append("isInline={!r}".format(self.isInline))
        if self.startLine is not None:
            repr_args.append("startLine={!r}".format(self.startLine))
        if self.startColumn is not None:
            repr_args.append("startColumn={!r}".format(self.startColumn))
        if self.length is not None:
            repr_args.append("length={!r}".format(self.length))
        return "CSSStyleSheetHeader(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["CSSStyleSheetHeader", dict]]:
        if init is not None:
            try:
                ourselves = CSSStyleSheetHeader(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["CSSStyleSheetHeader", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSStyleSheetHeader.safe_create(it))
            return list_of_self
        else:
            return init


class CSSStyle(object):
    """
    CSS style representation.
    """

    def __init__(
        self,
        cssProperties: List[Union["CSSProperty", dict]],
        shorthandEntries: List[Union["ShorthandEntry", dict]],
        styleSheetId: Optional[str] = None,
        cssText: Optional[str] = None,
        range: Optional[Union["SourceRange", dict]] = None,
    ) -> None:
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.styleSheetId is not None:
            repr_args.append("styleSheetId={!r}".format(self.styleSheetId))
        if self.cssProperties is not None:
            repr_args.append("cssProperties={!r}".format(self.cssProperties))
        if self.shorthandEntries is not None:
            repr_args.append("shorthandEntries={!r}".format(self.shorthandEntries))
        if self.cssText is not None:
            repr_args.append("cssText={!r}".format(self.cssText))
        if self.range is not None:
            repr_args.append("range={!r}".format(self.range))
        return "CSSStyle(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["CSSStyle", dict]]:
        if init is not None:
            try:
                ourselves = CSSStyle(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["CSSStyle", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSStyle.safe_create(it))
            return list_of_self
        else:
            return init


class CSSRule(object):
    """
    CSS rule representation.
    """

    def __init__(
        self,
        selectorList: Union["SelectorList", dict],
        origin: str,
        style: Union["CSSStyle", dict],
        styleSheetId: Optional[str] = None,
        media: Optional[List[Union["CSSMedia", dict]]] = None,
    ) -> None:
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.styleSheetId is not None:
            repr_args.append("styleSheetId={!r}".format(self.styleSheetId))
        if self.selectorList is not None:
            repr_args.append("selectorList={!r}".format(self.selectorList))
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        if self.style is not None:
            repr_args.append("style={!r}".format(self.style))
        if self.media is not None:
            repr_args.append("media={!r}".format(self.media))
        return "CSSRule(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["CSSRule", dict]]:
        if init is not None:
            try:
                ourselves = CSSRule(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["CSSRule", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSRule.safe_create(it))
            return list_of_self
        else:
            return init


class CSSProperty(object):
    """
    CSS property declaration data.
    """

    def __init__(
        self,
        name: str,
        value: str,
        important: Optional[bool] = None,
        implicit: Optional[bool] = None,
        text: Optional[str] = None,
        parsedOk: Optional[bool] = None,
        disabled: Optional[bool] = None,
        range: Optional[Union["SourceRange", dict]] = None,
    ) -> None:
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        if self.important is not None:
            repr_args.append("important={!r}".format(self.important))
        if self.implicit is not None:
            repr_args.append("implicit={!r}".format(self.implicit))
        if self.text is not None:
            repr_args.append("text={!r}".format(self.text))
        if self.parsedOk is not None:
            repr_args.append("parsedOk={!r}".format(self.parsedOk))
        if self.disabled is not None:
            repr_args.append("disabled={!r}".format(self.disabled))
        if self.range is not None:
            repr_args.append("range={!r}".format(self.range))
        return "CSSProperty(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["CSSProperty", dict]]:
        if init is not None:
            try:
                ourselves = CSSProperty(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["CSSProperty", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSProperty.safe_create(it))
            return list_of_self
        else:
            return init


class CSSMedia(object):
    """
    CSS media rule descriptor.
    """

    def __init__(
        self,
        text: str,
        source: str,
        sourceURL: Optional[str] = None,
        range: Optional[Union["SourceRange", dict]] = None,
        styleSheetId: Optional[str] = None,
        mediaList: Optional[List[Union["MediaQuery", dict]]] = None,
    ) -> None:
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.text is not None:
            repr_args.append("text={!r}".format(self.text))
        if self.source is not None:
            repr_args.append("source={!r}".format(self.source))
        if self.sourceURL is not None:
            repr_args.append("sourceURL={!r}".format(self.sourceURL))
        if self.range is not None:
            repr_args.append("range={!r}".format(self.range))
        if self.styleSheetId is not None:
            repr_args.append("styleSheetId={!r}".format(self.styleSheetId))
        if self.mediaList is not None:
            repr_args.append("mediaList={!r}".format(self.mediaList))
        return "CSSMedia(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["CSSMedia", dict]]:
        if init is not None:
            try:
                ourselves = CSSMedia(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["CSSMedia", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSMedia.safe_create(it))
            return list_of_self
        else:
            return init


class CSSKeyframesRule(object):
    """
    CSS keyframes rule representation.
    """

    def __init__(
        self,
        animationName: Union["Value", dict],
        keyframes: List[Union["CSSKeyframeRule", dict]],
    ) -> None:
        """
        :param animationName: Animation name.
        :type animationName: dict
        :param keyframes: List of keyframes.
        :type keyframes: List[dict]
        """
        super().__init__()
        self.animationName = Value.safe_create(animationName)
        self.keyframes = CSSKeyframeRule.safe_create_from_list(keyframes)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.animationName is not None:
            repr_args.append("animationName={!r}".format(self.animationName))
        if self.keyframes is not None:
            repr_args.append("keyframes={!r}".format(self.keyframes))
        return "CSSKeyframesRule(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["CSSKeyframesRule", dict]]:
        if init is not None:
            try:
                ourselves = CSSKeyframesRule(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["CSSKeyframesRule", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSKeyframesRule.safe_create(it))
            return list_of_self
        else:
            return init


class CSSKeyframeRule(object):
    """
    CSS keyframe rule representation.
    """

    def __init__(
        self,
        origin: str,
        keyText: Union["Value", dict],
        style: Union["CSSStyle", dict],
        styleSheetId: Optional[str] = None,
    ) -> None:
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.styleSheetId is not None:
            repr_args.append("styleSheetId={!r}".format(self.styleSheetId))
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        if self.keyText is not None:
            repr_args.append("keyText={!r}".format(self.keyText))
        if self.style is not None:
            repr_args.append("style={!r}".format(self.style))
        return "CSSKeyframeRule(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["CSSKeyframeRule", dict]]:
        if init is not None:
            try:
                ourselves = CSSKeyframeRule(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["CSSKeyframeRule", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSKeyframeRule.safe_create(it))
            return list_of_self
        else:
            return init


class CSSComputedStyleProperty(object):

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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        return "CSSComputedStyleProperty(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["CSSComputedStyleProperty", dict]]:
        if init is not None:
            try:
                ourselves = CSSComputedStyleProperty(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["CSSComputedStyleProperty", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CSSComputedStyleProperty.safe_create(it))
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
