import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycyber",
    version="0.0.1",
    author="daohu527",
    author_email="daohu527@gmail.com",
    description="Apollo autopilot middleware.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daohu527/pycyber",
    project_urls={
        "Bug Tracker": "https://github.com/daohu527/pycyber/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    package_data={'': [
        'internal/*.so',
        'tools/cyber_node/cyber_node.py',
        'tools/cyber_channel/cyber_channel.py',
    ]},
    packages=setuptools.find_packages(where="."),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'cyber_channel = pycyber.tools.cyber_channel.main:main',
            'cyber_node = pycyber.tools.cyber_node.main:main',
        ],
    },
    python_requires=">=3.6",
)
