from logic import *

def create_json_rules(request):
    rules = create_unordered_rules_from_request(request)
    rules = create_ordered_json_rules_from_unordered_rules(rules)
    return rules


def create_ordered_json_rules_from_unordered_rules(rules):
    formatted_rules = {}
    indexes = sorted([int(key) for key in rules])
    for i in indexes:
        rule = rules[str(i)]
        add_rule_to_json_formatted_rules(rule, formatted_rules)

    return formatted_rules


def add_rule_to_json_formatted_rules(rule, rules):
    if rule["key_value"] in rules:
        rules[rule["key_value"]].append(rule)
    else:
        rules[rule["key_value"]] = [rule]


def traverse_json(document, data, rules, apply_rule):
    if isinstance(data, dict):
        for key in data:
            if key in rules:
                for rule in rules[key]:
                    if rule["rule_type"] == "key:dict/lit":
                        apply_rule(document, data[key], rule)

            if key in rules:
                if isinstance(data[key], list):
                    for item in data[key]:
                        for rule in rules[key]:
                            if rule["rule_type"] == "key:list":
                                apply_rule(document, item, rule)

            traverse_json(document, data[key], rules, apply_rule)

    elif isinstance(data, list):
        for item in data:
            traverse_json(document, item, rules, apply_rule)


def replace_json_text_params_with_data(text, data):
    if isinstance(data, dict):
        text = "!" + text
        text_array = text.split("JSON")
        for index, text in enumerate(text_array):
            if text.startswith("["):
                dict_keys, extra_text = get_keys_from_text(text, [])
                parameter = get_json_data_parameter(data, dict_keys)
                text_array[index] = parameter + extra_text
        return "".join(text_array)[1:]
    else:
        return text.replace("JSON", str(data))


def get_keys_from_text(text, dict_keys=[]):
    key = ""
    expect_key = True
    for index, char in enumerate(text):
        if expect_key and char == "[":
            expect_key = False

        elif expect_key and char != "[":
            return dict_keys, text[index:]

        elif not expect_key and char == "]":
            expect_key = True
            dict_keys.append(key)
            key = ""

        else:
            key += char

    return dict_keys, ""


def get_json_data_parameter(data, dict_keys):
    if len(dict_keys) == 0:
        return str(data)
    return get_json_data_parameter(data[dict_keys[0]], dict_keys[1:])
