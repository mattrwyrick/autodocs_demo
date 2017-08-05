from logic import *

AND = lambda x, y: x and y
OR = lambda x, y: x or y

def create_csv_rules(request):
    rules = create_unordered_rules_from_request(request)
    rules = create_ordred_csv_rules_from_unordered_rules(rules)
    return rules


def create_ordred_csv_rules_from_unordered_rules(rules):
    formatted_rules = []
    indexes = sorted([int(key) for key in rules])
    for i in indexes:
        rule = rules[str(i)]
        formatted_rules.append(rule)
    return formatted_rules


def create_column_mapping(row):
    mapping = {}
    for index, item in enumerate(row):
        mapping[item] = index
    return mapping


def add_to_remove_rules(remove_rules, remove, index):
    if remove:
        remove_rules.add(index)


def update_rules(rules, remove_rules):
    updated_rules = []
    for index, rule in enumerate(rules):
        if index in remove_rules:
            remove_rules.remove(index)
        else:
            updated_rules.append(rule)
    return updated_rules


def iterate_csv(document, data, rules, column_mapping, apply_rule):
    remove_rules = set()

    for rule_index, rule in enumerate(rules):
        remove = special_fixed_rule(document, "top", rule, apply_rule)
        add_to_remove_rules(remove_rules, remove, rule_index)
    rules = update_rules(rules, remove_rules)

    for row_number, row_data in enumerate(data, start=1):
        for rule_index, rule in enumerate(rules):
            if applicable_rule(row_number, row_data, rule, column_mapping):
                remove = apply_rule(document, row_number, row_data, rule, column_mapping)
                add_to_remove_rules(remove_rules, remove, rule_index)
        rules = update_rules(rules, remove_rules)

    for rule_index, rule in enumerate(rules):
        special_fixed_rule(document, "bottom", rule, apply_rule)


def special_fixed_rule(document, name, rule, apply_rule):
    if rule['rule_type'] == "fixed":
        if rule["rule_value"] == name:
            apply_rule(document, "", [], rule, {})
            return True
    return False


def applicable_rule(row_number, row_data, rule, column_mapping):
    rule_type = rule["rule_type"]
    if rule_type == "row":
        return True
    elif rule_type == "fixed":
        return meets_fixed(row_number, rule["rule_value"])
    elif "conditional" in rule_type:
        return meets_condition(row_number, row_data, rule["rule_value"], column_mapping)


def meets_fixed(row_number, rule_value):
    if (rule_value == "bottom") or (rule_value == "top"):
        return False
    if "*" in rule_value:
        return row_number % int(rule_value.split("*")[1]) == 0
    return row_number == int(rule_value)


def meets_condition(row_number, row_data, rule_value, column_mapping):
    text_array = get_text_array_from_text(rule_value)
    text_array = eval_conditions(text_array, row_number, row_data, column_mapping)
    text_array = eval_operators(text_array)
    text_array = eval_parenthesis(text_array)
    text_array = eval_cond_expression(text_array)
    return text_array


def eval_cond_expression(old_array):
    index = 0
    max_len = len(old_array)
    return eval_cond_recursivley(old_array, index, max_len)[0]

def eval_cond_recursivley(old_array, index, max_len):
    result = False
    func = lambda x, y: y

    while index < max_len:
        item = old_array[index]

        if isinstance(item, bool):
            if func is None:
                return False, -1
            else:
                result = func(result, item)
                func = None

        elif (item == AND) or (item == OR):
            if func is not None:
                return False, -1
            else:
                func = item

        elif item == "(":
            if func is None:
                return False, -1
            result, index = eval_cond_recursivley(old_array, index+1, max_len)

        elif item == ")":
            return result, index

        index += 1

    return result, index


def eval_parenthesis(old_array):
    text_array = []
    parenthesis = ["(", ")"]
    for item in old_array:
        if isinstance(item, str) or isinstance(item, unicode):
            for char in item:
                if char in parenthesis:
                    text_array.append(char)
        else:
            text_array.append(item)
    return text_array


def eval_operators(old_array):
    mapping = {"||": OR, "&&": AND,}
    operators = [key for key in mapping]

    for operator in operators:
        text_array = []
        for item in old_array:
            if isinstance(item, str) or isinstance(item, unicode):
                item = item.replace(" ", "")
                temp_array = []
                the_split = item.split(operator)
                len_split = len(the_split)
                index = 0
                while index < len_split:
                    value = the_split[index]
                    if value != "":
                        temp_array.append(value)
                    if index < len_split - 1:
                        temp_array.append(mapping[operator])
                    index += 1
                text_array.extend(temp_array)
            else:
                text_array.append(item)
        old_array = text_array

    return old_array


def eval_conditions(old_array, row_number, row_data, column_mapping):
    text_array = []
    for item in old_array:
        if item.startswith("<") and item.endswith(">"):
            text_array.append(check_condition(item, row_number, row_data, column_mapping))
        else:
            text_array.append(item)
    return text_array


def check_condition(text, row_number, row_data, column_mapping):
    if len(text) > 1:
        text = text[1:-1]
        values = text.split(":")
        method, use_row = get_condition_method(values[0], values[1])
        if use_row:
            return method(values[1], row_number)
        else:
            values1 = row_data[column_mapping[values[1]]] if values[1] in column_mapping else row_data[int(values[1])]
            return method(values1, values[2])


def get_condition_method(func_name, value1):
    if func_name == "startswith":
        return lambda x, y: x.startswith(y), False
    elif func_name == "endswith":
        return lambda x, y: x.endswith(y), False
    elif func_name == "equals":
        return lambda x, y: x == y, False
    elif func_name == "contains":
        return lambda x, y: y in x, False
    elif func_name == "inside":
        return lambda x, y: x in y, False
    elif func_name == "row":
        if "*" in value1:
            return lambda x, y: y % int(x[1:]) == 0, True
        else:
            return lambda x, y: int(x) == y, True

    return lambda x, y: False, True



def check_remove_apply_rule(rule):
    rule_type = rule["rule_type"]
    if rule_type == "conditional1":
        return True
    if rule_type == "fixed":
        if not ("*" in rule["rule_value"]):
            return True
    return False


def replace_text_params_with_data(text, row_number, data, column_mapping):
    text = "!" + text.replace("ROW#", str(row_number))
    text_array = text.split("CSV")
    for index, text in enumerate(text_array):
        if text.startswith("["):
            data_index, extra_text = get_index_from_text(text, column_mapping)
            parameter = get_data_parameter(data_index, data)
            text_array[index] = parameter + extra_text
    return "".join(text_array)[1:]


def get_index_from_text(text, column_mapping):
    text_length = len(text)
    for index, char in enumerate(text):
        if char == "]":
            data_index = text[1:index]
            data_index = column_mapping[data_index] if data_index in column_mapping else int(data_index)
            extra_text = "" if (index+1) == text_length else text[index+1:]
            return data_index, extra_text
    return -1, text


def get_data_parameter(index, data):
    if index == -1:
        return ""
    return data[index]
