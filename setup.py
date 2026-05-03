from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="indreelforge",
    version="1.0.0",
    author="InReelForge",
    author_email="support@indreelforge.com",
    description="Official Python SDK for InReelForge — Social Media API to post to Instagram, YouTube, TikTok, Facebook, X, LinkedIn, Threads, Pinterest, Reddit & Bluesky",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://indreelforge.com",
    project_urls={
        "Documentation": "https://indreelforge.com/docs",
        "Source": "https://github.com/Indreelforge/inreelforge-python",
        "Bug Tracker": "https://github.com/Indreelforge/inreelforge-python/issues",
    },
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "social-media-api", "instagram-api", "youtube-api", "tiktok-api",
        "facebook-api", "twitter-api", "linkedin-api", "threads-api",
        "pinterest-api", "reddit-api", "bluesky-api",
        "social-media-posting", "video-upload", "indreelforge",
    ],
)
