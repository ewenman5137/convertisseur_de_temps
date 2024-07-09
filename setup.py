from setuptools import setup, find_packages

setup(
    name='convertisseur_de_temps',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author="Ewen BUHOT",
    author_email="ewenbuhot@outlook.fr",
    description="Un convertisseur de temps en Python",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/ewenman5137/convertisseur_de_temps",  # Remplacez par l'URL de votre dépôt
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
