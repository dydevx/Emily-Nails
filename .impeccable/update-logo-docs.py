from pathlib import Path
import json,re,colorsys

root=Path(__file__).resolve().parent.parent
renames={'rose-deep':'gold-deep','rose':'gold','blush':'cream','pink':'petal'}
colors={'#fffcfd':'#fffaf5','#fcf3f5':'#f5ebe2','#f4e4e9':'#ead1cc','#92506b':'#8a613b','#763d55':'#6c472b','#302630':'#403026','#6f5c67':'#705c4e','#e5d6dd':'#e0cfbe'}
def remap(s):
    for a,b in renames.items():s=re.sub(r'\b'+a+r'\b',b,s)
    for a,b in colors.items():s=s.replace(a,b)
    return s.replace('rgb(48 38 48','rgb(64 48 38')

p=root/'DESIGN.md'
s=remap(p.read_text(encoding='utf-8'))
s=s.replace('Elegant, gentle salon editorial in one light petal theme.','Elegant salon editorial in the original logo\'s ivory, bronze-gold and blush palette.')
s=s.replace('Emily Nails pairs airy petal surfaces with expressive serif headings and quiet, readable service information. The user-confirmed character is elegant and gentle, retaining petal. Generous spacing and original salon media make the website feel personal and considered.','Emily Nails pairs warm ivory surfaces with bronze-gold actions and soft blush accents taken from the original logo. The user requested this logo palette, more AI beauty imagery and custom social icons. Expressive serif headings and readable service information preserve the elegant, gentle character.')
s=s.replace('Pale petal surfaces and a restrained deep gold accent.','Warm ivory surfaces, bronze-gold accents and gentle blush details.')
s=s.replace('The palette is warm, quiet and petal throughout;','The palette follows the cream, bronze-gold and pink details of logo.jpg;')
s=s.replace('**Rose:**','**Bronze Gold:**').replace('**Deep Rose:**','**Deep Bronze:**')
s=s.replace('**Blush Paper:**','**Warm Cream:**').replace('**Soft Pink:**','**Petal Blush:**')
s=s.replace('**Plum Ink:**','**Warm Brown Ink:**').replace('**Muted Plum:**','**Muted Warm Brown:**').replace('**Pink Divider:**','**Cream Divider:**')
s=s.replace('Large headings sit beside structured service or pricing content; photographs use asymmetric two-column grids.','The services heading leads a three-column image grid. Pricing keeps its heading beside native disclosures; studio media uses asymmetric two-column grids.')
s=s.replace('Services retain two columns.','Services change from three to two columns below 700px. The design inspiration grid changes from four to two columns; social links change from three columns to a vertical list.')
s=s.replace('The decorative manicure campaign image is inspiration, while the original pedicure photograph and video document salon activity.','Seven unique AI images illustrate the hero, six services, the studio introduction and a four-image inspiration collection. All generated assets are local WebP files with provenance in assets/provenance.json. A concise German label identifies the inspiration collection. The original pedicure photograph and video remain in a separate media pair.')
s=s.replace('Services are open text groups with a top divider, serif title and constrained description.','Services are open image-led groups: rectangular campaign photograph, serif title and constrained description, without a card shell. The image grid uses three columns on desktop and two on mobile. Image hover scales gently to 1.035.')
s=s.replace('The user-confirmed character is elegant and gentle, retaining petal.','The user-confirmed character is elegant and gentle, with colors matching the original logo.')
s=s.replace('elegant, gentle petal character','elegant, gentle logo-derived palette')
s=s.replace('approved petal direction','approved ivory, gold and blush direction')
s=s.replace('rose','gold').replace('Rose','Gold')
s=s.replace('Images and open content regions have square corners. Controls use the small shared radius;','Images and open content regions have square corners. Social icon tiles use 16px corners, the link focus boundary uses 12px, and other controls use the small shared 6px radius;')
s=s.replace('## Do\'s and Don\'ts', '''### Social Links

Use the official local Tabler outline brand SVGs for Instagram, Facebook and TikTok, rendered with currentColor in 54px cream icon tiles. Gold icon strokes match the logo; hover and focus fill the tile bronze-gold and turn the icon white. Pair each icon with the platform name and actual profile handle. The main section uses three columns on desktop and a vertical list on mobile. Footer icons use a quieter 17px size. Keep SVGs aria-hidden because the adjacent text supplies the accessible name. The MIT license is included in assets/icons/LICENSE.txt.

## Do's and Don'ts''')
p.write_text(s,encoding='utf-8')

sidecar=root/'.impeccable/design.json'
d=json.loads(remap(sidecar.read_text(encoding='utf-8')))
for key,meta in d['extensions']['colorMeta'].items():
    value=meta['canonical']
    rgb=tuple(int(value[i:i+2],16)/255 for i in (1,3,5))
    h,l,sat=colorsys.rgb_to_hls(*rgb)
    ramp=[]
    for light in [.15,.2643,.3786,.4929,.6071,.7214,.8357,.95]:
        channels=colorsys.hls_to_rgb(h,light,sat*min(1,(1-light)/.2))
        ramp.append('#'+''.join(f'{round(c*255):02x}' for c in channels))
    meta['tonalRamp']=ramp
    meta['displayName']={'gold':'Bronze Gold','gold-deep':'Deep Bronze','background':'Warm Ivory','cream':'Warm Cream','petal':'Petal Blush','ink':'Warm Brown Ink','muted':'Muted Warm Brown','line':'Cream Divider','white':'White'}[key]
d['narrative']['overview']=s.split('## Overview')[1].split('**Key Characteristics:**')[0].strip()
d['narrative']['keyCharacteristics']=['Warm ivory, bronze-gold and blush-pink colors from the original logo.','Self-hosted Cormorant Garamond and DM Sans.','Six image-led services and a four-image AI inspiration collection.','Custom styled local Tabler social icons with hover and focus states.','Native pricing disclosures, keyboard access and reduced motion.']
for field in ['dos','donts']:
    d['narrative'][field]=[v.replace('elegant, gentle petal character','elegant, gentle logo-derived palette').replace('approved petal direction','approved logo palette') for v in d['narrative'][field]]
for component in d['components']:
    component['description']=component.get('description','').replace('Rose','Bronze-gold').replace('rose','gold')
d['extensions']['imagery']={'uniqueAIImages':7,'newImages':6,'delivery':'local WebP','desktopServicesColumns':3,'mobileServicesColumns':2,'desktopInspirationColumns':4,'mobileInspirationColumns':2,'provenance':'assets/provenance.json','label':'Design-Inspirationen, mit KI gestaltet.'}
d['extensions']['socialIcons']={'library':'Tabler Icons','style':'outline','brands':['instagram','facebook','tiktok'],'tileSize':'54px','tileRadius':'16px','stroke':'2','footerSize':'17px','hover':'bronze-gold background and white stroke','license':'MIT'}
sidecar.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')

direction=root/'.impeccable/direction.md'
direction.write_text('''# Latest approved update

User requested more AI images, colors matching the original logo and custom social icons. The current approved palette is warm ivory #fffaf5, cream #f5ebe2, bronze-gold #8a613b, deep bronze #6c472b and petal blush #ead1cc. This supersedes the earlier rose/plum palette. Six new generated beauty images supplement the original hero; local WebP delivery keeps the page light. Services use a three-column photo grid (two on mobile); the AI inspiration collection uses four columns (two on mobile). Instagram, Facebook and TikTok use local Tabler SVGs inside custom cream/gold icon tiles. Business information, prices, section anchors, language and booking interactions are preserved.

''' + direction.read_text(encoding='utf-8'),encoding='utf-8')
print('Updated product-linked design documentation and sidecar.')
