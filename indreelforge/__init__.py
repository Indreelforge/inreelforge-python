"""
InReelForge — Official Python SDK

Social Media API to upload videos, photos & text to Instagram, YouTube,
TikTok, Facebook, X, LinkedIn, Threads, Pinterest, Reddit & Bluesky
with a single API call.

Usage:
    from inreelforge import InReelForge

    client = InReelForge(api_key="your-api-key")
    result = client.upload_video(
        user="my-profile",
        platforms=["instagram", "tiktok", "youtube"],
        video_path="./video.mp4",
        title="My awesome video",
    )
"""

from .client import InReelForge, InReelForgeError

__version__ = "1.0.0"
__all__ = ["InReelForge", "InReelForgeError"]
