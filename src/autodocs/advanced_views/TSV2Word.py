from datetime import datetime
from django.shortcuts import render
from autodocs.example_data.data import CSV1
import autodocs.advanced_views.logic.CSV_logic as logic


def tsv2word_view(request):
    if request.method == "POST":
        rules = logic.create_csv_rules(request)
        response = create_word_document(request, rules)
        return response
    response = render(request, "converters/TSV2Word.html")
    return response


def create_word_document(request, rules):
    try:
        text = request.POST["text"]
        if text == "1":
            text = CSV1.replace(",", "\t")
        data = (line.split('\t') for line in text.split("\n"))
    except:
        return render(request, 'converters/TSV2Word.html')

    from autodocs.docx_writer import New_Document
    document = New_Document()
    column_mapping = logic.create_column_mapping(data.next())
    logic.iterate_csv(document, data, rules, column_mapping, apply_rule)
    filename = request.POST["file_name"] if request.POST["file_name"] != u"" else "TSV to Word - %s" % datetime.now().isoformat()
    response = document.create_output(filename)
    return response


def apply_rule(document, row_number, row_data, rule, column_mapping):
    text = logic.replace_text_params_with_data(rule["rule_text"], row_number, row_data, column_mapping)
    style_list = logic.text_to_style_list(text)

    doc_type = rule["text_type"]
    if doc_type == "paragraph":
        segment = document.add_paragraph()
    elif "heading" in doc_type:
        segment = document.add_heading(level=int(doc_type.split(":")[1]))
    else:
        segment = None

    if segment:
        logic.write_style_list_to_word(segment, style_list)

    return logic.check_remove_apply_rule(rule)
