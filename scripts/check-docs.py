"""Check the configured publication root, independent of the archived root config."""
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / 'home/shivansh/AIO3/AIO3-DOCS'
config = json.loads((ROOT / 'docs.json').read_text())
errors = []


def routes(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from routes(item)
    elif isinstance(value, dict):
        for key in ('pages', 'groups', 'tabs'):
            if key in value:
                yield from routes(value[key])


def exists(route):
    path = ROOT / unquote(urlsplit(route).path).lstrip('/')
    return any(p.is_file() for p in (path, Path(str(path) + '.mdx'), Path(str(path) + '.md'), path / 'index.mdx'))


pages = list(routes(config['navigation']))
for route, count in Counter(pages).items():
    if count > 1:
        errors.append(f'Duplicate navigation route: {route}')
    if not exists(route):
        errors.append(f'Missing navigation route: {route}')
for key in ('logo', 'favicon'):
    value = config.get(key, {})
    for link in value.values() if isinstance(value, dict) else [value]:
        if isinstance(link, str) and link.startswith('/') and not exists(link):
            errors.append(f'Missing {key}: {link}')
for page in ROOT.rglob('*.mdx'):
    content = page.read_text()
    body = re.sub(r'\A---\n.*?\n---\s*', '', content, flags=re.S)
    if not body.strip():
        errors.append(f'Empty page: {page.relative_to(ROOT)}')
    for link in re.findall(r'(?:href=[\"\']|\]\()(/[^\s\"\')]+)', content):
        if not link.startswith('//') and not exists(link):
            errors.append(f'{page.relative_to(ROOT)}: missing link {link}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} navigation routes, page bodies and local links/assets in {ROOT}')
