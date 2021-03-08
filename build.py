import glob
import os

html_names = set()
css_names = set()

for html in glob.glob('html/*.html'):
    for css in glob.glob('css/*.css'):
        with open(html) as f:
            html_content = f.read()
        with open(css) as f:
            css_content = f.read()

        html_name = os.path.basename(html)
        css_name = os.path.basename(css)
        assert '__' not in html_name
        assert '__' not in css_name

        html_names.add(html_name)
        css_names.add(css_name)

        out_name = f'www/{html_name}__{css_name}.html'
        with open(out_name, 'w') as f:
            f.write(html_content)
            f.write('<style>' + css_content + '</style>')

with open('index.html') as f:
    index_template = f.read()

h_select = ''
c_select = ''
for h in html_names:
    h_select += (f'''<option value="{h}"{' selected' if 'none' in h else ''}>{h}</option>''')
for c in css_names:
    c_select += (f'''<option value="{c}"{' selected' if 'none' in c else ''}>{c}</option>''')

with open('www/index.html', 'w') as f:
    f.write(index_template.replace('**h**', h_select).replace('**c**', c_select))
