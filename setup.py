from setuptools import setup
import re

version = ''
with open('guilded/ext/menus/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

setup(
    name='guilded-ext-menus',
    author='Rapptz, shayypy',
    url='https://github.com/shayypy/guilded-ext-menus',
    version=version,
    packages=['guilded.ext.menus'],
    license='MIT',
    description='An extension module to make reaction-based menus with guilded.py',
    install_requires=['guilded.py>=1.2.0'],
    python_requires='>=3.8',
)
