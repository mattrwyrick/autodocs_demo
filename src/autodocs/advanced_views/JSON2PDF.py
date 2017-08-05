from datetime import datetime
from django.shortcuts import render
from autodocs.example_data.data import JSON1, JSON2
import autodocs.advanced_views.logic.JSON_logic as logic


def json2pdf_view(request):
    if request.method == "POST":
        rules = logic.create_json_rules(request)
        response = create_pdf_document(request, rules)
        return response
    response = render(request, "converters/JSON2PDF.html")
    return response


def create_pdf_document(request, rules):
    try:
        from json import loads
        text = str(request.POST["text"])

        if text == "1":
            data = JSON1
        elif text == "2":
            data = JSON2
        else:
            data = loads(text)
    except:
        return render(request, 'converters/JSON2PDF.html')

    from autodocs.docx_writer import New_Document
    document = New_Document()
    logic.traverse_json(document, data, rules, apply_rule)
    filename = request.POST["file_name"] if request.POST["file_name"] != u"" else "JSON to PDF - %s" % datetime.now().isoformat()
    response = document.create_output(filename, pdf=True)
    return response


def apply_rule(document, data, rule):
    text = logic.replace_json_text_params_with_data(rule["rule_text"], data)
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