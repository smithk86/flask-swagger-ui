from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'quart_swagger_ui/README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='quart-swagger-ui',
    version='3.23.10',
    description='Swagger UI blueprint for Quart',
    long_description=long_description,
    zip_safe=False,

    url='https://github.com/sveint/quart-swagger-ui',

    author='Svein Tore Koksrud Seljebotn',
    author_email='sveint@gmail.com',
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='quart swagger',
    packages=['quart_swagger_ui'],
    install_requires=['quart'],
    package_data={
        'quart_swagger_ui': [
            'README.md',
            'templates/*.html',
            'dist/VERSION',
            'dist/LICENSE',
            'dist/README.md',
            'dist/*.html',
            'dist/*.js',
            'dist/*.css',
            'dist/*.png'
        ],
    }
)
