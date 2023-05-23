import os
import re
from flask import Flask, render_template, request, redirect, url_for, Markup, session, Response
from werkzeug.utils import secure_filename
from deep_translator import GoogleTranslator


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt'])

langs_list = GoogleTranslator().get_supported_languages()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def translate_text(text, src, dest):
    max_chars = 4000
    if(src == "" or src == "Detectar idioma"):
        src = 'auto'
    # Divide el texto en líneas en lugar de caracteres individuales
    text_lines = text.splitlines()

    # Traduce cada línea y almacena las traducciones
    translated_lines = []
    current_chars = 0
    current_part = ""
    translator = GoogleTranslator(source=src, target=dest)
    for line in text_lines:
        if current_chars + len(line) < max_chars:
            current_part += line + "\n"
            current_chars += len(line) + 1
        else:
            print("Current chars: " + str(current_chars))
            translated_part = translator.translate(current_part)
            translated_lines.append(translated_part)
            current_part = line + "\n"
            current_chars = len(line) + 1

    print("Current chars sale: " + str(current_chars))
    # Traduce y almacena la última parte del texto
    translated_part = translator.translate(current_part)
    translated_lines.append(translated_part)

    # Une las líneas traducidas en un solo texto
    translated_text = ' '.join(translated_lines)

    return translated_text


def export_html(content):

    return True


def export_txt(content):
    return True


def get_html_template(text, src, dest):
    title_regex = r"<--(.+?)-->"
    match = re.search(title_regex, text)
    if match:
        title = match.group(1)
        text = re.sub(r"<--(.+?)-->", '\n', text)
    else:
        title = "Título no encontrado"

    content_html = Markup(text.replace("\n", "</p>\n<p>"))
    html = render_template(
        'traduccion.html', title=title, content=content_html, src=src, dest=dest)

    return html


def get_html_text(text, src, dest):
    character_names = [
        "100_Man_Challenge",
        "Bi_Sa-Won",
        "Billowing_Clouds",
        "Black_Moon",
        "Broken_Fists_Sect",
        "Buk_Jin-Hu",
        "Bul-Yeong",
        "Central_Heavenly_Alliance",
        "Cerulean_Dragon_Society",
        "Chae_Yak-Ran",
        "Conquerors",
        "Cultivation",
        "Dam_Jeok-Shim",
        "Dam_Jin-Hong",
        "Dam_Soo-Cheon",
        "Deceitful_Heavens",
        "Demon_Extermination_Squad",
        "Dissolution_of_the_Northern_Heavenly_Sect_Arc",
        "Episode_10",
        "Eun_Ha-Seol",
        "Gathering_of_Ten_Thousand_Shadows",
        "Geum_Dan-Yeop",
        "Gong_Son-Chang",
        "Great_Four_of_the_Northern_Heavens",
        "Gwan_Mun-Jung",
        "Ha_Jin-Wol",
        "Ha_Jin-Wol/Image_Gallery",
        "Ha_Jin-Wol/Relationships",
        "Ha_Jin-Wol/Synopsis",
        "Hae-Min",
        "Hidden_Ghost_Sect",
        "Home_of_Ten_Thousand_Spirits",
        "Hwang-Cheol",
        "Hyun_Gong-Hwi",
        "Hyun_Hyun_So",
        "Im_Jin-Yeop",
        "Iron_Brigade",
        "Iron_Castle",
        "Jae_Hyeok-Shim",
        "Jah_Moon-Ho",
        "Jang_Pae-San",
        "Jaw_Hyeok-Shim",
        "Jeok-Yeob",
        "Ji_Sung-Yool",
        "Jin_Kwan-Ho",
        "Jin_Mu-Won",
        "Jin_Mu-Won/Image_Gallery",
        "Jin_Mu-Won/Relationships",
        "Jin_Yeoung-Seol",
        "Jo_Cheon-Woo",
        "Jo_Un-Kyung",
        "Jong_Ri_Mu-hwan",
        "Kyung_Mu-Saeng",
        "Kyung_Mu-Seang",
        "Legend_of_the_Northern_Blade",
        "Legend_of_the_Northern_Blade_Wiki_(Manhwa)",
        "List_of_Characters",
        "Lower_Moon_Kingdom",
        "Main_Page",
        "Man_Seo-Jin",
        "Mok_Eun-Pyeong",
        "Mount_Hua_Sect",
        "Moyong_Hyun",
        "Moyong_Yul-Cheon",
        "Mu-Hwan_of_Wise_Judgment",
        "Mu_Mountain",
        "Murim",
        "Myeong_Ryu-San",
        "Nam_Moon-San",
        "Nam_Soo-Ryeon",
        "Nam_Un-San",
        "Neung_Goon-Hwi",
        "Nine_Skies",
        "Noh_Tae-Tae",
        "Northern_Heavenly_Sect",
        "Novel",
        "Protectors_of_the_Western_Heavens",
        "Rules_&_Regulations",
        "Sa-Ryung",
        "Seo-Moon_Hwa",
        "Seo-Moon_Hye_Ryung",
        "Seo_Geum-Hyang",
        "Seo_Hye-Ryung",
        "Seo_Moon-Hwa",
        "Seo_Mu-Sang",
        "Seven_Lesser_Heavens",
        "Shim_Mu-Wae",
        "Shim_Soo-Ah",
        "Shim_Won-Lee",
        "Shim_Woo-Lee",
        "Shredder",
        "Silent_Night",
        "Snow_Flower",
        "Story_Arcs",
        "Successor_of_the_Northern_Blade",
        "Successor_of_the_Northern_Heavenly_Sect",
        "Successor_of_the_Northern_Heavenly_Sect_Arc",
        "Tae_Mu-Kang",
        "Tang_Family_of_Sichuan",
        "Tang_Geon-Woo",
        "Tang_Gi-Mun",
        "Tang_Mi-Ryeo",
        "Third_Mercenary_Group",
        "Three-Year_War",
        "Timeline",
        "Walls_of_Ten_Thousand_Shadows",
        "West_Gate_Family",
        "White_Dragon_Merchant_Troupe",
        "Wraith_Killer_Sect",
        "Yeon_Cheon-Hwa",
        "Yeon_Cheon-Wha",
        "Yeon_So-So",
        "Yeop-Wol",
        "Yong_Mu-Sung",
        "Yoo_Kwang-Yeon",
        "Yoon_Cheon-Hak"
    ]
    character_names = sorted(character_names, key=len, reverse=True)
    pretext = text
    for character_name in character_names:
        name_aux = character_name.replace('_', ' ')
        escaped_name = re.sub(r'[-_\s]', r'[-_# ]?', character_name)
        regex = re.compile(f"{escaped_name}", re.IGNORECASE)
        wiki_link = f'https://legend-of-the-northern-blade.fandom.com/wiki/{character_name}'
        pretext = regex.sub(
            Markup(f'<a href="{wiki_link}" target="_blank">{name_aux}</a>'), pretext, count=1)
    return get_html_template(pretext, src, dest)


@app.route('/')
def index():
    return render_template('index.html', languages=langs_list)


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_name = secure_filename(file.filename)
    if file and allowed_file(file.filename):
        file_content = file.read().decode('utf-8')
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('index.html', file_content=file_content, file_name=file_name, languages=langs_list)
    else:
        print('Invalid Upload only txt')
    print("file uploaded successfully")
    return render_template('index.html', languages=langs_list)


@app.route('/translate', methods=['POST'])
def translate():
    file = request.files.get('file')
    src = request.form['source_language']
    dest = request.form['target_language']
    if(file):
        file_content = file.read().decode('utf-8')
    else:
        file_content = request.form['file_content']
    translated_text = translate_text(file_content, src, dest)
    html_text = get_html_text(translated_text, src, dest)

    return html_text


@app.route('/download', methods=['POST'])
def download():
    pass


if __name__ == '__main__':
    app.run(debug=True)
