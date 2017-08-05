##################################
############ RULES ###############
##################################
def create_unordered_rules_from_request(request):
    rules = {}
    for key in request.POST:
        if key.startswith("rule-") and not (key.endswith(":0")):
            add_post_info_to_rules(rules, key, request.POST)

    return rules


def add_post_info_to_rules(rules, key, post):
    item_index = key.split('-')[1].split(":")[1]
    item_key = key.split('-')[1].split(':')[0]
    item_value = post[key]
    if item_index in rules:
        rules[item_index][item_key] = item_value
    else:
        rules[item_index] = {}
        rules[item_index][item_key] = item_value


##################################
############ STYLE ###############
##################################
class StyleRule(object):
    def __init__(self, style, value, cast=lambda x: x):
        self.style = style
        self.value = cast(value)


def write_style_list_to_word(segment, style_list):
    increment_by = lambda x, y: x + y
    params = {
        "bold": [0, increment_by],
        "italic": [0, increment_by],
        "underline": [0, increment_by],
        "font": [[], append_style_value_to_list],
        "size": [[], append_style_value_to_list],
    }

    for item in style_list:
        if isinstance(item, StyleRule):
            if item.style in params:
                update_param = params[item.style]
                update_param[0] = update_param[1](update_param[0], item.value)
        else:
            bold = True if params["bold"][0] > 0 else False
            italic = True if params["italic"][0] > 0 else False
            underline = True if params["underline"][0] > 0 else False
            font = params["font"][0][-1] if len(params["font"][0]) > 0 else "garamond"
            size = params["size"][0][-1] if len(params["size"][0]) > 0 else False
            segment.write(text=item, bold=bold, italic=italic, underline=underline, font=font, size=size)


def append_style_value_to_list(array, value):
    if (value is None) and (array != []):
        del array[-1]
    elif value is not None:
        array.append(value)
    return array


def text_to_style_list(text):
    text_array = get_text_array_from_style_text(text)
    formatted_array = format_style_text_array(text_array)
    return formatted_array


def format_style_text_array(text_array):
    cast_int = lambda x: int(x)
    cast_str = lambda x: str(x)

    exact_styles = {
        "<b>": ("bold", 1),
        "</b>": ("bold", -1),
        "<i>": ("italic", 1),
        "</i>": ("italic", -1),
        "<u>": ("underline", 1),
        "</u>": ("underline", -1),
        "</font>": ("font", None),
        "</size>": ("size", None),
    }

    conditional_styles = {
        "<font": ("font", cast_str),
        "<size": ("size", cast_int),
    }

    formatted_array = []
    for item in text_array:
        split_item = item.split(":")

        if item in exact_styles:
            style = exact_styles[item]
            formatted_array.append(StyleRule(style[0], style[1]))

        elif (split_item[0] in conditional_styles) and (len(split_item) == 2):
            style = conditional_styles[split_item[0]]
            formatted_array.append(StyleRule(style[0], split_item[1].replace(">", ""), style[1]))

        else:
            formatted_array.append(item)

    return formatted_array


def get_text_array_from_text(text):
    text = text.replace("<br>", "\n")
    text_array = []
    start = None
    index = 0
    marker_index = 0
    for index, char in enumerate(text):
        if char == "<":
            start = index
            if marker_index != index:
                text_array.append(text[marker_index: index])
        elif char == ">":
            if start is not None:
                text_array.append(text[start: index+1])
                marker_index = index + 1
            start = None

    if marker_index < index:
        text_array.append(text[marker_index: index+1])

    return text_array


def get_text_array_from_style_text(text):
    text = text.replace("<br>", "\n")
    return get_text_array_from_text(text)




